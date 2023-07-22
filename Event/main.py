from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_tables, engine
# from sqlmodel import Session
from .routers import event,user,tag,like,authentication
# session = Session (bind=engine)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(event.router)
app.include_router(tag.router)
app.include_router(like.router)

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)