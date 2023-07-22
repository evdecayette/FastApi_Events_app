import urllib
from sqlmodel import SQLModel, create_engine
from sqlmodel import Session as SQLModelSession
server_name = "DECA\\SQLEXPRESS"
database_name = "Event_db"

# Escape special characters in the connection URL
escaped_server_name = urllib.parse.quote_plus(server_name)
escaped_database_name = urllib.parse.quote_plus(database_name)

# Construct the connection URL
connection_url = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={escaped_server_name};DATABASE={escaped_database_name};Trusted_Connection=yes;')}"

engine = create_engine(connection_url, echo=True)


def get_db() -> SQLModelSession:
    with SQLModelSession(engine) as session:
        yield session

def create_tables():
    SQLModel.metadata.create_all(engine)


