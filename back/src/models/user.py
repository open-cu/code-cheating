from sqlalchemy import Column, Integer, String, Float

from src.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)

    average_coefficient = Column(Float)
    maximum_coefficient = Column(Float)
    median_coefficient = Column(Float)
