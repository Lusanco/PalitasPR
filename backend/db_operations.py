
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
        inner_dict = front_data[model_name] # inner_dict = {"first_name": "Louis", "last_name": "Toro"}

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


    def filter(self, model_name, **data):
        """
            Retrieve objects based on specified criteria.

            Args:
                model_name: In our case the name of the class.
                **data: Keyword arguments representing filtering criteria.
                    example:
                        filtered_objs = db.filter('User', service={'name': 'Gardening'})
                        in this example will show all the USERS who is doing Gardening.

            there is a section to test the function after the delete method.

            note: need fix to handle to view all services offered by an user
        """


        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            # Retrieve the model class from the classes_dict based on the model_name
            model_class = self.classes_dict[model_name]
        except KeyError:
            session.close()
            return None

        query = session.query(model_class)

        # Iterate over the key-value in the kwargs(data) dictionary
        for key, value in data.items():
            column = getattr(model_class, key, None)
            if column is not None:
                # If a valid column is found, apply the filtering condition to the query
                query = query.filter(getattr(model_class, key) == value)

            # Check if the key represents a relationship with Service
            if key == 'service':
                query = query.join(UserServiceAssoc)
                query = query.join(Service)

                # Apply filtering conditions on the Service model
                for service_key, service_value in value.items():
                    service_column = getattr(Service, service_key, None)
                    if service_column is not None:
                        query = query.filter(getattr(Service, service_key) == service_value)

        filtered_objs = query.all()

        # Serialize the filtered objects by calling the all_columns method on each object
        serialized_objs = [obj.all_columns() for obj in filtered_objs]

        session.close()
        return serialized_objs



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
                            UserServiceAssoc.user_id == user_id).first()

                    if assoc_obj:
                        session.delete(assoc_obj)
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



# db = DBOperations()


# -----DELETE_TEST----- #


# print("Deleting Service associated to an user...")
# result = db.delete('Service', user_id='c0a5be5a-94bf-4ad8-95dc-1d6e54cb1aed', name='Gardening')
# if result:
#     print("Deleted successfully.")


# -----FILTER_TEST----- #

# Filter User objects based on their associated Service and Town
# filtered_objs = db.filter('Town', service={'name': 'Gardening'})
# print(filtered_objs)
