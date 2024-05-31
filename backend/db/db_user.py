'''
    All related functions for user class that involves the database
    and routes from flask
'''
from emails import send_confirm_email
from email_validator import validate_email, EmailNotValidError
from db_init import get_session
import bcrypt
from models import User


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
        response, status = self.new({"User": dict_of_user})
        return response, status