from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
# from auth.auth import auth_backend
import uvicorn
from db.base import metadata
from db.database import engine
# from auth.database import User
# from auth.manager import get_user_manager

# from auth.schemas import UserCreate, UserRead

import os


from api.router import router as api_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    
    #
    print(1)
    await create_tables()
    print(2)
    
    yield

    # 


async def create_tables() -> None:
    print(3)
    async with engine.begin() as conn:
        print(4)
        await conn.run_sync(metadata.create_all)
        print(5)


app = FastAPI(lifespan=lifespan) #сюда что-то дополнить



app.include_router(router=api_router)