from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from db.database import get_db
import jwt
from datetime import datetime, timedelta

from models.models_users import User
from utils import verify_password, create_jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router_login = APIRouter()


@router_login.post("/get_token")
def login(response: Response, db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="账号或密码错误")

    data = {
        "username": user.username,
        "password": user.hashed_password
    }
    token = create_jwt_token(data)
    response.set_cookie(key="token", value=token, httponly=True, samesite="strict")
    return {"access_token": token, "token_type": "bearer"}


@router_login.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="token")
    return {"detail": "Successfully logged out"}
