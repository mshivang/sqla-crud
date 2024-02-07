from models.room import Room
from sqlalchemy.orm import Session
from dependencies import get_db
from fastapi import Depends

# Create a room in database.
def create_room(room_data, db: Session = Depends(get_db)):
    try:
        new_room = Room(**room_data)
        db.add(new_room)
        db.commit()
        db.refresh(new_room)
        return new_room
    
    # Rollback the db in case of an error
    except Exception as e:
        db.rollback()  
        raise e
    
    # Close the db to release resources
    finally:
        db.close()

# Get all rooms from database.
def get_all_rooms(db: Session = Depends(get_db)):
    try:
        rooms = db.query(Room).all()
        return rooms
    
    except Exception as e:
        raise e
    
    finally:
        db.close()

# Get a particular room by id.
def get_room_by_id(room_id, db: Session = Depends(get_db)):
    try:
        room = db.query(Room).filter(Room.id == room_id).first()
        return room
    
    except Exception as e:
        raise e
    
    finally:
        db.close()

# Updates a particular room by id.
def update_room(room_id, update_data, db: Session = Depends(get_db)):
    try:
        room = db.query(Room).filter(Room.id == room_id).first()
        if room:
            for key, value in update_data.items():
                setattr(room, key, value)
            db.commit()
            db.refresh(room)
            return room
        else:
            return None
    
    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()

# Deletes a particular room by id.
def delete_room(room_id, db: Session = Depends(get_db)):
    try:
        room = db.query(Room).filter(Room.id == room_id).first()
        if room:
            db.delete(room)
            db.commit()
            return room
        else:
            return None
    
    except Exception as e:
        db.rollback()
        raise e
    
    finally:
        db.close()
