from models.room import Room
from database import session

# Create a room in database.
def create_room(**room_data):
    try:
        new_room = Room(**room_data)
        session.add(new_room)
        session.commit()
        session.refresh(new_room)
        return new_room
    
    # Rollback the session in case of an error
    except Exception as e:
        session.rollback()  
        raise e
    
    # Close the session to release resources
    finally:
        session.close()

# Get all rooms from database.
def get_all_rooms():
    try:
        rooms = session.query(Room).all()
        return rooms
    
    except Exception as e:
        raise e
    
    finally:
        session.close()

# Get a particular room by id.
def get_room_by_id(room_id):
    try:
        room = session.query(Room).filter(Room.id == room_id).first()
        return room
    
    except Exception as e:
        raise e
    
    finally:
        session.close()

# Updates a particular room by id.
def update_room(room_id, **update_data):
    try:
        room = session.query(Room).filter(Room.id == room_id).first()
        if room:
            for key, value in update_data.items():
                setattr(room, key, value)
            session.commit()
            session.refresh(room)
            return room
        else:
            return None
    
    except Exception as e:
        session.rollback()
        raise e
    
    finally:
        session.close()

# Deletes a particular room by id.
def delete_room(room_id):
    try:
        room = session.query(Room).filter(Room.id == room_id).first()
        if room:
            session.delete(room)
            session.commit()
            return room
        else:
            return None
    
    except Exception as e:
        session.rollback()
        raise e
    
    finally:
        session.close()
