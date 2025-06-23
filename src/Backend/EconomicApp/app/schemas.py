from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    balance: float = Field(default=1000.0, ge=0, description="Баланс пользователя")
    experience: int = Field(default=0, ge=0, description="Опыт пользователя")
    education_id: Optional[int] = Field(None, description="ID образования")

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    balance: Optional[float] = Field(None, ge=0)
    experience: Optional[int] = Field(None, ge=0)
    education_id: Optional[int] = None


class EducationBase(BaseModel):
    title: str = Field(..., max_length=100, description="Название образования")
    cost: int = Field(..., ge=0, description="Стоимость обучения")

class EducationCreate(EducationBase):
    pass

class EducationUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    cost: Optional[int] = Field(None, ge=0)



class WorkBase(BaseModel):
    title: str = Field(..., max_length=100, description="Название работы")
    min_lvl: int = Field(..., ge=1, description="Минимальный уровень для работы")
    salary: int = Field(..., ge=0, description="Зарплата")
    education_id: Optional[int] = Field(None, description="Требуемое образование")
    improvement: int = Field(default=0, ge=0, description="Бонус к улучшению")

class WorkCreate(WorkBase):
    pass

class WorkUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    min_lvl: Optional[int] = Field(None, ge=1)
    salary: Optional[int] = Field(None, ge=0)
    education_id: Optional[int] = None
    improvement: Optional[int] = Field(None, ge=0)

