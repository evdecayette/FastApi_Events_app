from fastapi import APIRouter, Depends,HTTPException
from typing import List
from ..models import Likes
from Event import database
from sqlmodel import Session as SQLModelSession,select
from datetime import datetime, date


get_db = database.get_db

router = APIRouter(
    prefix="/like",
    tags=["Like"]
)


# Likes routes
@router.get("/", response_model=List[Likes])
def get_likes(db: SQLModelSession = Depends(get_db)):
    likes = db.exec(select(Likes)).all()
    return likes

@router.get("/{like_id}", response_model=Likes)
def get_tag(like_id: int,db: SQLModelSession = Depends(get_db)):
    like = db.exec(select(Likes).where(Likes.likeId == like_id)).first()
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    return like

@router.post("/", response_model=Likes)
def create_like(like: Likes,db: SQLModelSession = Depends(get_db)):
    db.add(like)
    db.commit()
    db.refresh(like)
    return like

@router.put("/{like_id}", response_model=Likes)
def update_like(like_id: int, updated_like: Likes,db: SQLModelSession = Depends(get_db)):
    like = db.exec(select(Likes).where(Likes.likeId == like_id)).first()
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    for field, value in updated_like.dict().items():
        setattr(like, field, value)
    like.created_at = datetime.utcnow()
    db.commit()
    db.refresh(like)
    return like

@router.delete("/{like_id}")
def delete_like(like_id: int,db: SQLModelSession = Depends(get_db)):  
    like = db.exec(select(Likes).where(Likes.likeId == like_id)).first()
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    db.delete(like)
    db.commit()
    return {"message": "Like deleted successfully"}