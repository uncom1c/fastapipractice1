from datetime import datetime
import os
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, declared_attr, mapped_column

from sqlalchemy import Table

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, func, select

from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS

from auth.schemas import UserCreate



DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


Base: DeclarativeMeta = declarative_base()

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)
