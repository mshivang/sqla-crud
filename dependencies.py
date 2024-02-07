from sqlalchemy.orm import Session
from database import session

def get_db() -> Session:
    try:
        yield session
    finally:
        session.close()