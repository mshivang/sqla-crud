from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from .env.local only in development mode
if os.environ.get('FAST_API_ENV') == 'development':
    env_file = Path(__file__).resolve().parent / '.env.local'
else:
    env_file = Path(__file__).resolve().parent / '.env'

load_dotenv(env_file)

url = URL.create(
    drivername = os.environ.get('DB_DIRVER_NAME'),
    username = os.environ.get('DB_USERNAME'),
    password = os.environ.get('DB_PASSWORD'),
    host = os.environ.get('DB_HOST'),
    database = os.environ.get('DB_DATABASE'),
    port = os.environ.get('DB_PORT')
)

engine = create_engine(url)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = session.query_property()

def init_db():
    # Creating tables.
    import models
    Base.metadata.create_all(bind=engine)

     # Run Alembic migrations
    from alembic.config import Config
    from alembic import command

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head", sql=False, tag=None)
