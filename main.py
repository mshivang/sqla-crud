from database import session, init_db
from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database
    init_db()
    yield
    # Clean up database session
    session.remove()

# Initializing fast api app.
app = FastAPI(lifespan=lifespan)

#Routers
app.include_router(users.router)
    