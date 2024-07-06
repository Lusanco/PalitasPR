# db.py
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
import os

load_dotenv()
db_url = os.getenv("DB_URL")

engine = create_engine(
    db_url,
    pool_size=30,
    max_overflow=15,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

from base_model import Base

Base.metadata.bind = engine


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
    finally:
        session.close()


def init_db():
    with session_scope() as session:
        Base.metadata.create_all(session.get_bind())


def get_session():
    with session_scope() as session:
        return session
