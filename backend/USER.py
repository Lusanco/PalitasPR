from flask import jsonify, request
from routes import app_bp
from db_operations import DBOperations
from models import User


@app_bp.route('/users', methods=['GET'])
def get_users():
    user = DBOperations().filter({'User': {}})
    return jsonify (user)

@app_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = DBOperations().filter({'User': {'id': user_id}})
    if user:
        return jsonify (user)
    else:
        return jsonify ({'error': 'User not found'}), 404

@app_bp.route('/users', methods=['POST'])
def create_users():
    data = request.json
    if list(data.keys())[0] == 'User':
        data = data['User'].copy()
        new_user = DBOperations().sign_up(data)
    if new_user:
        return jsonify ({'message': 'User created successfully'}), 201
    else:
        return jsonify ({'error': 'Error creating user'}), 400

@app_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    DBOperations().login = (email, password)
    return jsonify ({"message": "Login attempted"}), 200

@app_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    user_data['id'] = user_id
    updated_user = DBOperations().update({'User': user_data})
    if updated_user:
        return jsonify ({'message': 'User updared successfully'})
    else:
        return jsonify ({'error': 'Error updating user'}), 400

@app_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_to_delete = DBOperations().delete('User', id=user_id)
    if user_to_delete:
        return jsonify ({'message': 'User deleted successufully'})
    else:
        return jsonify ({'error': 'Error deleting user'})

