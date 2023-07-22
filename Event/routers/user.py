from fastapi import APIRouter, Depends,HTTPException
from typing import List
from ..models import Users, ShowUser
from Event import database, hashing
from sqlmodel import Session as SQLModelSession,select
from datetime import datetime, date
from ..repository import user
get_db = database.get_db

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

# User routes
@router.get("/", response_model=List[ShowUser])
def get_users(db: SQLModelSession = Depends(get_db)):
    return user.get_all(db)

@router.get("/{user_id}", response_model=ShowUser)
def get_user(user_id: int, db: SQLModelSession = Depends(get_db)):
    return user.get_an_user(user_id,db)


@router.post("/", response_model=ShowUser)
def create_user(an_user: Users,db: SQLModelSession = Depends(get_db)):
    return user.create(an_user,db)

@router.put("/{user_id}", response_model=Users)
def update_user(user_id: int, updated_user: Users,db: SQLModelSession = Depends(get_db)):
    return user.update(user_id,db, update_user)

@router.delete("/{user_id}")
def delete_user(user_id: int,db: SQLModelSession = Depends(get_db)):
    return user.destroy(user_id,db)