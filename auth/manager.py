
from typing import Optional, List
from db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, Request, Form
# from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas

from db.models import user

from config import JWT_SECRET

SECRET = JWT_SECRET




        
    # async def create(
    #     self,
    #     user_create: schemas.UC,
    #     safe: bool = False,
    #     request: Optional[Request] = None,
    # ) -> models.UP:
    #     await self.validate_password(user_create.password, user_create)

    #     existing_user = await self.user_db.get_by_email(user_create.email)
    #     if existing_user is not None:
    #         raise exceptions.UserAlreadyExists()

    #     user_dict = (
    #         user_create.create_update_dict()
    #         if safe
    #         else user_create.create_update_dict_superuser()
    #     )
    #     password = user_dict.pop("password")
    #     user_dict["hashed_password"] = self.password_helper.hash(password)
    #     user_dict["role_id"] = 1

    #     created_user = await self.user_db.create(user_dict)

    #     await self.on_after_register(created_user, request)

    #     return created_user



# async def get_user_manager(user_db=Depends(get_async_session)):
#     yield UserManager(user_db)
