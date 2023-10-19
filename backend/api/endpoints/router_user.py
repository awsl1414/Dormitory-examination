from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas_users import UserCreate, User
from db.database import get_db
from crud.crud_user import create_user

router_user = APIRouter()


@router_user.post("/create_user", response_model=User)
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, username=user.username, password=user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="用户名已存在")
    return db_user
