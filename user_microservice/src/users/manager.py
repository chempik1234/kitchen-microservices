from fastapi import Depends
from fastapi_users import BaseUserManager
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from ..config import AppConfig
from .models import get_user_db
from .schemas import UserDB, UserCreate

app_config = AppConfig()


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = app_config.JWTSecret
    verification_token_secret = app_config.JWTSecret


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
