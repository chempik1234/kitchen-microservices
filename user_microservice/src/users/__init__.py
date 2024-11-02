from fastapi_users import FastAPIUsers

from .backends import auth_backend
from .manager import get_user_manager
from .schemas import User, UserCreate, UserUpdate, UserDB

fastapi_users_object = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

fastapi_users_users_router = fastapi_users_object.get_users_router()
fastapi_users_auth_router = fastapi_users_object.get_auth_router(auth_backend)
fastapi_users_register_router = fastapi_users_object.get_register_router()
fastapi_users_reset_password_router = fastapi_users_object.get_reset_password_router()
fastapi_users_verify_router = fastapi_users_object.get_verify_router()
