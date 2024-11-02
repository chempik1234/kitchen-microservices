from betterconf import Config
from betterconf.config import Field


class AppConfig(Config):
    Port: int = Field("PORT", default=8081)
    LogLevel: str = Field("LOG_LEVEL", default="ERROR")
    # DbHost: str = Field("DATABASE_HOST", default="db")
    # DbPort: int = Field("DATABASE_PORT", default=5432)
    # DbUser: str = Field("DATABASE_USER", default="postgres")
    # DbName: str = Field("DATABASE_NAME", default="postgres")
    DbPassword: str = Field("DATABASE_PASSWORD", default="postgres")
    DbURL: str = Field("DATABASE_URL", default="sqlite:///../../default_db.db")  # engine postgresql != engine sqlite
    JWTSecret: str = Field("JWT_SECRET", default="mysupersecret")
    JWT_LIFETIME_SECONDS: int = Field("JWT_LIFETIME_SECONDS", default=3600)

    URL_PREFIX: str = Field("USER_MICROSERVICE_PREFIX", default="")
