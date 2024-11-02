from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeMeta

from .models import UserModel
from .schemas import UserCreate, UserInfo
from ..services import FakeService, DatabaseService


class FakeUserService(FakeService):
    model = UserCreate
    retrieve_model = UserInfo

    unique_model_fields = ["username"]

    def to_retrieve_model(self, obj: model) -> retrieve_model:
        return self.retrieve_model(**obj.model_dump(exclude={"password"}))


class DatabaseUserService(DatabaseService):
    model = UserModel
    create_model = UserCreate
    retrieve_model = UserInfo

    unique_model_fields = ["username"]

    def database_model_from_pydantic_model(self, data: create_model):
        new_instance = self.model()
        new_instance.username = data.username
        new_instance.password = data.password
        new_instance.age = data.age
        new_instance.name = data.name
        new_instance.email = data.email
        new_instance.is_subscribed = data.is_subscribed

    def to_retrieve_model(self, obj: DeclarativeMeta) -> retrieve_model:
        return self.retrieve_model.from_orm(obj)
