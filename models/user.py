from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(200))
    fname = Column(String(50))
    lname = Column(String(50))

    def __init__(self, fname=None, lname=None, password=None, email=None):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.name!r}>'