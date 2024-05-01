#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_model import Base, BaseModel
from models import Service, User
from db_operations import DBOperations  # Import the method for creating new objects
from routes import app_bp
from flask_mail import Mail, Message
import secrets
from emails import confirm_email


# Create Flask app instance
app = Flask(__name__)
# Configure Flask app for sending emails using Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "antoniofdjs@gmail.com"
app.config["MAIL_PASSWORD"] = "syhk sijd eoli tgba"
app.register_blueprint(app_bp)
mail = Mail(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
CORS(app)

# Create the engine
engine = create_engine(
    "postgresql://demo_dev:demo_dev_pwd@demodb.ctossyay6vcz.us-east-2.rds.amazonaws.com/postgres"
)

# Bind the engine to the Base class
Base.metadata.bind = engine


# @app.route('/create_object', methods=['POST'])
# def create_object():
#     data = request.json # data = {"User": {"first_name": "John", "last_name": "Doe"}}

#     # If user is signing up
#     if list(data.keys())[0] == 'User':
#         data = data['User'].copy()
#         new_obj = DBOperations().sign_up(data)

#     else:
#         new_obj = DBOperations().new(data)

#     # Check if object was created
#     if new_obj:
#         return render_template("login.html")
#         return jsonify({'message': f'{type(new_obj).__name__} created successfully'}), 201
#     else:
#         return jsonify({'error': 'Error creating object'}), 400


# VERIFY EMAIL ROUTE
@app.route("/verify_email/<token>", methods=["GET"])
def verify_email(token):

    if not token:
        return "Verification token is missing"

    verified = confirm_email(token)

    if not verified:
        return "Invalid verification token"

    return "Email verification successful"


# # Define route to serve the index.html page
# @app.route("/")
# def index():
#     return render_template("index.html")


@app.route("/")
def index():
    # Serve the built index.html from the frontend directory
    # return serve_static("index.html")
    return app.send_static_file("index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    """Serves static files from the configured static directory, or returns a 404 for unmatched files."""
    try:
        return app.send_static_file(filename)
    except FileNotFoundError:
        # Handle non-existent files gracefully
        return "File not found", 404


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/signup")
def signup_page():
    return render_template("signup.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    DBOperations().login(email, password)
    response_html = render_template("login_response.html")
    return response_html


@app.route("/api/create_object", methods=["POST"])
def create_object():
    form_data = request.get_json()

    # If user is signing up
    if (
        "first_name" in form_data
        and "last_name" in form_data
        and "email" in form_data
        and "password" in form_data
    ):
        user_data = {
            "first_name": form_data["first_name"],
            "last_name": form_data["last_name"],
            "email": form_data["email"],
            "password": form_data["password"],
        }
        new_obj = DBOperations().sign_up(user_data)
    else:
        new_obj = DBOperations().new(form_data)

    # Check if object was created
    if new_obj:
        return
    else:
        pass
        # return render_template("error.html", error="Error creating object"), 400
    return


@app.route("/api/filter", methods=["POST"])
def search_filter():
    """
    Front has to send {'Service': {'name': 'Nails, 'town': 'Ponce'}}
    town is an optional argument for dict

    Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}

    example:
        filtered_objs = db.filter({'User': {'name': 'service_name', 'town': 'town_name'}})
    """
    data = request.json
    dictionary = DBOperations().filter(data)
    print(data)
    print(1, dictionary)

    if dictionary:
        return jsonify(dictionary)
        print(2, dictionary)
    else:
        return jsonify({"error": "Error filtering data"})
    print(3, dictionary)


# @app.route('/update', methods=['POST'])
# def updates():
#     """
#         Usage: {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}
#         This will update the specified object with the values you want to change
#         Example: {'User_id': {'last_name': 'Santiago', 'email': 'watagata@gmail.com'}}
#     """
#     data = request.json
#     obj_to_update = DBOperations().update(data)
#     return jsonify(obj_to_update)

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data.get("email")
#     password = data.get("password")
#     DBOperations().login = (email, password)
#     return jsonify ({"message": "Login attempted"}), 200

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
