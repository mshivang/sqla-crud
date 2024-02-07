from models.message import Message
from sqlalchemy.orm import Session
from database import get_session
from fastapi import Depends

# Create a message in database.
def create_message(db: Session = Depends(get_session), **message_data):
    try:
        new_message = Message(**message_data)
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return new_message
    
    # Rollback the db in case of an error
    except Exception as e:
        db.rollback()  
        raise e
    
    # Close the db to release resources
    finally:
        db.close()

# Get all messages from database.
def get_all_messages(db: Session = Depends(get_session)):
    try:
        messages = db.query(Message).all()
        return messages
    
    except Exception as e:
        raise e
    
    finally:
        db.close()

# Get a particular message by id.
def get_message_by_id(message_id, db: Session = Depends(get_session)):
    try:
        message = db.query(Message).filter(Message.id == message_id).first()
        return message
    
    except Exception as e:
        raise e
    
    finally:
        db.close()

# Updates a particular message by id.
def update_message(message_id, db: Session = Depends(get_session), **update_data):
    try:
        message = db.query(Message).filter(Message.id == message_id).first()
        if message:
            for key, value in update_data.items():
                setattr(message, key, value)
            db.commit()
            db.refresh(message)
            return message
        else:
            return None
    
    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()

# Deletes a particular message by id.
def delete_message(message_id, db: Session = Depends(get_session)):
    try:
        message = db.query(Message).filter(Message.id == message_id).first()
        if message:
            db.delete(message)
            db.commit()
            return message
        else:
            return None
    
    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()
