from models.user import User
from database import session

# Create a user in database.
def create_user(**user_data):
    try:
        new_user = User(**user_data)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    
    # Rollback the session in case of an error
    except Exception as e:
        session.rollback()  
        raise e
    
    # Close the session to release resources
    finally:
        session.close()

# Get all users from database.
def get_all_users():
    try:
        users = session.query(User).all()
        return users
    
    except Exception as e:
        raise e
    
    finally:
        session.close()

# Get a particular user by id.
def get_user_by_id(user_id):
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    
    except Exception as e:
        raise e
    
    finally:
        session.close()

# Updates a particular user by id.
def update_user(user_id, **update_data):
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in update_data.items():
                setattr(user, key, value)
            session.commit()
            session.refresh(user)
            return user
        else:
            return None
    
    except Exception as e:
        session.rollback()
        raise e
    
    finally:
        session.close()

# Deletes a particular user by id.
def delete_user(user_id):
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return user
        else:
            return None
    
    except Exception as e:
        session.rollback()
        raise e
    
    finally:
        session.close()
