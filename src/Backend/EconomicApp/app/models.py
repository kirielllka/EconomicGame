from sqlalchemy import Column,Integer,String, Float, DATETIME, func, ForeignKey

from database import Base

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=1000)
    experience = Column(Integer)
    education = Column(ForeignKey(''))
    created_at = Column(DATETIME, default=func.now)

class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer,primary_key=True)
    title = Column(String)
    cost = Column(Integer)


class Work(Base):
    __tablename__ = 'work'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    min_lvl = Column(Integer)
    salary = Column(Integer)
    education = Column(ForeignKey(''))
    improvement = Column(Integer)