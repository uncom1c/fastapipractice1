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
    found_user = found_user.mappings().first()
    
    if found_user:
        return UserRead(**found_user)
    else:
        return None

async def get_email(email, db: AsyncSession = Depends(get_async_session)):

    query1 = user.select().where(user.c.email == email)
    found_user = await db.execute(query1)
    found_user = found_user.mappings().first()
    if found_user:
        return UserRead(**found_user)
    else:
        return None


@router.post("/register")
async def register_handler(user_create: UserCreate, db: AsyncSession = Depends(get_async_session)):
    
    # validate
    # put to db
    # return from db
    # inserted_user = user.insert().values(email = user_create.email, username = user_create.username, password = user_create.password)
    if await get_email(user_create.email, db):
        return "email taken"
    if await get_username(user_create.username, db):
        return "username taken"
    
    user_create = encode_user(user_create)
    query = user.insert().values(**user_create.dict())
    inserted_user = await db.execute(query)
    await db.commit()

    return inserted_user.mappings().all




@router.post("/login")
async def login_handler(user_login: User_login, db: AsyncSession = Depends(get_async_session)):
    usertry = await get_username(user_login.username , db)
    if not usertry:
        return "no such user"

    if not verify_password(user_login.password, usertry.password):
        return "wrong password"
    
    return "login ok"
 



    # validate
    # get from db
    # generate jwt
    # return jwt
    
    return jwt



@router.get("/user")
async def user_login_handler(username, db: AsyncSession = Depends(get_async_session)):
    # decode and verify jwt
    # get user from db by jwt
    # return user
 
    
    return await get_username(username, db)

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