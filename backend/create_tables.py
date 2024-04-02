#!/usr/bin/python3
"""
    MODIFY WITH YOUR DB, IM USING POSTGRE BUT YOU CAN USE...
    MYSQL, REMEMBER TO CHANGE VALUES IN CREATE ENGINE
    AFTER YOU CREATE YOUR DB YOU CAN RUN THIS
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_model import Base

# Create the engine
engine = create_engine('postgresql://postgres:9495@localhost/postgres')

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create all tables in the database
Base.metadata.create_all(engine)

# Optionally, you can add some initial data or perform other setup tasks here

# Close the session
engine.dispose()