#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_model import Base, BaseModel
from models import Service, User
from db_operations import DBOperations   # Import the method for creating new objects


# Create Flask app instance
app = Flask(__name__)
CORS(app)

# Create the engine
engine = create_engine('postgresql://postgres:9495@localhost/postgres')

# Bind the engine to the Base class
Base.metadata.bind = engine

# Define route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')  # API??? FRONTEND CAN CALL THIS
def all_users():
    """
        Return all Users in DB to frontend

        This function retrieves all users from the database and returns them to the frontend.
        It accepts optional query parameters to filter the users. If no parameters are provided,
        it fetches all users. It then serializes the user objects and returns them as JSON.
        Ensure that request and jsonify are imported from Flask.
    """

    query_params = request.args

    if query_params:
        # Filter users based on query parameters
        users = DBOperations().filter('User', **query_params)
        serialized_users = users
    else:
        Session = sessionmaker(bind=engine)
        session = Session()
        
        users = session.query(User).all()

        # Retrieve all the columns for each object and the values
        serialized_users = [user.all_columns() for user in users]

        # Close the session to release resources
        session.close()
    
    return jsonify(serialized_users)

@app.route('/services') # API??? FRONTEND CAN CALL THIS
def all_services():
    """
        Return all services in DB to frontend
    """
    query_params = request.args

    if query_params:
        # Filter services based on query parameters
        services = DBOperations().filter('Service', **query_params)
        serialized_services = services
    else:
        Session = sessionmaker(bind=engine)
        session = Session()
        
        services = session.query(Service).all()

        # Retrieve all the columns for each object and the values
        serialized_services = [service.all_columns() for service in services]
        
        # Close the session to release resources
        session.close()
    
    return jsonify(serialized_services)

@app.route('/create_object', methods=['POST'])
def create_object():
    data = request.json # data = {"User": {"first_name": "John", "last_name": "Doe"}}
    new_obj = DBOperations().new(data)

    if new_obj:
        return jsonify({'message': f'{type(new_obj).__name__} created successfully'}), 201
    else:
        return jsonify({'error': 'Error creating object'}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)