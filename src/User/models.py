from sqlalchemy import Column,String,Integer,Boolean,ForeignKey

from database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    tg_id = Column(Integer)
    exp = Column(Integer)
    lvl = Column(Integer)
    balance = Column(Boolean,default=0)
    work = Column(Integer,ForeignKey('work.id',ondelete='SET NULL'), nullable=True)