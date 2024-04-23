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
from models import User, Service, Town, UserServiceAssoc, Review, Task
from base_model import BaseModel, Base
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt


class DBOperations():

    classes_dict = {
                'User': User,
                'Service': Service,
                'Town': Town,
                'UserServiceAssoc': UserServiceAssoc,
                'Review': Review,
                'Task': Task
                }


    def __init__(self):
        self.engine = create_engine('postgresql://demo_dev:demo_dev_pwd@localhost/demo_db')    


    def new(self, front_data):
        """
            Add new obj to database

            get():
                retrieves the value associated with the model_name key from the self.classes_dict dictionary.
                If model_name is found in the dictionary, model_class will be assigned the corresponding value
        """
        if front_data is None:
            return None

        # print(front_data)
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
        my_service_id = None

        if model_class:
            if 'town' in data_dict:
                town_name = data_dict['town']
            if 'name' in data_dict:
                service_name = data_dict['name']
            else:
                print('no service name provided')
                session.close()
                return {}

            service = session.query(Service).filter_by(name=service_name).first()
            if service:
                my_service_id = service.id
            else:
                print(f"No service found with name: {service_name}")
                session.close()
                return {}
        if my_service_id is not None:
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
        else:
            session.close()
            return {}


    def delete(self, data):
        """
            Delete objects and handle if the object has relationship
            Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}
        """
        session = sessionmaker(bind=self.engine)
        session = session()

        model_name = list(data.keys())[0]
        model_class = self.classes_dict.get(model_name)
        if not model_class:
            print("\nInvalid model name.\n")
            session.close()
            return None
        
        inner_dict = data[model_name]
        query = session.query(model_class)

        for key, value in inner_dict.items():
            column = getattr(model_class, key, None)
            if column is not None:
                query = query.filter(getattr(model_class, key) == value)
            else:
                print(f"\nInvalid attribute '{key}' for model '{model_name}'.\n")
                session.close()
                return None

        objs_to_delete = query.all()
        if not objs_to_delete:
            print("No object found to delete.\n")
            session.close()
            return True
        
        for obj in objs_to_delete:
            if model_name == 'User':
                password = input("Enter your password to confirm delete: ")
                if not self.confirm_password(obj, password):
                    print("Incorrect password.")
                    session.close()
                    return False
                else:
                    # Print the user's first name and last name when deleted
                    print(f"User {obj.first_name} {obj.last_name} deleted.")

            if model_name == 'Service' and 'user_id' in inner_dict:
                # If the model is 'Service' and user_id is provided,
                # delete the associated UserServiceAssoc object for the specific user
                assoc_obj = session.query(UserServiceAssoc) \
                    .filter(UserServiceAssoc.service_id == obj.id,
                            UserServiceAssoc.user_id == inner_dict['user_id']).all()

                if assoc_obj:
                    for obj in assoc_obj:
                        session.delete(obj)
            else:
                # Delete all associated UserServiceAssoc objects first
                assoc_objs = session.query(UserServiceAssoc) \
                    .filter(UserServiceAssoc.user_id == obj.id).all()
                for assoc_obj in assoc_objs:
                    session.delete(assoc_obj)

                # Delete the filtered objects themselves
                session.delete(obj)

        session.commit()
        session.close()
        return True


    def update(self, data):
        """
            Update an object from Data Base
            Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        class_name = list(data.keys())[0]  # First key, class name
        if class_name in self.classes_dict:
            update_dict = {}
            update_dict.update(data[class_name])

            # Get the object ID from the update_dict
            obj_id = update_dict.pop('id', None)

            if obj_id:
                # Retrieve the object from the database
                model_class = self.classes_dict[class_name]
                obj = session.query(model_class).filter_by(id=obj_id).first()

                if obj:
                    # Iterate over the remaining key-value pairs in update_dict
                    for key, value in update_dict.items():
                        # Check if the attribute exists in the model
                        if hasattr(model_class, key):
                            setattr(obj, key, value)
                        else:
                            print(f"Attribute '{key}' not found in {class_name} model.")

                    session.commit()
                    print(f"{class_name} object with ID {obj_id} updated successfully.")
                else:
                    print(f"{class_name} object with ID {obj_id} not found.")
            else:
                return "Object ID not provided."
        else:
            return "Class Not Found"

        session.close()
        return "Object updated"


    def login(self, email=None, pwd=None):
        '''
        Validate login for a user
        If valid,  db.new() will be called to handle the user creation
        USAGE: Receive pwd and email of user
        '''
        Session = sessionmaker(bind=self.engine)
        session = Session()
        
        if email and pwd:
            user = session.query(User).filter_by(email=email).first()

            if user:
                # Retrieve the hashed password from the database
                hashed_password = user.password.encode('utf-8')  # Ensure it's encoded as bytes

                # Verify the password using bcrypt
                if bcrypt.checkpw(pwd.encode('utf-8'), hashed_password):
                    print(f"\nLogin successful for user: {user.first_name} {user.last_name}\n")
                else:
                    print(f"\nEmail or password INCORRECT, try again\n")
            else:
                print(f"\nNo user found with email: {email}\n")
        
        session.close()


    def sign_up(self, data):
        '''
            user signs up THIS IS A ROUGH SKETCH IDEA
            USAGE: Send a dict of the user to create {name: ..., email:...,...}
        '''
        import bcrypt
        Session = sessionmaker(bind=self.engine)
        session = Session()

        print("Data received:", data)

        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        pwd = data['password']
        

        # Check if all required fields are present
        if not (email and first_name and last_name and pwd):
            print("Error: Missing required fields.")
            session.close()
            return None


        # Check if email doesnt exist in db
        user = session.query(User).filter_by(email=email).first()
        if user:
            print("Email is already in use")
            session.close()
            return None
        
        # Check if passwords match
        # if pwd != confirm_pwd:
        #     print("Passwords do not match")
        #     session.close()
        #     return

        # Generate a new password hash with bcrypt and 12 rounds
        # .encode is needed to hash properly, but we need to decode before saving to db
        # we use this for sensitive data
        new_hashed_password = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt(rounds=12))
        new_hashed_password = new_hashed_password.decode('utf-8')  # Decode bytes to string for SQLAlchemy

        dict_of_user = {
        'email': email,
        'password': new_hashed_password,
        'first_name': first_name,
        'last_name': last_name
        }

        obj = self.new({'User': dict_of_user})
        session.close()
        return (obj)


    def confirm_password(self, user_obj, password):
        """
        Confirm the password for the given user object.
        """

        # Retrieve the hashed password from the database
        hashed_password = user_obj.password.encode('utf-8')

        # Verify the password using bcrypt
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True
        else:
            return False


# # -------------TEST AREA DONT TOUCH FRONT USERS----------------------
# db = DBOperations()


#------- SIGN_UP TEST ---------------------------

# db.sign_up({'email': "antoniofdjs@gmail.com", 'password': '9150', 'first_name': 'Antonio', 'last_name': 'De Jesus'})

#-------------------------------------------------
# start_time = time()

# ----- LOGIN TEST ------
# db.login('jd123@gmail.com', 'pwd1')
# -----------------------

# db.update({'User': {'id': '2cc63d22-a074-4f6a-84ab-66db61eb279a', 'last_name': 'Santiago'}})

# db.new({'User': {'first_name': 'Pepe', 'last_name': 'Gomez', 'email': 'pepito@gmail.com'}})
# -----DELETE_TEST----- 

# print("Deleting Service associated to an user...")
# result = db.delete('Service', user_id='c0a5be5a-94bf-4ad8-95dc-1d6e54cb1aed', name='Gardening')
# if result:
#     print("Deleted successfully.")


# -----FILTER_TEST----- 

# filtered_objs = db.filter({'User': {'name': 'John'}})
# print(filtered_objs)

# end_time = time()
# elapsed_time = end_time - start_time
# print("Time taken:", elapsed_time, "seconds")