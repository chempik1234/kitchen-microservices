import uvicorn
from .config import AppConfig
from .create_app import app

from .users import (fastapi_users_reset_password_router,
                    fastapi_users_register_router,
                    fastapi_users_verify_router,
                    fastapi_users_auth_router,
                    fastapi_users_users_router)
from .users.router import router as custom_user_router

app.include_router(custom_user_router, tags=["users-misc"])
app.include_router(fastapi_users_auth_router, prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users_register_router, prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users_reset_password_router, prefix="/auth", tags=["auth"])
app.include_router(fastapi_users_verify_router, prefix="/auth", tags=["auth"])
app.include_router(fastapi_users_users_router, prefix="/users", tags=["users"])

# if __name__ == '__main__':
#     uvicorn.run(app, host=config.Port)
