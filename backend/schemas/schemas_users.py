from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        from_attributes = True


class User(UserInDB):
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "root",
                "password": "123456"
            }
        }
