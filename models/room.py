from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.user import User

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=False)
    created_by = Column(Integer, ForeignKey(User.id)) 

    # relationships
    host = relationship('User', backref='rooms')

    def __init__(self, name=None, created_by=None):
        self.name = name
        self.created_by = created_by  

    def __repr__(self):
        return f'<Room {self.name!r}>'
