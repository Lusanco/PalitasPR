from flask import jsonify, request
from routes import app_bp
from db_operations import DBOperations
from models import Service


@app_bp.route('/services', methods=['GET'])
def get_services():
    services = DBOperations().filter({'Service': {}})
    return jsonify(services)

@app_bp.route('/services/<service_id>', methods=['GET'])
def get_service(service_id):
    service = DBOperations().filter({'Service': {'id': service_id}})
    if service:
        return jsonify(service)
    else:
        return jsonify({'error': 'Service not found'}), 404

@app_bp.route('/services', methods=['POST'])
def create_services():
    service_data = request.json
    new_service = DBOperations().new(service_data)
    if new_service:
        return jsonify ({'message': 'Service created successfully'}), 201
    else:
        return jsonify ({'error': 'Error creating service'}), 400

@app_bp.route('/services/<service_id>', methods=['PUT'])
def update_service(service_id):
    service_data = request.json
    service_data['id'] = service_id
    updated_service = DBOperations().update({'Service': service_data})
    if updated_service:
        return jsonify ({'message': 'Service updated successfully'})
    else:
        return jsonify ({'error': 'Error updating service'}), 400

@app_bp.route('/service/<service_id>', methods=['DELETE'])
def delete_service(service_id):
    service_to_delete = DBOperations().delete('Service', id=service_id)
    if service_to_delete:
        return jsonify ({'message': 'Service deleted successufully'})
    else:
        return jsonify ({'error': 'Error deleting service'}), 400

