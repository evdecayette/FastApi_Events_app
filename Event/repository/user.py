from ..models import Users
from sqlmodel import Session,select
from fastapi import HTTPException
from datetime import datetime
from Event import hashing



def get_all(db:Session):    
    users = db.exec(select(Users)).all()
    return users

def get_an_user(db:Session, user_id:int):
    user = db.exec(select(Users).where(Users.userId == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create(db:Session, user:Users):
    user.password = hashing.Hash.encrypt(user.password)
    user.updated_at = datetime.now()
    current_date = datetime.now()
    user.created_at = current_date.strftime("%Y-%m-%d")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update(user_id:int, db: Session, updated_user: Users):
    user = db.exec(select(Users).where(Users.userId == user_id)).first()
    user.updated_at = datetime.utcnow()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in updated_user.dict().items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user

def destroy(user_id:int,db:Session):
    user = db.exec(select(Users).where(Users.userId == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}