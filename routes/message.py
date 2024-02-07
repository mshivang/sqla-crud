from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from controllers.message import fetch_messages, fetch_message, register_message, _update_message, _delete_message
from database import get_session

router = APIRouter()

# Route to get all messages
@router.get("/messages/", tags=["messages"])
async def read_messages(db: Session = Depends(get_session)):
    try:
        messages = fetch_messages(db)
        return JSONResponse(content={"messages": messages, "status": "success"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to add a new message
@router.post("/messages/", tags=["messages"])
async def add_message(data: dict, db: Session = Depends(get_session)):
    try:
        registered_message = register_message(data, db)
        return JSONResponse(content={"message": registered_message, "status": "success"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to get a message by ID
@router.get("/messages/{id}", tags=["messages"])
async def read_message(id: int, db: Session = Depends(get_session)):
    try:
        message = fetch_message(id, db)
        if message:
            return JSONResponse(content={"message": message, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Message not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to update a message by ID
@router.patch("/messages/{id}", tags=["messages"])
async def update_message_endpoint(id: int, data: dict, db: Session = Depends(get_session)):
    try:
        updated_message = _update_message(id, data, db)
        if updated_message:
            return JSONResponse(content={"message": updated_message, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Message not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to delete a message by ID
@router.delete("/messages/{id}", tags=["messages"])
async def delete_message_endpoint(id: int, db: Session = Depends(get_session)):
    try:
        deleted_message = _delete_message(id, db)
        if deleted_message:
            return JSONResponse(content={"message": deleted_message, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Message not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
