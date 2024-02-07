from services.user import create_user, get_all_users, get_user_by_id, delete_user, update_user

def register_user(data):
    return create_user(**data)

def fetch_users():
    return get_all_users()

def fetch_user(id):
    return get_user_by_id(id)

def delete_account(id):
    return delete_user(id)

def update_profile(id, data):
    return update_user(id, **data)