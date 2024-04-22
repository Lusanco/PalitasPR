from flask import jsonify, request
from routes import app_bp
from db_operations import DBOperations
from models import Town


@app_bp.route('/towns', methods=['GET'])
def get_towns():
    towns = DBOperations.filter({'Town': {}})
    return jsonify(towns)

@app_bp.route('/towns/<town_id>', methods=['GET'])
def get_town(town_id):
    town = DBOperations.filter({'Town': {'id': town_id}})
    if town:
        return jsonify(town)
    else:
        return jsonify({'error': 'Town not found'}), 404

@app_bp.route('/towns', methods=['POST'])
def create_town():
    town_data = request.json
    new_town = DBOperations().new(town_data)
    if new_town:
        return jsonify ({'message': 'Town created successfully'}), 201
    else:
        return jsonify ({'error': 'Error creating town'}), 400

@app_bp.route('/towns/<town_id>', methods=['PUT'])
def update_town(town_id):
    town_data = request.json
    town_data['id'] = town_id
    updated_town = DBOperations().update({'Town': town_data})
    if updated_town:
        return jsonify ({'message': 'Town updated successfully'})
    else:
        return jsonify ({'error': 'Error updating town'}), 400

@app_bp.route('/towns/<town_id>', methods=['DELETE'])
def delete_town(town_id):
    town_to_delete = DBOperations().delete('Town', id=town_id)
    if town_to_delete:
        return jsonify ({'message': 'Town deleted successufully'})
    else:
        return jsonify ({'error': 'Error deleting town'}), 400

