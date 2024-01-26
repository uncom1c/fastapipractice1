from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from db.database import user_to_db
from db.models import user as User
import psycopg2
from psycopg2 import Error

from auth.schemas import UserCreate
from config import JWT_SECRET
SECRET = JWT_SECRET

