
#!/usr/bin/python3
"""
    ALLOWS OPERATIONS FOR FRONT END DEVS
    THIS FILE WILL BRIDGE OUR CLASSES AND FLASK

"""
from os import getenv
from time import time
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.relationships import RelationshipProperty
from models import User, Service, Town, UserServiceAssoc
from base_model import BaseModel, Base

class DBOperations():

    classes_dict = {
                'User': User,
                'Service': Service,
                'Town': Town,
                'UserServiceAssoc': UserServiceAssoc
                }


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

        Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}

        example:
            filtered_objs = db.filter({'User': {'name': 'service_name', 'town': 'town_name'}}).

            There is a section to test the function after the delete method.
        """

        Session = sessionmaker(bind=self.engine)
        session = Session()

        town_name = "All"
        model_name = list(data.keys())[0]
        data_dict = data[model_name]

        model_class = self.classes_dict.get(model_name)

        if model_class:
            if 'town' in data_dict:
                town_name = data_dict['town']
            if 'name' in data_dict:
                service_name = data_dict['name']
            else:
                print('no service name provided') 
            service = session.query(Service).filter_by(name = service_name).first()
            my_service_id = service.id

        if town_name == 'All':
            print("Doing all")
            rows = session.query(UserServiceAssoc.user_id,User.first_name, User.last_name, func.array_agg(Town.name)) \
            .join(Town) \
            .join(User)\
            .filter(UserServiceAssoc.service_id == my_service_id) \
            .group_by(UserServiceAssoc.user_id, User.first_name, User.last_name) \
            .order_by(UserServiceAssoc.user_id) \
            .all()
        else:
            print("Doing Specific town")
            rows = session.query(UserServiceAssoc.user_id,User.first_name, User.last_name, func.array_agg(Town.name)) \
            .join(Town) \
            .join(User)\
            .filter((UserServiceAssoc.service_id == my_service_id) & (Town.name == town_name)) \
            .group_by(UserServiceAssoc.user_id, User.first_name, User.last_name) \
            .order_by(UserServiceAssoc.user_id) \
            .all()

        my_dict = {}

        for row in rows:
            user_id = row.user_id
            first_name = row.first_name
            last_name = row.last_name
            town_names = row[3]  # Assuming the array of town names is at index 3
            inner_dict = {
                'service': service_name,
                'first_name': first_name,
                'last_name': last_name,
                'towns': town_names
            }
            my_dict[user_id] = inner_dict

        # print(f"MY DICTIONARY: {my_dict}")
        session.close()
        return(my_dict)


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


    def update(self, data):
        """
            Update an object from Data Base
            Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()
    
        class_name = list(data.keys())[0] # First key, class name
        if class_name in self.classes_dict:
            update_dict = {}
            update_dict.update(data[class_name])

            # User id from dict of front data
            if 'id' in update_dict:
                user_id = update_dict['id']
                update_dict.pop('id')
            else:
                return 'Id not found'

            # Perform the query
            user = session.query(self.classes_dict[class_name]).filter_by(id=user_id).first()

            user_dict = user.all_columns()
            user_dict.update(update_dict)

            for key, value in user_dict.items():
                setattr(user, key, value)

            # Commit the changes to the database
            session.commit()
            print("Object was updated")
            # Close the session
        else:
            return "Class Not Found"
        session.close()
        return "Object updated"



# -------------TEST AREA DONT TOUCH FRONT USERS----------------------
# db = DBOperations()
# start_time = time()

# db.update({'User': {'id': '2cc63d22-a074-4f6a-84ab-66db61eb279a', 'last_name': 'Santiago'}})

# db.new({'User': {'first_name': 'Pepe', 'last_name': 'Gomez', 'email': 'pepito@gmail.com'}})
# -----DELETE_TEST----- 

# print("Deleting Service associated to an user...")
# result = db.delete('Service', user_id='c0a5be5a-94bf-4ad8-95dc-1d6e54cb1aed', name='Gardening')
# if result:
#     print("Deleted successfully.")


# -----FILTER_TEST----- 

# filtered_objs = db.filter({'User': {'name': 'Auto Body Painting'}})
# print(filtered_objs)

# end_time = time()
# elapsed_time = end_time - start_time
# print("Time taken:", elapsed_time, "seconds")
