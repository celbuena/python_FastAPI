from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DB connection
#user name: root
#pass: admin
#db_name: db_zicare

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost:3306/db_zicare"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()