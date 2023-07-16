from datetime import datetime, date
from sqlmodel import SQLModel, Field

# Define the User table
class UserBase(SQLModel):
    userId: int
    admin: bool
    created_at: datetime
    email: str
    profile: str
    updated_at: datetime
    username: str
    password: str

class Users(UserBase, table=True):
    userId : int = Field(default=None,primary_key=True)
    admin:bool = Field(sa_column="admin")
    created_at : date = Field(sa_column="created_at")
    email :str = Field(sa_column="email")
    profile :str = Field(sa_column="profile")
    updated_at : datetime =Field(sa_column="start_date")
    username: str = Field(sa_column="username")
    password : str = Field(sa_column="password")

# Define the Event table
class EventBase(SQLModel):
    eventId: int
    created_at: datetime
    description: str
    end_date: datetime
    location: str
    image: str
    start_date: datetime
    title: str
    updated_at: datetime
    userId: int

class Events(EventBase, table=True):
    eventId : int = Field(default=None,primary_key=True)
    created_at:date = Field(sa_column="create_at")
    description : str = Field(sa_column="description")
    end_date : date = Field(sa_column="end_date")
    location :str = Field(sa_column="location")
    image: str = Field(sa_column="image")
    start_date : date =Field(sa_column="start_date")
    title: str = Field(sa_column="title")
    updated_at : datetime = Field(sa_column="update_at")
    userId: int = Field(sa_column="userId", foreign_key="users.userId")

# Define the Tag table
class TagBase(SQLModel):
    tagId: int
    created_at: datetime
    eventId: int
    name: str
    updated_at: datetime

class Tags(TagBase, table=True):
    tagId : int = Field(default=None,primary_key=True)
    created_at:date = Field(sa_column="create_at")
    name : str = Field(sa_column="name")
    updated_at:date = Field(sa_column="update_at")
    eventId: int = Field(sa_column="eventId", foreign_key="events.eventId")

# Define the Like table
class LikeBase(SQLModel):
    likeId: int
    created_at: datetime
    eventId: int
    userId: int
    vote_type: str

class Likes(LikeBase, table=True):
    likeId : int = Field(default=None,primary_key=True)
    created_at:date = Field(sa_column="create_at")
    userId: int = Field(sa_column="userId", foreign_key="users.userId")
    eventId: int = Field(sa_column="eventId", foreign_key="events.eventId")
    vote_type : str = Field(sa_column="vote_type")
