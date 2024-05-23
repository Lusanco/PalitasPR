
#!/usr/bin/python3
"""
    ALLOWS OPERATIONS FOR FRONT END DEVS
    THIS FILE WILL BRIDGE OUR CLASSES AND FLASK
    USING LOCAL POSTGRES DB NEED TO CHAMGE TO AWS

"""
from os import getenv
from time import time
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.relationships import RelationshipProperty
from models import User, Service, Town, Promo_Towns, Review, Task, Promotion, Request, Request_Towns, Promotion
from base_model import BaseModel, Base
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
from emails import send_confirm_email
from sqlalchemy import func
import random
import datetime
from sqlalchemy.dialects.postgresql import UUID
from unidecode import unidecode
from aws_bucket import create_model_folder
from email_validator import validate_email, EmailNotValidError


class DBOperations():

    classes_dict = {
                'User': User,
                'Service': Service,
                'Town': Town,
                'UserServiceAssoc': Promo_Towns,
                'Review': Review,
                'Task': Task,
                'Promotion': Promotion,
                'Request': Request
                }


    def __init__(self):
        self.engine = create_engine('postgresql://demo_dev:demo_dev_pwd@demodb.ctossyay6vcz.us-east-2.rds.amazonaws.com/postgres')    


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

            session.add(new_object)

            # check if object needs aws folder
            aws_folders = {
                Promotion: 'Promotion',
                Request: 'Request',
                Review: 'Review'
                }
            if model_class in aws_folders:
                response = create_model_folder(
                    new_object.user_id,
                    aws_folders[model_class],
                    new_object.id)
                print(response)

            session.commit()
            session.close()
            return new_object
        else:
            print("Not a valid class")
            session.close()
            return None


    def filter(self, model=None, service=None, town='all'):
        """
        Retrieve objects based on specified criteria from url query

        Usage: model=promotions or model=<requests>, service=<DJ>, town=<all> or specific <town>

        Returns: List of dict of the post details
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        my_service_id = None

        if model:
            town_name = unidecode(town).lower()
            if service:
                service_name = unidecode(service).lower()
            else:
                print('no service name provided')
                session.close()
                return {}

            # Check if service exists
            service = session.query(Service).filter(func.lower(Service.name).op("~")(f"{service_name}")).first()
            if service:
                my_service_id = service.id
                service_name = service.name
            else:
                print(f"No service found with name: {service_name}")
                session.close()
                return {}

        if my_service_id is not None:
            
            if model == 'promotions':
                rows = self.explore_promos(session, my_service_id, town_name)
            if model == 'requests':
                rows = self.explore_requests(session, my_service_id, town_name)

            # List to put inside all dicts
            list_of_dict = []

            for row in rows:
                if model == 'promotions': # Promotions dictionary data
                    inner_dict = {
                        'promo_id': str(row.promo_id),
                        'service': service_name,
                        'title': row.title,
                        'description': row.description,
                        'price_min': row.price_min,
                        'price_max': row.price_max,
                        'first_name': row.first_name,
                        'last_name': row.last_name,
                        'towns': row[3],
                        'created_at': row.created_at.strftime("%Y-%m-%d")
                    }
                else: # Requests dictionary data
                    inner_dict = {
                        'request_id': str(row.request_id),
                        'service': service_name,
                        'title': row.title,
                        'description': row.description,
                        'first_name': row.first_name,
                        'last_name': row.last_name,
                        'towns': row[3],
                        'created_at': row.created_at.strftime("%Y-%m-%d")
                    }

                list_of_dict.append(inner_dict)

            session.close()
            return(list_of_dict)
        else:
            session.close()
            return {}

    def explore_promos(self, session, my_service_id, town_name):
        '''
            Main query to filter promotions
        '''
        if town_name == 'all':  # Get all promotions of a service in all towns
            print("Doing all")
            rows = session.query(Promo_Towns.promo_id,
                                User.first_name,
                                User.last_name,
                                func.array_agg(Town.name),
                                Promotion.created_at,
                                Promotion.title,
                                Promotion.description,
                                Promotion.price_min,
                                Promotion.price_max
                                ) \
            .select_from(Promotion)\
            .join(User, Promotion.user_id == User.id)\
            .join(Promo_Towns, Promotion.id == Promo_Towns.promo_id)\
            .join(Town, Promo_Towns.town_id == Town.id)\
            .filter((Promotion.service_id == my_service_id))\
            .group_by(Promo_Towns.promo_id,
                    User.first_name,
                    User.last_name,
                    Promotion.created_at,
                    Promotion.description,
                    Promotion.title,
                    Promotion.price_min,
                    Promotion.price_max
                    )\
            .order_by(Promo_Towns.promo_id)\
            .all()
            return rows
        else:  # Get all promotions of a service in a single town
            print("Doing Specific town")
            rows = session.query(Promo_Towns.promo_id,
                                User.first_name, User.last_name,
                                func.array_agg(Town.name),
                                Promotion.created_at,
                                Promotion.title,
                                Promotion.description,
                                Promotion.price_min,
                                Promotion.price_max
                                ) \
            .select_from(Promotion)\
            .join(User, Promotion.user_id == User.id)\
            .join(Promo_Towns, Promotion.id == Promo_Towns.promo_id)\
            .join(Town, Promo_Towns.town_id == Town.id)\
            .filter((Promotion.service_id == my_service_id) & (func.lower(Town.name).op("~")(f"{town_name}")))\
            .group_by(Promo_Towns.promo_id,
                    User.first_name,
                    User.last_name,
                    Promotion.created_at,
                    Promotion.title,
                    Promotion.description,
                    Promotion.price_min,
                    Promotion.price_max)\
            .order_by(Promo_Towns.promo_id)\
            .all()
            return rows

    def explore_requests(self, session, my_service_id, town_name):
        '''
            Main query to filter requests
        '''
        if town_name == 'all':  # Get all promotions of a service in all towns
            print("Doing all")
            rows = session.query(Request_Towns.request_id,
                                User.first_name,
                                User.last_name,
                                func.array_agg(Town.name),
                                Request.created_at,
                                Request.title,
                                Request.description
                                ) \
            .select_from(Request)\
            .join(User, Request.user_id == User.id)\
            .join(Request_Towns, Request.id == Request_Towns.request_id)\
            .join(Town, Request_Towns.town_id == Town.id)\
            .filter((Request.service_id == my_service_id))\
            .group_by(Request_Towns.request_id, User.first_name, User.last_name, Request.created_at, Request.description, Request.title)\
            .order_by(Request_Towns.request_id)\
            .all()
            return rows
        else:  # Get all Requests of a service in a single town
            print("Doing Specific town")
            rows = session.query(Request_Towns.request_id,
                                User.first_name, User.last_name,
                                func.array_agg(Town.name),
                                Request.created_at,
                                Request.title,
                                Request.description
                                ) \
            .select_from(Request)\
            .join(User, Request.user_id == User.id)\
            .join(Request_Towns, Request.id == Request_Towns.request_id)\
            .join(Town, Request_Towns.town_id == Town.id)\
            .filter((Request.service_id == my_service_id) & (func.lower(Town.name).op("~")(f"{town_name}")))\
            .group_by(Request_Towns.request_id, User.first_name, User.last_name, Request.created_at, Request.title, Request.description)\
            .order_by(Request_Towns.request_id)\
            .all()
            return rows

    def promo_request(self, user_id):
        """
            Query promotions and requests from a specified user
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        promotions = self.my_promos(session, user_id)
        requests = self.my_requests(session, user_id)

        # List to put inside all dicts
        promos_dict = []
        requests_dict = []

        for row in promotions:
            inner_dict = {
                'promo_id': str(row.promo_id),
                'service': row.name,
                'title': row.title,
                'description': row.description,
                'price_min': row.price_min,
                'price_max': row.price_max,
                'first_name': row.first_name,
                'last_name': row.last_name,
                'towns': row[3],
                'created_at': row.created_at.strftime("%Y-%m-%d")
            }
            promos_dict.append(inner_dict)
            for row in requests:
                inner_dict = {
                    'request_id': str(row.request_id),
                    'service': row.name,
                    'title': row.title,
                    'description': row.description,
                    'first_name': row.first_name,
                    'last_name': row.last_name,
                    'towns': row[3],
                    'created_at': row.created_at.strftime("%Y-%m-%d")
                }

                requests_dict.append(inner_dict)

        session.close()
        return(promos_dict, requests_dict)

    def my_promos(self, session, my_user_id):
        '''
            Main query to filter promotions
        '''
        print(f'Inside my_promos def, my user id is: {my_user_id}')
        rows = session.query(Promo_Towns.promo_id,
                            User.first_name,
                            User.last_name,
                            func.array_agg(Town.name),
                            Promotion.created_at,
                            Promotion.title,
                            Promotion.description,
                            Promotion.price_min,
                            Promotion.price_max,
                            Service.name
                            ) \
        .select_from(Promotion)\
        .join(User, Promotion.user_id == User.id)\
        .join(Promo_Towns, Promotion.id == Promo_Towns.promo_id)\
        .join(Town, Promo_Towns.town_id == Town.id)\
        .join(Service, Promotion.service_id == Service.id)\
        .filter((Promotion.user_id == my_user_id))\
        .group_by(Promo_Towns.promo_id,
                User.first_name,
                User.last_name,
                Promotion.created_at,
                Promotion.description,
                Promotion.title,
                Promotion.price_min,
                Promotion.price_max,
                Service.name
                )\
        .order_by(Promo_Towns.promo_id)\
        .all()
        return rows

    def my_requests(self, session, my_user_id):
        '''
            Main query to filter promotions
        '''
        print(f'Inside my_promos def, my user id is: {my_user_id}')
        rows = session.query(Request_Towns.request_id,
                            User.first_name,
                            User.last_name,
                            func.array_agg(Town.name),
                           Request.created_at,
                           Request.title,
                           Request.description,
                           Service.name
                            ) \
        .select_from(Request)\
        .join(User, Request.user_id == User.id)\
        .join(Request_Towns, Request.id == Request_Towns.request_id)\
        .join(Town, Request_Towns.town_id == Town.id)\
        .join(Service, Request.service_id == Service.id)\
        .filter((Request.user_id == my_user_id))\
        .group_by(Request_Towns.request_id,
                User.first_name,
                User.last_name,
                Request.created_at,
                Request.description,
                Request.title,
                Service.name
                )\
        .order_by(Request_Towns.request_id)\
        .all()
        return rows

    # def delete(self, data):
    #     """
    #         Delete objects and handle if the object has relationship
    #         Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}
    #     """
    #     session = sessionmaker(bind=self.engine)
    #     session = session()

    #     model_name = list(data.keys())[0]
    #     model_class = self.classes_dict.get(model_name)
    #     if not model_class:
    #         print("\nInvalid model name.\n")
    #         session.close()
    #         return None

    #     inner_dict = data[model_name]
    #     query = session.query(model_class)

    #     for key, value in inner_dict.items():
    #         column = getattr(model_class, key, None)
    #         if column is not None:
    #             query = query.filter(getattr(model_class, key) == value)
    #         else:
    #             print(f"\nInvalid attribute '{key}' for model '{model_name}'.\n")
    #             session.close()
    #             return None

    #     objs_to_delete = query.all()
    #     if not objs_to_delete:
    #         print("No object found to delete.\n")
    #         session.close()
    #         return True
        
    #     for obj in objs_to_delete:
    #         if model_name == 'User':
    #             password = input("Enter your password to confirm delete: ")
    #             if not self.confirm_password(obj, password):
    #                 print("Incorrect password.")
    #                 session.close()
    #                 return False
    #             else:
    #                 # Print the user's first name and last name when deleted
    #                 print(f"User {obj.first_name} {obj.last_name} deleted.")

    #         if model_name == 'Service' and 'user_id' in inner_dict:
    #             # If the model is 'Service' and user_id is provided,
    #             # delete the associated UserServiceAssoc object for the specific user
    #             assoc_obj = session.query(UserServiceAssoc) \
    #                 .filter(UserServiceAssoc.service_id == obj.id,
    #                         UserServiceAssoc.user_id == inner_dict['user_id']).all()

    #             if assoc_obj:
    #                 for obj in assoc_obj:
    #                     session.delete(obj)
    #         else:
    #             # Delete all associated UserServiceAssoc objects first
    #             assoc_objs = session.query(UserServiceAssoc) \
    #                 .filter(UserServiceAssoc.user_id == obj.id).all()
    #             for assoc_obj in assoc_objs:
    #                 session.delete(assoc_obj)

    #             # Delete the filtered objects themselves
    #             session.delete(obj)

    #     session.commit()
    #     session.close()
    #     return True


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
                return ({'message':"Object ID not provided."}, 400)
        else:
            return ({'message':"Class not found"}, 400)

        session.close()
        return ({'message': "ok"}, 200)


    def login(self, email=None, pwd=None):
        '''
        Validate login for a user
        If valid,  db.new() will be called to handle the user creation
        USAGE: Receive pwd and email of user
        '''
        Session = sessionmaker(bind=self.engine)
        session = Session()

        response = {"message": "Null Email or Password"}, 400 # BAd request, NULL email or pawd
        if email and pwd:
            user = session.query(User).filter_by(email=email).first()

            if user:
                # Retrieve the hashed password from the database
                hashed_password = user.password.encode('utf-8')  # Ensure it's encoded as bytes

                # Verify the password using bcrypt
                if bcrypt.checkpw(pwd.encode('utf-8'), hashed_password):
                    response = {"message": user}, 200
                else:
                    response = {"message": "Invalid credentials"}, 401
            else:
                response = {"message": "Invalid credentials"}, 404  # Email not found
        session.close()
        return response

    def sign_up(self, data):
        '''
            user signs up THIS IS A ROUGH SKETCH IDEA
            USAGE: Send a dict of the user to create {name: ..., email:...,...}
        '''
        import bcrypt
        import secrets
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
            return {'message': 'Missing a required field'}, 400
        
            # Validate email format
        try:
            validate_email(email)
        except EmailNotValidError as e:
            print(f"Error: Invalid email format - {e}")
            session.close()
            return {'message': f'{e}'}, 400

        # Check if email doesnt exist in db
        user = session.query(User).filter_by(email=email).first()
        if user:
            print("Email is already in use")
            session.close()
            return {'message': 'Email already in use'}, 409

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

        # Generate a verification token for the user
        verification_token = secrets.token_urlsafe(32)  # Generate a URL-safe token

        dict_of_user = {
        'email': email,
        'password': new_hashed_password,
        'first_name': first_name,
        'last_name': last_name,
        'verification_token': verification_token
        }
        send_confirm_email(email, first_name, verification_token)
        obj = self.new({'User': dict_of_user})
        session.close()
        if obj:
            return {'message': 'Account created'}, 201
        else:
            return {'message': 'Error in signup logic'}, 500


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

    def search(self, class_name, obj_id):
        """
        Search for an object based on its class model and ID.
        """
        if class_name in self.classes_dict:
            model_class = self.classes_dict[class_name]
            Session = sessionmaker(bind=self.engine)
            session = Session()
            obj = session.query(model_class).filter_by(id=obj_id).first()
            session.close()
            if obj:
                return obj
            else:
                return None
        else:
            return None

    # def search_all_objects(self, class_name, service_id=None):
    #     """
    #     Retrieve all Promotion objects from the database.
    #     """
    #     if class_name in self.classes_dict:
    #         model_class = self.classes_dict[class_name]

    #         Session = sessionmaker(bind=self.engine)
    #         session = Session()

    #         if service_id:
    #             obj = session.query(model_class).filter_by(service_id=service_id).all()
    #         else:
    #             obj = session.query(model_class).all()

    #         session.close()

    #         return obj
    #     else:
    #         return None
