#!/usr/bin/python3
# backend/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base_model import Base

# Create the engine
engine = create_engine('postgresql://postgres:9150@localhost/postgres')

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create session maker
Session = sessionmaker(bind=engine)
