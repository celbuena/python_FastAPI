from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

#Request schema register
class UserCreate(UserBase):
    password: str
    name: str
    email: str

class UserInfo(UserBase):
    name: str
    email: str

class UserLogin(UserBase):
    password: str

class UserUpdateInfo(UserBase):
    name: str
    email: str

    class Config:
        orm_mode = True