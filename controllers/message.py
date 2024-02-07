from services.message import create_message, get_all_messages, get_message_by_id, delete_message, update_message

def message_to_dict(message):
    return {
        "id": message.id,
        "text": message.text,
        "room_id": message.room_id,
        "created_by": message.created_by,
    }

def register_message(data):
    new_message = create_message(**data)
    return message_to_dict(new_message)

def fetch_messages():
    messages = get_all_messages()
    return [message_to_dict(message) for message in messages]

def fetch_message(id):
    message = get_message_by_id(id)
    return message_to_dict(message) if message else None

def _delete_message(id):
    deleted_message = delete_message(id)
    return message_to_dict(deleted_message) if deleted_message else None

def _update_message(id, data):
    updated_message = update_message(id, **data)
    return message_to_dict(updated_message) if updated_message else None
