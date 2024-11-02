from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, CookieTransport
from ..config import AppConfig

app_config = AppConfig()


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(app_config.JWTSecret, lifetime_seconds=app_config.JWT_LIFETIME_SECONDS)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=CookieTransport(),
    get_strategy=get_jwt_strategy
)
