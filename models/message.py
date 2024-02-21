from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.room import Room

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    text = Column(String(500), unique=False)
    room_id = Column(Integer, ForeignKey(Room.id)) 
    created_by = Column(Integer, unique=False) 

    # relationships
    room = relationship('Room', backref='messages')

    def __init__(self, text=None, room_id=None, created_by=None):
        self.text = text
        self.created_by = created_by  
        self.room_id = room_id
        
    def __repr__(self):
        return f'<Room {self.text!r}>'
