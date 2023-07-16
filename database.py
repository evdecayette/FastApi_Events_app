import urllib, pyodbc
from sqlmodel import SQLModel, create_engine, Session
server_name = "DECA\\SQLEXPRESS"
database_name = "Event_db"

# Escape special characters in the connection URL
escaped_server_name = urllib.parse.quote_plus(server_name)
escaped_database_name = urllib.parse.quote_plus(database_name)

# Construct the connection URL
connection_url = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={escaped_server_name};DATABASE={escaped_database_name};Trusted_Connection=yes;')}"

engine = create_engine(connection_url, echo=True)

# SQLModel.metadata.create_all(engine)

# class Users(SQLModel, table=True):    
#     userId : int = Field(default=None,primary_key=True)
#     admin:bool = Field(sa_column="admin")
#     created_at : date = Field(sa_column="created_at")
#     email :str = Field(sa_column="email")
#     updated_at : datetime =Field(sa_column="start_date")
#     username: str = Field(sa_column="username")
#     profile: str = Field(sa_column="profile")
#     userPassword : datetime = Field(sa_column="userPassword")

# class Event(SQLModel, table=True):
    
#     eventId : int = Field(default=None,primary_key=True)
#     created_at:date = Field(sa_column="create_at")
#     description : str = Field(sa_column="description")
#     end_date : date = Field(sa_column="end_date")
#     location :str = Field(sa_column="location")
#     image: str = Field(sa_column="image")
#     start_date : date =Field(sa_column="start_date")
#     title: str = Field(sa_column="title")
#     updated_at : datetime = Field(sa_column="update_at")
#     userId: int = Field(sa_column="userId", foreign_key="users.userId")

# class Tags(SQLModel, table=True):   
#     TagId : int = Field(default=None,primary_key=True)
#     created_at:date = Field(sa_column="create_at")
#     name : str = Field(sa_column="name")
#     updated_at:date = Field(sa_column="update_at")
#     eventId: int = Field(sa_column="eventId", foreign_key="event.eventId")


# class Likes(SQLModel, table=True):   
#     LikeId : int = Field(default=None,primary_key=True)
#     created_at:date = Field(sa_column="create_at")
#     userId: int = Field(sa_column="userId", foreign_key="users.userId")
#     eventId: int = Field(sa_column="eventId", foreign_key="event.eventId")
#     vote_type : str = Field(sa_column="vote_type")


def create_tables():
    SQLModel.metadata.create_all(engine)


