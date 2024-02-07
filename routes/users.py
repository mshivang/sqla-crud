from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from controllers.user import fetch_users, fetch_user, register_user, _update_user, _delete_user
from dependencies import get_db

router = APIRouter()

# Route to get all users
@router.get("/users/", tags=["users"])
async def read_users(db: Session = Depends(get_db)):
    try:
        users = fetch_users(db)
        return JSONResponse(content={"users": users, "status": "success"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to add a new user
@router.post("/users/", tags=["users"])
async def add_user(data: dict, db: Session = Depends(get_db)):
    try:
        registered_user = register_user(data, db)
        return JSONResponse(content={"user": registered_user, "status": "success"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to get a user by ID
@router.get("/users/{id}", tags=["users"])
async def read_user(id: int, db: Session = Depends(get_db)):
    try:
        user = fetch_user(id, db)
        if user:
            return JSONResponse(content={"user": user, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to update a user by ID
@router.patch("/users/{id}", tags=["users"])
async def update_user_endpoint(id: int, data: dict, db: Session = Depends(get_db)):
    try:
        updated_user = _update_user(id, data, db)
        if updated_user:
            return JSONResponse(content={"user": updated_user, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to delete a user by ID
@router.delete("/users/{id}", tags=["users"])
async def delete_user_endpoint(id: int, db: Session = Depends(get_db)):
    try:
        deleted_user = _delete_user(id, db)
        if deleted_user:
            return JSONResponse(content={"user": deleted_user, "status": "success"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to get the current user (dummy data)
@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser", "status": "success"}
