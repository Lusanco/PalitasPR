#!/usr/bin/python3
"""
    ALLOWS OPERATIONS FOR FRONT END DEVS
    THIS FILE WILL BRIDGE OUR CLASSES AND FLASK

"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.models import User, Service
from backend.base_model import BaseModel, Base
from . import Session

class DBoperations():

    classes_dict = {'User': User, 'Service': Service}
    
    def new(self, **front_data):
        """Add new obj to database"""
        if front_data is None:
            print("No data received")
        else:
            # Check if first key from front_data is a class available     {'User': {first_name: Ant, last_name: De Jesus}}
            for key, value in front_data.items():
                if key in self.classes_dict:
                    
                    new_object = self.classes_dict[key](**value)
                    print("Object wass added")
                    print(new_object)
                break
            else:
                print("Not valid class")
