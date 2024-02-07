from sqlalchemy.orm import Session
from database import get_session

async def get_db() -> Session:
    db = get_session()
    try:
        yield db
    finally:
        db.close()