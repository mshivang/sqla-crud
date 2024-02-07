from models.user import User
from sqlalchemy.orm import Session
from database import get_session
from fastapi import Depends

# Create a user in database.
def create_user(db: Session = Depends(get_session), **user_data):
    try:
        new_user = User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    # Rollback the db in case of an error
    except Exception as e:
        db.rollback()  
        raise e
    
    # Close the db to release resources
    finally:
        db.close()

# Get all users from database.
def get_all_users(db: Session = Depends(get_session)):
    try:
        users = db.query(User).all()
        return users
    
    except Exception as e:
        raise e
    
    finally:
        db.close()

# Get a particular user by id.
def get_user_by_id(user_id, db: Session = Depends(get_session)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        return user
    
    except Exception as e:
        raise e
    
    finally:
        db.close()

# Updates a particular user by id.
def update_user(user_id, db: Session = Depends(get_session), **update_data):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in update_data.items():
                setattr(user, key, value)
            db.commit()
            db.refresh(user)
            return user
        else:
            return None
    
    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()

# Deletes a particular user by id.
def delete_user(user_id, db: Session = Depends(get_session)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return user
        else:
            return None
    
    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()
