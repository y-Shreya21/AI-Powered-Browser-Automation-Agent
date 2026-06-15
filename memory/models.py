# memory/models.py

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Memory(Base):

    __tablename__ = "memories"

    id = Column(Integer, primary_key=True)

    goal = Column(String)

    action = Column(String)

    observation = Column(String)

    timestamp = Column(DateTime)