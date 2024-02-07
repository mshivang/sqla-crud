from services.room import create_room, get_all_rooms, get_room_by_id, delete_room, update_room
from sqlalchemy.orm import Session

def room_to_dict(room):
    return {
        "id": room.id,
        "name": room.name,
        "created_by": room.created_by,
    }

def register_room(data, db: Session):
    new_room = create_room(data, db)
    return room_to_dict(new_room)

def fetch_rooms(db: Session):
    rooms = get_all_rooms(db)
    return [room_to_dict(room) for room in rooms]

def fetch_room(id, db: Session):
    room = get_room_by_id(id, db)
    return room_to_dict(room) if room else None

def _delete_room(id, db: Session):
    deleted_room = delete_room(id, db)
    return room_to_dict(deleted_room) if deleted_room else None

def _update_room(id, data, db: Session):
    updated_room = update_room(id, data, db)
    return room_to_dict(updated_room) if updated_room else None
