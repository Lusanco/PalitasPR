'''
    All related functions for user class that involves the database
    and routes from flask
'''
from emails import send_confirm_email
from email_validator import validate_email, EmailNotValidError
from models import User, Initial_Contact, Profile, Review, Task
from db.db_operations import DBOperations
from db.db_task import Db_task
from sqlalchemy import or_
import aws_bucket
import bcrypt


class Db_user:
    '''
        Class to call when using any user functionality
        required.

        Examples:
        * User queries
        * User route functionality  like login or signup
    '''
    def __init__(self, db_session):
        self.session = db_session

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

        keys=['phone', 'first_name', 'last_name', 'password', 'email']
        email = data["email"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        password = data["password"]
        phone = data['phone']

        for key in keys:
            if key not in keys:
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
            'phone': phone
        }
        response, status = DBOperations(self.session).new({"User": dict_of_user})
        if status != 201:
            return response, status
        send_confirm_email(email, first_name, verification_token)
        return response, status

    # WORKING DOWN HEERE NEED TEST
    def get_contacts_section(self, user_id):
        """
            get all initial contact messages user has received and its tasks
        """
        all_contacts = {}
        sent_contacts = []
        received_contacts = []

        initialContacts = self.session.query(Initial_Contact)\
            .filter(or_(Initial_Contact.receiver_id==user_id, Initial_Contact.sender_id==user_id))\
            .order_by(Initial_Contact.updated_at.desc())\
            .all()
        if not initialContacts:
            return {'results': None}, 200

        for initialContact in initialContacts:
            contact_dict = {}
            contact_dict.update(initialContact.all_columns())
            task = Db_task(self.session).get_task_by_contactId(initialContact.id)
            if task:
                contact_dict['task'] = task.all_columns()
            else:
                contact_dict['task'] = None
            # DO NOT TOUCH LINE BELOW, adding object to session, prevent detached objects error on lazy loads
            initialContact = self.session.merge(initialContact)

            # received_contacts: The user is the receiver, we need sender info
            if user_id == initialContact.receiver_id:
                sender = initialContact.sender
                contact_dict['sender_first_name'] = sender.first_name
                contact_dict['sender_last_name'] = sender.last_name
                contact_dict['sender_email']= sender.email
                contact_dict['phone'] = sender.phone
                contact_dict.pop('receiver_id')
                received_contacts.append(contact_dict)
            else: # sent_contacts: User is sender, we need receiver_info
                receiver = initialContact.receiver
                contact_dict['receiver_first_name'] = receiver.first_name
                contact_dict['receiver_last_name'] = receiver.last_name
                contact_dict['receiver_email']= receiver.email
                contact_dict['phone'] = receiver.phone
                contact_dict.pop('sender_id')
                sent_contacts.append(contact_dict)

            all_contacts['received'] = received_contacts
            all_contacts['sent'] = sent_contacts
        return {'results': all_contacts}, 200

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

    # ONLY FOR DATABASE RESETS
    def create_folders_for_allUsers(self):
        '''
            after resetting db, lets make all folders for users
        '''
        users = self.session.query(User).all()
        for user in users:
            aws_bucket.create_user_folder(user.id)
        return 'Succes'
