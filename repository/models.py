from sqlalchemy import Column, Integer, String
from repository.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    email = Column(String)