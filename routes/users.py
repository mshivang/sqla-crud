from fastapi import APIRouter, HTTPException
from controllers.user import fetch_users, fetch_user, register_user, update_profile, delete_user

router = APIRouter()

# Route to get all users
@router.get("/users/", tags=["users"])
async def read_users():
    try:
        users = fetch_users()
        return {"users": users, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to add a new user
@router.post("/users/", tags=["users"])
async def add_user(data: dict):
    try:
        registered_user = register_user(data)
        return {"user": registered_user, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to get a user by ID
@router.get("/users/{id}", tags=["users"])
async def read_user(id: int):
    try:
        user = fetch_user(id)
        if user:
            return {"user": user, "status": "success"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to update a user by ID
@router.patch("/users/{id}", tags=["users"])
async def update_user_endpoint(id: int, data: dict):
    try:
        updated_user = update_profile(id, data)
        if updated_user:
            return {"user": updated_user, "status": "success"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to delete a user by ID
@router.delete("/users/{id}", tags=["users"])
async def delete_user_endpoint(id: int):
    try:
        deleted_user = delete_user(id)
        if deleted_user:
            return {"user": deleted_user, "status": "success"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Route to get the current user (dummy data)
@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser", "status": "success"}