from services.user import create_user, get_all_users, get_user_by_id, delete_user, update_user
from sqlalchemy.orm import Session

def user_to_dict(user):
    return {
        "id": user.id,
        "email": user.email,
        "fname": user.fname,
        "lname": user.lname,
    }

def register_user(data, db: Session):
    new_user = create_user(data, db)
    return user_to_dict(new_user)

def fetch_users(db: Session):
    users = get_all_users(db)
    return [user_to_dict(user) for user in users]

def fetch_user(id, db: Session):
    user = get_user_by_id(id, db)
    return user_to_dict(user) if user else None

def _delete_user(id, db: Session):
    deleted_user = delete_user(id, db)
    return user_to_dict(deleted_user) if deleted_user else None

def _update_user(id, data, db: Session):
    updated_user = update_user(id, data, db)
    return user_to_dict(updated_user) if updated_user else None
