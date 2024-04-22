#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_model import Base, BaseModel
from models import Service, User
from db_operations import DBOperations   # Import the method for creating new objects
from routes import app_bp


# Create Flask app instance
app = Flask(__name__)
app.register_blueprint(app_bp)
# login_manager = LoginManager()
# login_manager.init_app(app)
CORS(app)

# Create the engine
engine = create_engine('postgresql://demo_dev:demo_dev_pwd@localhost/demo_db')

# Bind the engine to the Base class
Base.metadata.bind = engine

# Define route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')


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
#         return jsonify({'message': f'{type(new_obj).__name__} created successfully'}), 201
#     else:
#         return jsonify({'error': 'Error creating object'}), 400

# @app.route('/filter', methods=['POST'])
# def search_filter():
#     """
#         Front has to send {'Service': {'name': 'Nails, 'town': 'Ponce'}}
#         town is an optional argument for dict

#         Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}

#         example:
#             filtered_objs = db.filter({'User': {'name': 'service_name', 'town': 'town_name'}})
#     """
#     data = request.json
#     dictionary = DBOperations().filter(data)

#     if dictionary:
#         return jsonify(dictionary)
#     else:
#         return jsonify({'error': 'Error filtering data'})

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
if __name__ == '__main__':
    app.run(debug=True)