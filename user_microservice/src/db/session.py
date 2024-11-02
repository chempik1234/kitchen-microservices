import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from ..config import AppConfig
logger = logging.getLogger(__name__)

app_config = AppConfig()

SQLALCHEMY_DATABASE_URL = app_config.DbURL

try:
    session_class = AsyncSession
    engine = create_async_engine(
        SQLALCHEMY_DATABASE_URL
    )
except Exception as e:
    logger.error(e)
    session_class = Session
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )


async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=session_class)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
