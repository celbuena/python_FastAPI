from sqlalchemy.orm import Session
from . import models, schema
import bcrypt

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def login(db: Session, user: schema.UserLogin):
    return db.query(models.User).filter(models.User.username == user.username, models.User.password == user.password).first()

def create_user(db: Session, user: schema.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    db_user = models.User(username=user.username, password=hashed_password, name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_request: schema.UserInfo):
    user = db.query(models.User).filter(models.User.username == user_request.username).first()

    setattr(user, 'name', user_request.name)
    setattr(user, 'email', user_request.email)

    db.commit()

    userUpdate = models.User(username=user.username, name=user.name, email=user.email)

    return userUpdate