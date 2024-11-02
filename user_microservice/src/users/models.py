from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable
import sqlalchemy as sa
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from ..db.base import Base
from .schemas import UserDB
from ..db.session import get_async_session


class UserTable(Base, SQLAlchemyBaseUserTable):
    first_name: Mapped[str] = sa.Column(
        sa.String(length=100),
        server_default=sa.sql.expression.literal("No first name given"),
        nullable=False
    )
    last_name: Mapped[str] = sa.Column(
        sa.String(length=100),
        server_default=sa.sql.expression.literal("No last name given"),
        nullable=False
    )


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(UserDB, session, UserTable)
