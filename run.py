#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.base_model import Base
from backend.models import Service, User
from backend.db_operations import DBOperations   # Import the method for creating new objects

# Create Flask app instance
app = Flask(__name__)

# Create the engine
engine = create_engine('postgresql://postgres:9150@localhost/postgres')

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
    """
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
    Session = sessionmaker(bind=engine)
    session = Session()
    
    services = session.query(Service).all()

    # Retrieve all the columns for each object and the values
    serialized_services = [service.all_columns() for service in services]
    
    # Close the session to release resources
    session.close()
    
    return jsonify(serialized_services)

@app.route('/create_object', methods=['POST'])  # Route to create new objects
def create_object():
    data = request.json  # Assuming you're sending JSON data with necessary information
    DBOperations.new(data)  # Call the method to create new objects
    return jsonify({'message': 'Object created successfully'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)