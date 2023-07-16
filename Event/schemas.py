from datetime import datetime, date
# from pydantic import BaseModel
from typing import Optional
from sqlmodel import Field, SQLModel

# class Event(SQLModel, table=True):
#     create_at:date
#     description : str
#     end_date : date
#     eventId : int = Field(primary_key=True)
#     location :str
#     start_date : date
#     title: str
#     update_at : datetime
#     userId: int  