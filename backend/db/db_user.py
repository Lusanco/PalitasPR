'''
    All related functions for user class that involves the database
    and routes from flask
'''
from emails import send_confirm_email
from email_validator import validate_email, EmailNotValidError
from db_init import get_session
from db.db_operations import DBOperations
import bcrypt
from models import User, Initial_Contact, Profile, Review, Task
from sqlalchemy import or_


class Db_user:
    '''
        Class to call when using any user functionality
        required.

        Examples:
        * User queries
        * User route functionality  like login or signup
    '''
    def __init__(self):
        self.session = get_session()

    def login(self, email=None, password=None):
        """
        This function handles user login by verifying the provided email and password.

        usage: email="abc@gmail.com", password="123"
        """
        response = {
            "error": "Null Email or Password"
        }, 400
        if email and password:
            user = self.session.query(User).filter_by(email=email).first()

            if user:
                hashed_password = user.password.encode("utf-8")

                if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                    response = {"message": user}, 200
                else:
                    response = {"message": "Invalid credentials"}, 401
            else:
                response = {"message": "Invalid credentials"}, 404
        return response

    def sign_up(self, data):
        """
        This method handles user registration or sign-up process.

        need to receive email, first_name, last_name, password from user.
        """
        import secrets

        email = data["email"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        password = data["password"]

        if not (email and first_name and last_name and password):
            print("error: Missing required fields.")
            return {"error": "Missing a required field"}, 400

        try:
            validate_email(email)
        except EmailNotValidError as e:
            print(f"Error: Invalid email format - {e}")
            return {"message": f"{e}"}, 400

        user = self.session.query(User).filter_by(email=email).first()
        if user:
            print("Email is already in use")
            return {"Error": "Email already in use"}, 409

        new_hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt(rounds=12)
        ).decode("utf-8")

        verification_token = secrets.token_urlsafe(32)

        dict_of_user = {
            "email": email,
            "password": new_hashed_password,
            "first_name": first_name,
            "last_name": last_name,
            "verification_token": verification_token,
        }
        send_confirm_email(email, first_name, verification_token)
        # Assuming self.new is a method that handles the creation of a new user
        response, status = DBOperations().new({"User": dict_of_user})
        return response, status

    # WORKING DOWN HEERE NEED TEST
    def get_initial_contacts(self, user_id):
        """
            get all initial contact messages user has received
        """
        all_initial_contacts = []

        initialContacts = self.session.query(Initial_Contact)\
            .filter(or_(Initial_Contact.receiver_id==user_id, Initial_Contact.sender_id==user_id))\
            .order_by(Initial_Contact.updated_at.desc())\
            .all()
        if not initialContacts:
            return {'results': None}, 200

        for initialContact in initialContacts:
            contact_dict = {}
            contact_dict.update(initialContact.all_columns())
            # The user is the receiver, we need sender info
            if user_id == initialContact.receiver_id:
                sender = initialContact.sender
                contact_dict['sender_first_name'] = sender.first_name
                contact_dict['sender_last_name'] = sender.last_name
                contact_dict['sender_email']= sender.email
                contact_dict.pop('receiver_id')
            else: # User is sender, we need receiver_info
                receiver = initialContact.receiver
                contact_dict['receiver_first_name'] = receiver.first_name
                contact_dict['receiver_last_name'] = receiver.last_name
                contact_dict['receiver_email']= receiver.email
                contact_dict.pop('sender_id')
            all_initial_contacts.append(contact_dict)
        return {'results': all_initial_contacts}, 200

    def get_profile_by_userId(self, userId):
        '''
            Get profile of a user
        '''
        profile = self.session.query(Profile).join(User, User.id==Profile.user_id).filter(User.id == userId).first()
        return profile


    def rating(self, userId):
        '''
            Calculate average rating of user based on
            total rating he has on reviews associated to him
        '''
        reviews = self.session.query(Review)\
        .join(Task, Task.id == Review.task_id)\
        .join(User, User.id == Task.provider_id)\
        .filter(User.id == userId)\
        .all()
        if not reviews:
            return 0

        # Ratings range from 1 to 5
        total_tasks = len(reviews)
        ratings_total = 0
        for review in reviews:
            ratings_total += review.rating
        avg_rating = ratings_total/(5*total_tasks)
        
        rating_in_stars = avg_rating * 5
        return rating_in_stars
