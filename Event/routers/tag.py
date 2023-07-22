from fastapi import APIRouter, Depends,HTTPException
from typing import List
from ..models import Tags
from Event import database, hashing
from sqlmodel import Session as SQLModelSession,select
from datetime import datetime, date

get_db = database.get_db

router = APIRouter(
    prefix="/tag",
    tags=["Tag"]
)

# Tags routes
@router.get("/", response_model=List[Tags])
def get_tags(db: SQLModelSession = Depends(get_db)):
    tags = db.exec(select(Tags)).all()
    return tags

@router.get("/{tag_id}", response_model=Tags)
def get_tag(tag_id: int,db: SQLModelSession = Depends(get_db)):
    tag = db.exec(select(Tags).where(Tags.tagId == tag_id)).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@router.post("/", response_model=Tags)
def create_tag(tag: Tags,db: SQLModelSession = Depends(get_db)):
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

@router.put("/{tag_id}", response_model=Tags)
def update_tag(tag_id: int, updated_tag: Tags,db: SQLModelSession = Depends(get_db)):    
    tag = db.exec(select(Tags).where(Tags.tagId == tag_id)).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    for field, value in updated_tag.dict().items():
        setattr(tag, field, value)
    tag.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(tag)
    return tag

@router.delete("/{tag_id}")
def delete_tag(tag_id: int,db: SQLModelSession = Depends(get_db)):
    tag = db.exec(select(Tags).where(Tags.tagId == tag_id)).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return {"message": "Tag deleted successfully"}