from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from repository import models, schema, crud
from repository.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/register")
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    isExistUser = crud.get_user_by_username(db, user.username)
    if isExistUser:
        raise HTTPException(status_code=400, detail="User Already Exist")
    user = crud.create_user(db, user)
    return {"username": user.username, "email": user.email, "name": user.name}

@app.post("/login")
def login(user: schema.UserLogin, db: Session = Depends(get_db)):
    isExistUser = crud.login(db, user)
    if isExistUser is None:
        raise HTTPException(status_code=400, detail="Username or Password Wrong")
    return {"username": user.username}

@app.put("/update")
def update(user: schema.UserInfo, db: Session = Depends(get_db)):
    userUpdate = crud.update_user(db, user)

    return {"username": userUpdate.username, "email": userUpdate.email, "name": userUpdate.name}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)