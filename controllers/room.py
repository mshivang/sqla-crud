from services.room import create_room, get_all_rooms, get_room_by_id, delete_room, update_room

def room_to_dict(room):
    return {
        "id": room.id,
        "name": room.name,
        "created_by": room.created_by,
    }

def register_room(data):
    new_room = create_room(**data)
    return room_to_dict(new_room)

def fetch_rooms():
    rooms = get_all_rooms()
    return [room_to_dict(room) for room in rooms]

def fetch_room(id):
    room = get_room_by_id(id)
    return room_to_dict(room) if room else None

def _delete_room(id):
    deleted_room = delete_room(id)
    return room_to_dict(deleted_room) if deleted_room else None

def _update_room(id, data):
    updated_room = update_room(id, **data)
    return room_to_dict(updated_room) if updated_room else None
