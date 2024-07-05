'''
    All related functions for user class that involves the database
    and routes from flask
'''
from emails import send_confirm_email
from email_validator import validate_email, EmailNotValidError
from models import User, Initial_Contact, Profile, Review, Task, Service
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
            if initialContact.promo_id:
                contact_dict['promoRequest_title'] = initialContact.promo.title
                contact_dict['promoRequest_description'] = initialContact.promo.description
            else:
                contact_dict['promoRequest_title'] = initialContact.request.title
                contact_dict['promoRequest_description'] = initialContact.request.description

            if task:
                contact_dict['task'] = task.all_columns()
                contact_dict['task']['description'] = task.description.split('|')
                contact_dict['task'].pop('service_id')
                service = self.session.query(Service.name).filter(Service.id == task.service_id).first()
                contact_dict['task']['service'] = service[0]
            else:
                contact_dict['task'] = None
                if initialContact.promo_id:
                    contact_dict['service'] = self.session.query(Service.name).filter(Service.id == initialContact.promo.service_id).first()[0]
                else:
                    contact_dict['service'] = self.session.query(Service.name).filter(Service.id == initialContact.request.service_id).first()[0]

            # RECEIVED_CONTACTS: The user is the receiver, we need sender info
            if user_id == initialContact.receiver_id:

                sender = initialContact.sender
                receiver = initialContact.receiver
                contact_dict['contact_first_name'] = sender.first_name
                contact_dict['contact_last_name'] = sender.last_name
                contact_dict['contact_email']= sender.email
                contact_dict['phone'] = sender.phone

                # Prepare task: contact sender is task receiver | contact receiver is task provider
                if task:
                    if task.promo_id:
                        contact_dict['task']['receiver_email'] = contact_dict['contact_email']
                        contact_dict['task']['receiver_first_name'] = contact_dict['contact_first_name']
                        contact_dict['task']['receiver_last_name'] = contact_dict['contact_last_name']
                        contact_dict['task']['receiver_phone'] = contact_dict['phone']
                        contact_dict['task']['provider_first_name'] = receiver.first_name
                        contact_dict['task']['provider_last_name'] = receiver.last_name
                        contact_dict['task']['provider_email']= receiver.email
                        contact_dict['task']['provider_phone'] = receiver.phone
                        provider_id = receiver.id

                    else:
                        contact_dict['task']['provider_email'] = contact_dict['contact_email']
                        contact_dict['task']['provider_first_name'] = contact_dict['contact_first_name']
                        contact_dict['task']['provider_last_name'] = contact_dict['contact_last_name']
                        contact_dict['task']['provider_phone'] = contact_dict['phone']
                        contact_dict['task']['receiver_first_name'] = receiver.first_name
                        contact_dict['task']['receiver_last_name'] = receiver.last_name
                        contact_dict['task']['receiver_email']= receiver.email
                        contact_dict['task']['receiver_phone'] = receiver.phone
                        provider_id = sender.id

                    # LOGIC FOR PICTURE QR:
                    if contact_dict['task']['status'] in ['closed', 'reviewed']:
                        profile = self.get_profile_by_userId(provider_id)
                        print(f'qr pic {profile.qr_pic}')
                        responseAWS, statusAWS = aws_bucket.get_picture(provider_id, 'Qr', None, profile.qr_pic)
                        print(statusAWS)
                        print(responseAWS)
                        if statusAWS == 200:
                            contact_dict['task']['qr_pic'] = responseAWS['results']
                        else:
                            contact_dict['task']['qr_pic'] = None 


                contact_dict.pop('receiver_id')
                if initialContact.receiver_hide is False:
                    received_contacts.append(contact_dict)
            else: # sent_contacts: User is sender, we need receiver_info
                
                receiver = initialContact.receiver
                sender = initialContact.sender
                contact_dict['contact_first_name'] = receiver.first_name
                contact_dict['contact_last_name'] = receiver.last_name
                contact_dict['contact_email']= receiver.email
                contact_dict['phone'] = receiver.phone

                # Prepare task: contact sender is task provider | contact receiver is task receiver
                if task:
                    if task.promo_id:
                        contact_dict['task']['provider_email'] = contact_dict['contact_email']
                        contact_dict['task']['provider_first_name'] = contact_dict['contact_first_name']
                        contact_dict['task']['provider_last_name'] = contact_dict['contact_last_name']
                        contact_dict['task']['provider_phone'] = contact_dict['phone']
                        contact_dict['task']['receiver_first_name'] = sender.first_name
                        contact_dict['task']['receiver_last_name'] = sender.last_name
                        contact_dict['task']['receiver_email']= sender.email
                        contact_dict['task']['receiver_phone'] = sender.phone
                        provider_id = receiver.id
                    else:
                        contact_dict['task']['receiver_email'] = contact_dict['contact_email']
                        contact_dict['task']['receiver_first_name'] = contact_dict['contact_first_name']
                        contact_dict['task']['receiver_last_name'] = contact_dict['contact_last_name']
                        contact_dict['task']['receiver_phone'] = contact_dict['phone']
                        contact_dict['task']['provider_first_name'] = sender.first_name
                        contact_dict['task']['provider_last_name'] = sender.last_name
                        contact_dict['task']['provider_email']= sender.email
                        contact_dict['task']['provider_phone'] = sender.phone
                        provider_id = sender.id
                    # LOGIC FOR PICTURE QR:
                    if contact_dict['task']['status'] in ['closed', 'reviewed']:
                        profile = self.get_profile_by_userId(provider_id)
                        print(f'qr pic {profile.qr_pic}')
                        responseAWS, statusAWS = aws_bucket.get_picture(provider_id, 'Qr', None, profile.qr_pic)
                        print(statusAWS)
                        print(responseAWS)
                        if statusAWS == 200:
                            contact_dict['task']['qr_pic'] = responseAWS['results']
                        else:
                            contact_dict['task']['qr_pic'] = None 

                contact_dict.pop('sender_id')
                if initialContact.sender_hide is False:
                    sent_contacts.append(contact_dict)

            # check hide status and append if able
         
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
