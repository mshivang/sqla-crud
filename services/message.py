from models.message import Message
from database import session

# Create a message in database.
def create_message(**message_data):
    try:
        new_message = Message(**message_data)
        session.add(new_message)
        session.commit()
        session.refresh(new_message)
        return new_message
    
    # Rollback the session in case of an error
    except Exception as e:
        session.rollback()  
        raise e
    
    # Close the session to release resources
    finally:
        session.close()

# Get all messages from database.
def get_all_messages():
    try:
        messages = session.query(Message).all()
        return messages
    
    except Exception as e:
        raise e
    
    finally:
        session.close()

# Get a particular message by id.
def get_message_by_id(message_id):
    try:
        message = session.query(Message).filter(Message.id == message_id).first()
        return message
    
    except Exception as e:
        raise e
    
    finally:
        session.close()

# Updates a particular message by id.
def update_message(message_id, **update_data):
    try:
        message = session.query(Message).filter(Message.id == message_id).first()
        if message:
            for key, value in update_data.items():
                setattr(message, key, value)
            session.commit()
            session.refresh(message)
            return message
        else:
            return None
    
    except Exception as e:
        session.rollback()
        raise e
    
    finally:
        session.close()

# Deletes a particular message by id.
def delete_message(message_id):
    try:
        message = session.query(Message).filter(Message.id == message_id).first()
        if message:
            session.delete(message)
            session.commit()
            return message
        else:
            return None
    
    except Exception as e:
        session.rollback()
        raise e
    
    finally:
        session.close()
