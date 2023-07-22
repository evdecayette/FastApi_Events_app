from fastapi import APIRouter, Depends,HTTPException
from ..models import Login, Users
from Event import database, token
from sqlmodel import Session as SQLModelSession,select
from Event import hashing
from fastapi.security import OAuth2PasswordRequestForm

get_db = database.get_db

router = APIRouter(
    tags=["Login"]
)

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(),db: SQLModelSession = Depends(get_db)):
    user = db.exec(select(Users).where(Users.email == request.username)).first()
    if not user:
         raise HTTPException(status_code=404, detail="Incorrect email")    

    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail="Incorrect Password")    

    access_token = token.create_access_token( data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

