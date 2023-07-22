# from fastapi import FastAPI,status, Depends, HTTPException
# from typing import Optional, List
# from fastapi.middleware.cors import CORSMiddleware
# from Event.models import Users, Events, Tags, Likes, ShowUser,ShowEvent, UserBase, EventBase, TagBase, LikeBase
# from Event.database import create_tables, engine
# from sqlmodel import Session
# from sqlmodel import Session as SQLModelSession,select
# from datetime import datetime, date
# from fastapi.responses import JSONResponse
# from Event.hashing import Hash
# session = Session (bind=engine)

# app = FastAPI()

# # def get_session() -> Session:
# #     session = Session()
# #     try:
# #         yield session
# #     finally:
# #         session.close()

# def get_db() -> SQLModelSession:
#     with SQLModelSession(engine) as session:
#         yield session

# # CORS configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# @app.on_event("startup")
# def startup():
#     create_tables()

# #+++++++++++++++++++++++++++++++++++++++ Users Routes ++++++++++++++++++++++++++++++++++++++++++

# # User routes
# @app.get("/users", response_model=List[ShowUser],tags=['users'])
# def get_users(db: SQLModelSession = Depends(get_db)):
#     with SQLModelSession(engine) as session:
#         users = db.exec(select(Users)).all()
#         return users

# @app.get("/users/{user_id}", response_model=ShowUser,tags=['users'])
# def get_user(user_id: int, db: SQLModelSession = Depends(get_db)):
#     user = db.query(Users).filter(Users.userId == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# @app.post("/users", response_model=ShowUser,tags=['users'])
# def create_user(user: Users,db: SQLModelSession = Depends(get_db)):
#     user.password = Hash.encrypt(user.password)
#     user.updated_at = datetime.now()
#     current_date = datetime.now()
#     user.created_at = current_date.strftime("%Y-%m-%d")
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# @app.put("/users/{user_id}", response_model=Users, tags=['users'])
# def update_user(user_id: int, updated_user: Users,db: SQLModelSession = Depends(get_db)):
#     user = db.exec(select(Users).where(Users.userId == user_id)).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     for field, value in updated_user.dict().items():
#         setattr(user, field, value)
#     user.updated_at = datetime.utcnow()
#     db.commit()
#     db.refresh(user)
#     return user

# @app.delete("/users/{user_id}", tags=['users'])
# def delete_user(user_id: int,db: SQLModelSession = Depends(get_db)):
#     user = session.exec(select(Users).where(Users.userId == user_id)).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     db.delete(user)
#     db.commit()
#     return {"message": "User deleted successfully"}


# #+++++++++++++++++++++++++++++++++++++++++ Event Routes +++++++++++++++++++++++++++++++++++++++++++++++++


# # Events routes
# @app.get("/events", response_model=List[Events],tags=['events'])
# def get_Events(db: SQLModelSession = Depends(get_db)):
#     with SQLModelSession(engine) as session:
#         events = db.exec(select(Events)).all()
#         return events

# @app.get("/events/{event_id}", response_model=ShowEvent,tags=['events'])
# def get_event(event_id: int, db: SQLModelSession = Depends(get_db)):
#     event = db.query(Events).filter(Events.eventId == event_id).first()
#     if not event:
#         raise HTTPException(status_code=404, detail="Event not found")
#     return event

# # Retrive all events created by a specific user
# @app.get("/events/user/{user_id}", response_model=List[ShowEvent],tags=["events"])
# def get_events_by_user(user_id: int,db: SQLModelSession = Depends(get_db)):
#     # Query the database to retrieve all events created by the specified user
#     events = db.query(Events).filter(Events.userId == user_id).all()
    
#     if not events:
#         raise HTTPException(status_code=404, detail="Events not found for the specified user")
    
#     return events


# @app.post("/events",response_model=ShowEvent,tags=['events'])
# def create_event(event: Events,db: SQLModelSession = Depends(get_db)):
#     db.add(event)
#     db.commit()
#     db.refresh(event)
#     return event

# @app.put("/events/{event_id}", response_model=Events,tags=['events'])
# def update_event(event_id: int, updated_event: Events):
#     with SQLModelSession(engine) as session:
#         event = session.exec(select(Events).where(Events.eventId == event_id)).first()
#         if not event:
#             raise HTTPException(status_code=404, detail="Event not found")
#         for field, value in updated_event.dict().items():
#             setattr(event, field, value)
#         event.updated_at = datetime.utcnow()
#         session.commit()
#         session.refresh(event)
#         return event

# @app.delete("/events/{event_id}",tags=['events'])
# def delete_event(event_id: int):
#     with SQLModelSession(engine) as session:
#         event = session.exec(select(Events).where(Events.eventId == event_id)).first()
#         if not event:
#             raise HTTPException(status_code=404, detail="Event not found")
#         session.delete(event)
#         session.commit()
#         return {"message": "Event deleted successfully"}

# #+++++++++++++++++++++++++++++++++++++++++ Tags Routes +++++++++++++++++++++++++++++++++++++++++++++++++

# # Tags routes
# @app.get("/tags", response_model=List[Tags],tags=['tags'])
# def get_tags():
#     with SQLModelSession(engine) as session:
#         tags = session.exec(select(Tags)).all()
#         return tags

# @app.get("/tags/{tag_id}", response_model=Tags,tags=['tags'])
# def get_tag(tag_id: int):
#     with SQLModelSession(engine) as session:
#         tag = session.exec(select(Tags).where(Tags.tagId == tag_id)).first()
#         if not tag:
#             raise HTTPException(status_code=404, detail="Tag not found")
#         return tag

# @app.post("/tags", response_model=Tags, tags=['tags'])
# def create_tag(tag: Tags):
#     with SQLModelSession(engine) as session:
#         session.add(tag)
#         session.commit()
#         session.refresh(tag)
#         return tag

# @app.put("/tags/{tag_id}", response_model=Tags,tags=['tags'])
# def update_tag(tag_id: int, updated_tag: Tags):
#     with SQLModelSession(engine) as session:
#         tag = session.exec(select(Tags).where(Tags.tagId == tag_id)).first()
#         if not tag:
#             raise HTTPException(status_code=404, detail="Tag not found")
#         for field, value in updated_tag.dict().items():
#             setattr(tag, field, value)
#         tag.updated_at = datetime.utcnow()
#         session.commit()
#         session.refresh(tag)
#         return tag

# @app.delete("/tags/{tag_id}",tags=['tags'])
# def delete_tag(tag_id: int):
#     with SQLModelSession(engine) as session:
#         tag = session.exec(select(Tags).where(Tags.tagId == tag_id)).first()
#         if not tag:
#             raise HTTPException(status_code=404, detail="Tag not found")
#         session.delete(tag)
#         session.commit()
#         return {"message": "Tag deleted successfully"}

# #+++++++++++++++++++++++++++++++++++++++++ Likes Routes +++++++++++++++++++++++++++++++++++++++++++++++++

# # Likes routes
# @app.get("/likes", response_model=List[Likes],tags=['likes'])
# def get_likes():
#     with SQLModelSession(engine) as session:
#         likes = session.exec(select(Likes)).all()
#         return likes

# @app.get("/tags/{like_id}", response_model=Likes,tags=['likes'])
# def get_tag(like_id: int):
#     with SQLModelSession(engine) as session:
#         like = session.exec(select(Likes).where(Likes.likeId == like_id)).first()
#         if not like:
#             raise HTTPException(status_code=404, detail="Like not found")
#         return like

# @app.post("/likes", response_model=Likes,tags=['likes'])
# def create_like(like: Likes):
#     with SQLModelSession(engine) as session:
#         session.add(like)
#         session.commit()
#         session.refresh(like)
#         return like

# @app.put("/tags/{like_id}", response_model=Likes,tags=['likes'])
# def update_like(like_id: int, updated_like: Likes):
#     with SQLModelSession(engine) as session:
#         like = session.exec(select(Likes).where(Likes.likeId == like_id)).first()
#         if not like:
#             raise HTTPException(status_code=404, detail="Like not found")
#         for field, value in updated_like.dict().items():
#             setattr(like, field, value)
#         like.created_at = datetime.utcnow()
#         session.commit()
#         session.refresh(like)
#         return like

# @app.delete("/likes/{like_id}",tags=['likes'])
# def delete_like(like_id: int):
#     with SQLModelSession(engine) as session:
#         like = session.exec(select(Likes).where(Likes.likeId == like_id)).first()
#         if not like:
#             raise HTTPException(status_code=404, detail="Like not found")
#         session.delete(like)
#         session.commit()
#         return {"message": "Like deleted successfully"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)