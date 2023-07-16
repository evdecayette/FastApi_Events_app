from fastapi import FastAPI,status, Depends, HTTPException
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from models import Users, Events, Tags, Likes, UserBase, EventBase, TagBase, LikeBase
from database import create_tables, engine
from sqlmodel import Session, select
from datetime import datetime
from fastapi.responses import JSONResponse

session = Session (bind=engine)

app = FastAPI()

def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
def startup():
    create_tables()

#+++++++++++++++++++++++++++++++++++++++ Users Routes ++++++++++++++++++++++++++++++++++++++++++

# User routes
@app.get("/users", response_model=List[Users])
def get_users():
    with Session(engine) as session:
        users = session.exec(select(Users)).all()
        return users

@app.get("/users/{user_id}", response_model=Users)
def get_user(user_id: int):
    with Session(engine) as session:
        user = session.exec(select(Users).where(Users.userId == user_id)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

@app.post("/users", response_model=Users)
def create_user(user: Users):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

@app.put("/users/{user_id}", response_model=Users)
def update_user(user_id: int, updated_user: Users):
    with Session(engine) as session:
        user = session.exec(select(Users).where(Users.userId == user_id)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        for field, value in updated_user.dict().items():
            setattr(user, field, value)
        user.updated_at = datetime.utcnow()
        session.commit()
        session.refresh(user)
        return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.exec(select(Users).where(Users.userId == user_id)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully"}


#+++++++++++++++++++++++++++++++++++++++++ Event Routes +++++++++++++++++++++++++++++++++++++++++++++++++


# User routes
@app.get("/events", response_model=List[Events])
def get_Events():
    with Session(engine) as session:
        events = session.exec(select(Events)).all()
        return events

@app.get("/events/{event_id}", response_model=Events)
def get_event(event_id: int):
    with Session(engine) as session:
        event = session.exec(select(Events).where(Events.eventId == event_id)).first()
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event

@app.post("/events", response_model=Events)
def create_event(event: Events):
    with Session(engine) as session:
        session.add(event)
        session.commit()
        session.refresh(event)
        return event

@app.put("/events/{event_id}", response_model=Events)
def update_event(event_id: int, updated_event: Events):
    with Session(engine) as session:
        event = session.exec(select(Events).where(Events.eventId == event_id)).first()
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        for field, value in updated_event.dict().items():
            setattr(event, field, value)
        event.updated_at = datetime.utcnow()
        session.commit()
        session.refresh(event)
        return event

@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    with Session(engine) as session:
        event = session.exec(select(Events).where(Events.eventId == event_id)).first()
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        session.delete(event)
        session.commit()
        return {"message": "Event deleted successfully"}

#+++++++++++++++++++++++++++++++++++++++++ Tags Routes +++++++++++++++++++++++++++++++++++++++++++++++++

# Tags routes
@app.get("/tags", response_model=List[Tags])
def get_tags():
    with Session(engine) as session:
        tags = session.exec(select(Tags)).all()
        return tags

@app.get("/tags/{tag_id}", response_model=Tags)
def get_tag(tag_id: int):
    with Session(engine) as session:
        tag = session.exec(select(Tags).where(Tags.tagId == tag_id)).first()
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return tag

@app.post("/tags", response_model=Tags)
def create_tag(tag: Tags):
    with Session(engine) as session:
        session.add(tag)
        session.commit()
        session.refresh(tag)
        return tag

@app.put("/tags/{tag_id}", response_model=Tags)
def update_tag(tag_id: int, updated_tag: Tags):
    with Session(engine) as session:
        tag = session.exec(select(Tags).where(Tags.tagId == tag_id)).first()
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        for field, value in updated_tag.dict().items():
            setattr(tag, field, value)
        tag.updated_at = datetime.utcnow()
        session.commit()
        session.refresh(tag)
        return tag

@app.delete("/tags/{tag_id}")
def delete_tag(tag_id: int):
    with Session(engine) as session:
        tag = session.exec(select(Tags).where(Tags.tagId == tag_id)).first()
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        session.delete(tag)
        session.commit()
        return {"message": "Tag deleted successfully"}

#+++++++++++++++++++++++++++++++++++++++++ Likes Routes +++++++++++++++++++++++++++++++++++++++++++++++++

# Likes routes
@app.get("/likes", response_model=List[Likes])
def get_likes():
    with Session(engine) as session:
        likes = session.exec(select(Likes)).all()
        return likes

@app.get("/tags/{like_id}", response_model=Likes)
def get_tag(like_id: int):
    with Session(engine) as session:
        like = session.exec(select(Likes).where(Likes.likeId == like_id)).first()
        if not like:
            raise HTTPException(status_code=404, detail="Like not found")
        return like

@app.post("/likes", response_model=Likes)
def create_like(like: Likes):
    with Session(engine) as session:
        session.add(like)
        session.commit()
        session.refresh(like)
        return like

@app.put("/tags/{like_id}", response_model=Likes)
def update_like(like_id: int, updated_like: Likes):
    with Session(engine) as session:
        like = session.exec(select(Likes).where(Likes.likeId == like_id)).first()
        if not like:
            raise HTTPException(status_code=404, detail="Like not found")
        for field, value in updated_like.dict().items():
            setattr(like, field, value)
        like.created_at = datetime.utcnow()
        session.commit()
        session.refresh(like)
        return like

@app.delete("/likes/{like_id}")
def delete_like(like_id: int):
    with Session(engine) as session:
        like = session.exec(select(Likes).where(Likes.likeId == like_id)).first()
        if not like:
            raise HTTPException(status_code=404, detail="Like not found")
        session.delete(like)
        session.commit()
        return {"message": "Like deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)