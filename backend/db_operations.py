"""
    ALLOWS OPERATIONS FOR FRONT END DEVS
    THIS FILE WILL BRIDGE OUR CLASSES AND FLASK

"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import User, Service
from base_model import BaseModel, Base


class DBOperations:

    classes_dict = {"User": User, "Service": Service}

    def __init__(self):
        self.engine = create_engine("postgresql://alfre:1234@localhost/demo_data")

    def new(self, **front_data):
        """Add new obj to database"""
