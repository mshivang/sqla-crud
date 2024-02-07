from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.user import User
from models.room import Room

class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True)
    text = Column(String(500), unique=False)
    room_id = Column(Integer, ForeignKey(Room.id)) 
    created_by = Column(Integer, ForeignKey(User.id)) 

    # relationships
    sent_by = relationship('User', backref='chats')
    room = relationship('Room', backref='chats')

    def __init__(self, name=None, created_by=None):
        self.name = name
        self.created_by = created_by  

    def __repr__(self):
        return f'<Room {self.name!r}>'
