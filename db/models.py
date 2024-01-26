from typing import List, Optional
from fastapi import Request
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON, Boolean
from datetime import date, datetime, timedelta
from db.base import metadata


role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)

)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False)
)

# class UserManager():
#     reset_password_token_secret = SECRET
#     verification_token_secret = SECRET

#     async def on_after_register(self, user: user, request: Optional[Request] = None):
#         print(f"User {user.id} has registered.")

#     def start(self, request =Request ):
#         self.request: Request = request
#         self.errors: List = []
#         self.username: Optional[str] = None
#         self.email: Optional[str] = None
#         self.password: Optional[str] = None
    
#     async def getting_data(self):
#         form = self.request.form

#     async def validation(self):