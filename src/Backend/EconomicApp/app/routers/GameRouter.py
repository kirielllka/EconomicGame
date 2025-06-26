from fastapi import APIRouter
from ..DAO import UserDAO,WorkDAO,EducationDAO
from .. import schemas

Game_Router = APIRouter()

class BaseViewSet:
    model_schema = None
    responce_schema = None
    ulr = None
    model_DAO = None

    @classmethod
    @Game_Router.post(path=f'/{ulr}/',response_model=responce_schema)
    async def create(cls, data:model_schema):
        return cls.model_DAO.create(data)

    @classmethod
    @Game_Router.get(path=f'/{BaseViewSet.ulr}/', response_model=responce_schema)
