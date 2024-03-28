#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

# main_app.py

from flask import Flask, jsonify, render_template, request
from backend import Session
from backend.models import Service, User
from backend.db_operations import DBoperations

# Create Flask app instance
app = Flask(__name__)

# Define route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Routes for API
@app.route('/users')
def all_users():
    """
    Return all Users in DB to frontend
    """
    session = Session()

    users = session.query(User).all()

    # Retrieve all the columns for each object and the values
    serialized_users = [user.all_columns() for user in users]

    # Close the session to release resources
    session.close()

    return jsonify(serialized_users)

@app.route('/services')
def all_services():
    """
    Return all services in DB to frontend
    """
    session = Session()

    services = session.query(Service).all()

    # Retrieve all the columns for each object and the values
    serialized_services = [service.all_columns() for service in services]

    # Close the session to release resources
    session.close()

    return jsonify(serialized_services)

@app.route('/create_object', methods=['POST'])
def create_object():
    data = request.json
    DBoperations.new(data)
    return jsonify({'message': 'Object created successfully'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
