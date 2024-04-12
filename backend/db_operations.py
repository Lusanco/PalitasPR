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
from models import User, Service, Town, UserServiceAssoc, Task
from base_model import BaseModel, Base

class DBOperations():

    classes_dict = {
                'User': User,
                'Service': Service,
                'Town': Town,
                'UserServiceAssoc': UserServiceAssoc,
                'Task': Task
                }


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
            user_id = str(row.user_id)
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

            # Check if the class is Task
            if class_name == 'Task':
                task_id = update_dict.get('id')
                status = update_dict.get('status')
                review = update_dict.get('review')
                rating = update_dict.get('rating')

                if task_id:
                    task = session.query(self.classes_dict[class_name]).filter_by(id=task_id).first()

                    if task:
                        task.status = status
                        task.review = review
                        task.rating = rating

                        session.commit()
                        print("Task updated successfully.")
                    else:
                        print("Task not found.")
                else:
                    return "Task ID not provided."
            else:
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
        else:
            return "Class Not Found"
        session.close()
        return "Object updated"
    

    def insert_task(self, data):
        """
        Insert a task into the database based on the provided parameters.
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Extract model_name and data_dict from the input data
        model_name = list(data.keys())[0]
        data_dict = data[model_name]

        # Determine the model class based on the model_name
        model_class = self.classes_dict.get(model_name)

        if not model_class:
            print("Invalid model_name.")
            session.close()
            return

        # Retrieve parameters for the task from data_dict
        provider_id = data_dict.get('provider_id')
        receiver_id = data_dict.get('receiver_id')
        service_name = data_dict.get('service_name')
        status = data_dict.get('status')
        review = data_dict.get('review')
        rating = data_dict.get('rating')

        if not all([
            provider_id,
            receiver_id,
            service_name
            ]):
            print("Missing parameters.")
            session.close()
            return

        # Retrieve provider and receiver
        provider = session.query(User)\
            .filter_by(id=provider_id,).first()
        receiver = session.query(User)\
            .filter_by(id=receiver_id).first()

        if not provider or not receiver:
            print("Provider or receiver not found.")
            session.close()
            return

        # Retrieve service
        service = session.query(Service)\
            .filter_by(name=service_name).first()

        if not service:
            print("Service not found.")
            session.close()
            return

        # Check if the provider has the service associated
        if not session.query(UserServiceAssoc)\
            .filter_by(user_id=provider.id, service_id=service.id).first():
            print("Provider does not offer this service.")
            return

        # Insert task
        task = Task(
            provider_id=provider.id,
            receiver_id=receiver.id,
            service_id=service.id,
            status=status,
            review=review,
            rating=rating
        )

        session.add(task)
        session.commit()

        print("Task inserted successfully.")
        session.close()




# -------------TEST AREA DONT TOUCH FRONT USERS----------------------
db = DBOperations()
# start_time = time()

# db.update({'User': {'id': '2cc63d22-a074-4f6a-84ab-66db61eb279a', 'last_name': 'Santiago'}})

# db.new({'User': {'first_name': 'Pepe', 'last_name': 'Gomez', 'email': 'pepito@gmail.com'}})
# -----DELETE_TEST----- 

# print("Deleting Service associated to an user...")
# result = db.delete('Service', user_id='c0a5be5a-94bf-4ad8-95dc-1d6e54cb1aed', name='Gardening')
# if result:
#     print("Deleted successfully.")


# -----FILTER_TEST----- 

filtered_objs = db.filter({'User': {'name': 'Auto Body Painting'}})
print(filtered_objs)


# -----TASK_TEST-----

# data = {
#     'Task': {
#         'provider_id': 'f648ac2c-b651-46c1-bc58-8d035d302e25',
#         'receiver_id': '878d0084-c65d-4814-9d61-dc186ecdd344',
#         'service_name': 'Auto Body Painting',
#         'status': 'Pending'
#     }
# }

# db.insert_task(data)


# -----UPDATE_TASK_TEST-----

# data = {
#     'Task': {
#         'id': 'd6a57008-19c9-4d72-a96e-da3084bff5b2',
#         'status': 'Completed',
#         'review': 'Great service!',
#         'rating': 5.0
#     }
# }

# db.update(data)

# end_time = time()
# elapsed_time = end_time - start_time
# print("Time taken:", elapsed_time, "seconds")