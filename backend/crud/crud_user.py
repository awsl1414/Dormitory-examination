from sqlalchemy.orm import Session
from models.models_users import User
from utils import get_password_hash, verify_password


def create_user(db: Session, username: str, password: str):
    db_user = User(username=username, hashed_password=get_password_hash(password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
