from fastapi import FastAPI, Depends
from routes import users, message, rooms
from dependencies import get_db
from database import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database
    init_db()
    yield
    # Clean up 

# Initializing fast api app.
app = FastAPI(lifespan=lifespan)

#Routers
app.include_router(users.router, dependencies=[Depends(get_db)])
app.include_router(message.router, dependencies=[Depends(get_db)])
app.include_router(rooms.router, dependencies=[Depends(get_db)])