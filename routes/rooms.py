from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from controllers.room import fetch_rooms, fetch_room, register_room, _update_room, _delete_room

router = APIRouter()

# Route to get all rooms
@router.get("/rooms/", tags=["rooms"])
async def read_rooms():
    try:
        rooms = fetch_rooms()
        return JSONResponse(content={"rooms": rooms, "status": "success"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to add a new room
@router.post("/rooms/", tags=["rooms"])
async def add_room(data: dict):
    try:
        registered_room = register_room(data)
        return JSONResponse(content={"room": registered_room, "status": "success"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to get a room by ID
@router.get("/rooms/{id}", tags=["rooms"])
async def read_room(id: int):
    try:
        room = fetch_room(id)
        if room:
            return JSONResponse(content={"room": room, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Room not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to update a room by ID
@router.patch("/rooms/{id}", tags=["rooms"])
async def update_room_endpoint(id: int, data: dict):
    try:
        updated_room = _update_room(id, data)
        if updated_room:
            return JSONResponse(content={"room": updated_room, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Room not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to delete a room by ID
@router.delete("/rooms/{id}", tags=["rooms"])
async def delete_room_endpoint(id: int):
    try:
        deleted_room = _delete_room(id)
        if deleted_room:
            return JSONResponse(content={"room": deleted_room, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Room not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
