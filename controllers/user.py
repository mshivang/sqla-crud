from services.user import create_user, get_all_users, get_user_by_id, delete_user, update_user

def user_to_dict(user):
    return {
        "id": user.id,
        "email": user.email,
        "fname": user.fname,
        "lname": user.lname,
    }

def register_user(data):
    new_user = create_user(**data)
    return user_to_dict(new_user)

def fetch_users():
    users = get_all_users()
    return [user_to_dict(user) for user in users]

def fetch_user(id):
    user = get_user_by_id(id)
    return user_to_dict(user) if user else None

def _delete_user(id):
    deleted_user = delete_user(id)
    return user_to_dict(deleted_user) if deleted_user else None

def _update_user(id, data):
    updated_user = update_user(id, **data)
    return user_to_dict(updated_user) if updated_user else None