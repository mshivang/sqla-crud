from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from typing import Dict

router = APIRouter()

rooms: Dict[str, set[WebSocket]] = {}

class ConnectionManager:
    def __init__(self):
        self.active_connections: set[WebSocket] = set()

    async def connect(self, websocket: WebSocket, room_id: int):
        await websocket.accept()
        self.active_connections.add(websocket)
        if room_id not in rooms:
            rooms[room_id] = set()
        rooms[room_id].add(websocket)
        print(f"Client connected to Room {room_id}: {websocket}")

    def disconnect(self, websocket: WebSocket, room_id: int):
        self.active_connections.remove(websocket)
        rooms[room_id].remove(websocket)
        print(f"Client disconnected from Room {room_id}: {websocket}")

    async def send_message(self, message, room_id: int):
        recipients = rooms.get(room_id, set())
        for connection in recipients:
            await connection.send_json(message)

    async def broadcast(self, message: str, room_id: int):
        for connection in rooms.get(room_id, []):
            await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws/{room_id}/{client_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, client_id: int):
    await manager.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.send_message(data, room_id)
            # await manager.broadcast(f"Client #{client_id} in Room #{room_id} says: {data}", room_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, room_id)
        await manager.broadcast(f"Client #{client_id} in Room #{room_id} left the chat", room_id)
