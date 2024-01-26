from typing import Optional
import uuid

from pydantic import BaseModel, EmailStr
import pydantic_core

class user_base(BaseModel):
    email: EmailStr
    username: str

class UserRead(user_base):
    password: str
    
    class Config:
        orm_mode = True


class UserCreate(user_base):
    password: str
    class Config:
        orm_mode = True

class UserforUser(user_base):
    id: int
    class Config:
        orm_mode = True

class User_login(BaseModel):
    email: str
    password: str

    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

