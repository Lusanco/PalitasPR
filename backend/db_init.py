# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

db_url = 'postgresql://demo_dev:demo_dev_pwd@demodb.ctossyay6vcz.us-east-2.rds.amazonaws.com/postgres'

engine = create_engine(
    db_url,
    pool_size=20,
    max_overflow=10, 
    pool_timeout=30, 
    pool_recycle=1800, 
    pool_pre_ping=True
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