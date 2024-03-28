#!/usr/bin/python3
"""
    ALLOWS OPERATIONS FOR FRONT END DEVS
    THIS FILE WILL BRIDGE OUR CLASSES AND FLASK

"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import User, Service
from base_model import BaseModel, Base

class DBOperations():

    classes_dict = {'User': User, 'Service': Service}
    
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:9150@localhost/postgres')    

    def new(self, front_data):
        """
            Add new obj to database

            get():
                retrieves the value associated with the model_name key from the self.classes_dict dictionary.
                If model_name is found in the dictionary, model_class will be assigned the corresponding value
        """
        if front_data is None:
            return None

        print(front_data)
        dict = {}
        # Extract the model name from the received data
        model_name = list(front_data.keys())[0]  # model_name = "User"

        # Extract the inner dictionary containing attribute-value
        inner_dict = front_data[model_name] # inner_dict = {"first_name": "Louis", "last_name": "Toro"}

        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Get the model class corresponding to the model name
        model_class = self.classes_dict.get(model_name) # model_class = User

        if model_class:
            # Iterate over the attribute-value in the inner dictionary
            for key, value in inner_dict.items():

                # Add each attribute-value pair to the dictionary
                dict[key] = value # dict = {"first_name": "Louis", "last_name": "Toro"}

            # Create a new object of the model class using the attribute-value
            new_object = model_class(**dict) # new_object = User(first_name="Louis", last_name="Toro")
            
            # Add the new object to the session
            session.add(new_object)
            # Commit changes
            session.commit()
            session.close()
            return new_object
        else:
            print("Not a valid class")
            session.close()
            return None

    # def new(front_data):
    #     """Add new obj to database"""
    #     if front_data is None:
    #         print("No data received")
    #     else:
    #         # Check if first key from front_data is a class available     {'User': {first_name: Ant, last_name: De Jesus}}
    #         dict = {}
    #         inner_dict = front_data['user']
    #         for key, value in inner_dict.items():
    #             dict[key] = value
    #             # if key in self.classes_dict:
                    
    #             #     new_object = self.classes_dict[key](**value)
    #             #     print("Object wass added")
    #             #     print(new_object)
    #             break
    #         else:
    #             print("Not valid class")
    #     print(dict)
    #     return User(**dict)

    def filter (self, model_name, **kwargs):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            # Retrieve the model class from the classes_dict based on the model_name
            model_class = self.classes_dict[model_name]
        except KeyError:
            # If the model_name is not found in the classes_dict, close the session and return None
            session.close()
            return None
        # Create a new query object for the specified model_class
        query = session.query(model_class)

        # Iterate over the key-value pairs in the kwargs dictionary
        for key, value in kwargs.items():
            # Attempt to retrieve the column attribute from the model_class using the key
            column = getattr(model_class, key, None)
            if column is not None:
                # If a valid column is found, apply the filtering condition to the query
                query = query.filter(getattr(model_class, key) == value)

        # Execute the query and retrieve all the filtered objects
        filtered_objs = query.all()
        # Serialize the filtered objects by calling the all_columns method on each object
        serialized_objs = [obj.all_columns() for obj in filtered_objs]

        session.close()
        # Return the list of serialized objects
        return serialized_objs