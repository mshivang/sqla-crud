from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect
from routes import message, rooms, socket
from dependencies import get_db
from database import init_db
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database
    init_db()
    yield
    # Clean up 

# Initializing fast api app.
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Routers
app.include_router(message.router, dependencies=[Depends(get_db)])
app.include_router(rooms.router, dependencies=[Depends(get_db)])
app.include_router(socket.router)