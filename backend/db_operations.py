#!/usr/bin/python3
"""
    ALLOWS OPERATIONS FOR FRONT END DEVS
    THIS FILE WILL BRIDGE OUR CLASSES AND FLASK

"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.relationships import RelationshipProperty
from models import User, Service, Town, UserServiceAssoc
from base_model import BaseModel, Base

class DBOperations():

    classes_dict = {'User': User, 'Service': Service, 'Town': Town, 'UserServiceAssoc': UserServiceAssoc}
    
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:9495@localhost/postgres')    

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
        inner_dict = front_data[model_name] # inner_dict = {"name": "Nails"}

        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Get the model class corresponding to the model name
        model_class = self.classes_dict.get(model_name) # model_class = User

        if model_class:
            # Iterate over the attribute-value in the inner dictionary
            for key, value in inner_dict.items():

                # Add each attribute-value to the dictionary
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




    def filter(self, data):
        """
        Retrieve objects based on specified criteria.

        Args:
            data: Dictionary containing the filtering criteria.
                example:
                    filtered_objs = db.filter({'User': {'name': 'Auto Body Painting'}})
                    in this case, it will show all the users that work on Auto body painting.

            There is a section to test the function after the delete method.
        """

        Session = sessionmaker(bind=self.engine)
        session = Session()

        result_dict = {}
        front_town = None
        front_name = None
        model_name = list(data.keys())[0]
        filter_values = data[model_name]

        model_class = self.classes_dict.get(model_name)

        if model_class:
            query = session.query(model_class)
            if 'town' in filter_values:
                front_town = filter_values.pop('town')
            if 'name' in filter_values:
                front_name = filter_values.pop('name')
            for key, value in filter_values.items():
                query = query.filter(getattr(model_class, key) == value)
            filtered_objs = query.all()

            Town = 'All'
            Name = 'All'
            if front_town:
                Town = front_town
            if front_name:
                Name = front_name
            for obj in filtered_objs:
                inner_dict = {}
                towns = []
                rows = obj.user_service_assoc
                if rows:
                    for row in rows:
                        service_name = row.service.name
                        if Town == row.town.name or Town == 'All' and Name == row.service.name or Name == 'All':
                            towns.append(row.town.name)
                            inner_dict['name'] = service_name
                            inner_dict['first_name'] = row.user.first_name
                            inner_dict['last_name'] = row.user.last_name
                            inner_dict['towns'] = towns
                            result_dict[obj.id] = inner_dict

        session.close()
        return result_dict






    def delete(self, model_name, user_id=None, **data):
        """
            Delete objects and handle if the object has relationship.

            example:
                result = db.delete('Service', user_id='c0a5be5a-94bf-4ad8-95dc-1d6e54cb1aed', name='Gardening')
                in this example will delete the row where the user_id is associated with the service we want to 
                delete in user_service_assoc table.
            
            there is a section to test the function after this method. 
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            # Retrieve the model class from the classes_dict based on the model_name
            model_class = self.classes_dict.get(model_name)
            if not model_class:
                return None

            # Create a new query object for the specified model_class
            query = session.query(model_class)

            # Iterate over the key-value in the kwargs(data) dictionary
            for key, value in data.items():
                # Attempt to retrieve the column attribute from the model_class using the key
                column = getattr(model_class, key, None)
                if column is not None:
                    # If a valid column is found, apply the filtering condition to the query
                    query = query.filter(getattr(model_class, key) == value)

            # Execute the query and retrieve all the filtered objects
            objs_to_delete = query.all()

            # If no objects are found, return True
            if not objs_to_delete:
                print("No objects found to delete.")
                return True

            # Iterate over the filtered objects and handle deletions based on relationships
            for obj in objs_to_delete:
                if model_name == 'Service' and user_id:
                    # If the model is 'Service' and user_id is provided,
                    # delete the associated UserServiceAssoc object for the specific user
                    assoc_obj = session.query(UserServiceAssoc)\
                    .filter(UserServiceAssoc.service_id == obj.id,\
                            UserServiceAssoc.user_id == user_id).all()

                    if assoc_obj:
                        for obj in assoc_obj:
                            session.delete(obj)
                else:
                    # Delete all associated UserServiceAssoc objects first
                    assoc_objs = session.query(UserServiceAssoc)\
                    .filter(UserServiceAssoc.user_id == obj.id).all()
                    for assoc_obj in assoc_objs:
                        session.delete(assoc_obj)

                    # Delete the filtered objects themselves
                    session.delete(obj)

            session.commit()
            return True

        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")
            return False

        finally:
            session.close()



db = DBOperations()


# -----DELETE_TEST----- #


# print("Deleting Service associated to an user...")
# result = db.delete('Service', user_id='63a047ec-c9fc-490a-8bbf-8ae8e66dd715', name='Auto Body Painting')
# if result:
#     print("Deleted successfully.")


# -----FILTER_TEST----- #

# Filter User objects based on their associated Service and Town
filtered_objs = db.filter({'User':{}})
print(filtered_objs)