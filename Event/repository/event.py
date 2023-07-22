from ..models import Events
from sqlmodel import Session,select
from fastapi import HTTPException
from datetime import datetime

def get_all(db:Session):
    events = db.exec(select(Events)).all()
    return events

def get_an_event(event_id:int, db:Session):
    # event = db.exec(Events).filter(Events.eventId == event_id).first()
    event =db.exec(select(Events).where(Events.eventId == event_id)).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

def create(event:Events,db:Session):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def update(db:Session, event_id, updated_event:Events):
    event = db.exec(select(Events).where(Events.eventId == event_id)).first()
    event.updated_at = datetime.utcnow()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    for field, value in updated_event.dict().items():
        setattr(event, field, value)
    db.commit()
    db.refresh(event)
    return event

def destroy(db:Session, event_id:int):
    event = db.exec(select(Events).where(Events.eventId == event_id)).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}