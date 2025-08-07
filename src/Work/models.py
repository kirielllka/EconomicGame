from sqlalchemy import String, Integer, Boolean, Column

from database import Base


class Work(Base):
    __tablename__ = 'work'
    id = Column(Integer, primary_key=True)
    work_name = Column(String)
    salary = Column(Boolean)
    need_lvl = Column(Integer)