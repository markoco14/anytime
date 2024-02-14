"""CRUD functions for users table"""
from sqlalchemy.orm import Session

from core.memory_db import USERS
from models.user_model import DBUser
import schemas



def get_user_by_email(db: Session, email: str):
    """ Returns a user by email"""
    db_user = db.query(DBUser).filter(
        DBUser.email == email).first()
    
    return db_user

def get_user_by_id(db: Session, user_id: int):
    db_user = db.query(DBUser).filter(
        DBUser.id == user_id).first()
    
    return db_user



def create_user(db: Session, user: schemas.CreateUserHashed) -> schemas.AppUser:
    """ Creates a user """
    
    db_user = DBUser(**user.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def list_users(db: Session):
    """ Returns a list of users """
    db_users = db.query(DBUser).all()
    return db_users


def patch_user(current_user: schemas.User, display_name: str = None):
    """ Updates a user """
    if display_name is not None:
        current_user.display_name = display_name

    USERS.update({current_user.email: current_user})



