from typing import Optional

from pydantic import Field

from fastapi_users import models as fastapi_user_models


class User(fastapi_user_models.BaseUser):
    first_name: Optional[str]
    last_name: Optional[str]


class UserCreate(fastapi_user_models.BaseUserCreate):
    first_name: Optional[str]
    last_name: Optional[str]


class UserUpdate(fastapi_user_models.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]


class UserDB(User, fastapi_user_models.BaseUserDB):
    pass
