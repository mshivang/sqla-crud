from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=False)
    created_by = Column(Integer, unique=False) 

    def __init__(self, name=None, created_by=None):
        self.name = name
        self.created_by = created_by  

    def __repr__(self):
        return f'<Room {self.name!r}>'
