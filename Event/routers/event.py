from fastapi import APIRouter, Depends,HTTPException
from typing import List
from ..models import Events, ShowEvent, Users
from Event import database
from sqlmodel import Session as SQLModelSession,select
from datetime import datetime
from ..repository import event
from .. import oauth2
get_db = database.get_db

router = APIRouter(
    prefix="/event",
    tags=["Event"]
)

@router.get("/", response_model=List[Events])
def get_Events(db: SQLModelSession = Depends(get_db),current_user:Users = Depends(oauth2.get_current_user)):
    return event.get_all(db)

@router.get("/{event_id}", response_model=ShowEvent)
def get_event(event_id: int, db: SQLModelSession = Depends(get_db),current_user:Users = Depends(oauth2.get_current_user)):
    return event.get_an_event(event_id,db)


@router.post("/",response_model=ShowEvent)
def create_event(an_event: Events,db: SQLModelSession = Depends(get_db),current_user:Users = Depends(oauth2.get_current_user)):
    return event.create(an_event,db)


@router.put("/{event_id}", response_model=Events)
def update_event(event_id: int, updated_event: Events,db: SQLModelSession = Depends(get_db),current_user:Users = Depends(oauth2.get_current_user)):
    return event.update(event_id, db,update_event)


@router.delete("/{event_id}")
def delete_event(event_id: int,db: SQLModelSession = Depends(get_db),current_user:Users = Depends(oauth2.get_current_user)):
    return event.destroy(event_id,db)