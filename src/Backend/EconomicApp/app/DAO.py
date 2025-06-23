from typing import Dict

from sqlalchemy import select,insert,delete
from models import Work,User,Education
from database import session_maker
from schemas import *

class BaseDAO:
    model = None


    @classmethod
    def get_all(cls):
        with session_maker() as session:
            return session.query(cls.model).all()

    @classmethod
    def retrieve(cls, model_id):
        with session_maker() as session:
            return session.query(cls.model).filter_by(model_id)

    @classmethod
    def create(cls,data:Dict[UserBase]):
        with session_maker() as session:
            data = cls.model(**data)
            session.add(data)
            session.commit()
            return data

    @classmethod
    def update(cls, model_id:int, updated_data):
        with session_maker() as session:
            human = session.query(cls.model).get(model_id)
            if not human:
                return None
            for key, value in updated_data.items():
                setattr(human, key, value)
            session.commit()
            return human

    @classmethod
    def delete(cls, model_id: int):
        with session_maker() as session:
            human = cls.retrieve(model_id)
        if human:
            session.delete(human)
            session.commit()

class UserDAO(BaseDAO):
    model = User

class WorkDAO(BaseDAO):
    model = Work

class EducationDAO(BaseDAO):
    model = Education