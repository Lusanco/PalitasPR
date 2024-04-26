from flask import jsonify, request
from routes import app_bp
from db_operations import DBOperations
from models import Service


@app_bp.route('/user_service_assocs', methods=['GET'])
def get_user_service_assocs():
    user_service_assocs = DBOperations().filter({'UserServiceAssoc': {}})
    return jsonify(user_service_assocs)

@app_bp.route('/user_service_assocs/<assoc_id>', methods=['GET'])
def get_user_service_assoc(assoc_id):
    user_service_assoc = DBOperations().filter({'UserServiceAssoc': {'id': assoc_id}})
    if user_service_assoc:
        return jsonify(user_service_assoc)
    else:
        return jsonify({'error': 'UserServiceAssoc not found'}), 404

@app_bp.route('/user_service_assocs', methods=['POST'])
def create_usa():
    data = request.json
    result = DBOperations().new(data)
    if result:
        return jsonify ({'message': 'Result created successfully'}), 201
    else:
        return jsonify ({'error': 'Error creating result'}), 400

@app_bp.route('/user_service_assocs/<assoc_id>', methods=['PUT'])
def update_usa(service_id):
    data = request.json
    data['id'] = service_id
    result = DBOperations().update({'Service': data})
    if result:
        return jsonify ({'message': 'Result updated successfully'})
    else:
        return jsonify ({'error': 'Error updating result'}), 400

@app_bp.route('/user_service_assocs/<assoc_id>', methods=['DELETE'])
def delete_usa(assocs_id):
    data = DBOperations().delete('Service', id=assocs_id)
    if data:
        return jsonify ({'message': 'Service deleted successufully'})
    else:
        return jsonify ({'error': 'Error deleting service'}), 400

