# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

db_url = 'postgresql://demo_dev:demo_dev_pwd@demodb.ctossyay6vcz.us-east-2.rds.amazonaws.com/postgres'

engine = create_engine(db_url)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

from base_model import Base
Base.metadata.bind = engine

def init_db():
    Base.metadata.create_all(engine)
