from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeMeta


class BasicService:
    model = object
    retrieve_model = BaseModel

    unique_model_fields = set()

    def __init__(self, *args, **kwargs):
        pass

    def create_object(self, instance):
        return True

    def to_retrieve_model(self, obj: model) -> retrieve_model:
        return self.retrieve_model()

    def all_objects(self):
        return []

    def get_objects(self):
        return [self.to_retrieve_model(i) for i in self.all_objects()]

    def get_object(self, **kwargs):
        for obj in self.all_objects():
            found = True
            for key, value in kwargs.items():
                if getattr(obj, key, None) != value:
                    found = False
                    break
            if found:
                return self.to_retrieve_model(obj)


class FakeService(BasicService):
    model = BaseModel
    retrieve_model = BaseModel

    def __init__(self, fake_db=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if fake_db is None:
            fake_db = []
        else:
            for num, item in enumerate(fake_db):
                if not isinstance(item, self.model):
                    fake_db[num] = self.model(**item)
        self.fake_db = fake_db

    def create_object(self, instance):
        if isinstance(instance, self.model):
            self.fake_db.append(instance)
        else:
            self.fake_db.append(self.model(**instance))

    def all_objects(self):
        return self.fake_db.copy()

    def to_retrieve_model(self, obj: model) -> retrieve_model:
        return self.retrieve_model(**obj.model_dump())


class DatabaseService(BasicService):
    model = DeclarativeMeta
    create_model = BaseModel
    retrieve_model = BaseModel

    def __init__(self, db_session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = db_session

    def all_objects(self):
        with self.session() as db_session:
            result = db_session.execute(select(self.model))
            return result.scalars.all()

    def database_model_from_pydantic_model(self, data: create_model):
        raise NotImplementedError()

    def create_object(self, data: BaseModel):
        with self.session() as db_session:
            instance = self.database_model_from_pydantic_model(data)
            db_session.add(instance)
            db_session.commit()
            return instance

    def get_objects(self, **kwargs):
        with self.session() as db_session:
            return db_session.query(self.model).filter_by(**kwargs).first()
