import datetime
import time
from typing import Dict, List
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy import Column
from auth.schemas import User_login, UserCreate, UserforUser, Token, TokenData, UserRead
from db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import user 
from config import JWT_ALGORITHM, JWT_SECRET
from passlib.context import CryptContext
from sqlalchemy.exc import *
from auth.auth import signJWT, decodeJWT
# from api.dependencies import *


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def encode_user(user: UserCreate):
    return UserCreate(email = user.email, username = user.username, password = get_password_hash(user.password))

async def get_username(username, db: AsyncSession = Depends(get_async_session)):

    query = user.select().where(user.c.username == username)
    found_user = await db.execute(query)
    print(found_user.all())
    found_user = found_user.one()
    print(found_user.one())
    
    if found_user:
        # return UserRead(**found_user)
        return found_user
    else:
        return None

async def get_email(email, db: AsyncSession = Depends(get_async_session)):

    query1 = user.select().where(user.c.email == email)
    found_user = await db.execute(query1)
    found_user = found_user.mappings().one()
    if found_user:
        return found_user
    else:
        return None

async def get_id(_id, db: AsyncSession = Depends(get_async_session)):

    query1 = user.select().where(user.c.id == _id)
    found_user = await db.execute(query1)
    found_user = found_user.mappings().one()
    if found_user:
        return found_user
    else:
        return None


@router.post("/register")
async def register_handler(user_create: UserCreate, db: AsyncSession = Depends(get_async_session)):
    
    # validate
    # put to db
    # return from db
    # inserted_user = user.insert().values(email = user_create.email, username = user_create.username, password = user_create.password)
    # if await get_email(user_create.email, db):
    #     return "email taken"
    # if await get_username(user_create.username, db):
    #     return "username taken"
    
    user_create = encode_user(user_create)
    query = user.insert().values(**user_create.dict())

    try:
        inserted_user = await db.execute(query)
    except IntegrityError:
        return "такой пользователь уже есть, ХУЕСОС"
    
    await db.commit()

    return f"Поздравляем, вы зарегались, пользователь {inserted_user.inserted_primary_key}"




@router.post("/login")
async def login_handler(user_login: User_login, db: AsyncSession = Depends(get_async_session)):

    result = await get_email(user_login.email, db)
    if not result:
        return "no such user"

    if not verify_password(user_login.password, result.password):
        return "wrong password"
    
    # generate jwt
    # return jwt
    exp_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
    print(exp_time)
    jwt_token = jwt.encode(
        {
            "id": result["id"],
            "exp": exp_time
        },
        JWT_SECRET,
        JWT_ALGORITHM
    )

    return jwt_token



@router.get("/user")
async def user_login_handler(jwt_token, db: AsyncSession = Depends(get_async_session)):
    # decode and verify jwt
    # get user from db by jwt
    # return user
    

    try:
        decoded_jwt = jwt.decode(jwt_token, JWT_SECRET, JWT_ALGORITHM, )
        user_id = decoded_jwt["id"]
    except jwt.exceptions.DecodeError:
        return "ПАШЁЛ НАХУЙ ХАКЕР Я ТВАЮ МАМАШУ ЕБАЛ"
    except jwt.exceptions.ExpiredSignatureError:
        return "перелогинься, время вышло"
    except:
        return "Ошибка какая-то, бля хз"

    return await get_id(user_id, db)

@router.get("/email")
async def user_email_handler(email, db: AsyncSession = Depends(get_async_session)):
    # decode and verify jwt
    # get user from db by jwt
    # return user
   
    
    return await get_email(email, db)

@router.get("/all")
async def all_handler(db: AsyncSession = Depends(get_async_session)):
    query = user.select()
    result = await db.execute(query)
    
    return (result.mappings().all())

@router.get("/zalupa")
async def zalupa_handler():
    return "hello world"