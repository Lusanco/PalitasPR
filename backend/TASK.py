from flask import jsonify, request
from routes import app_bp
from db_operations import DBOperations
from models import Town


@app_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = DBOperations().filter({'Task': {}})
    return jsonify(tasks)

@app_bp.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = DBOperations().filter({'Task': {'id': task_id}})
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app_bp.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.json
    new_task = DBOperations().new(task_data)
    if new_task:
        return jsonify ({'message': 'Task created successfully'}), 201
    else:
        return jsonify ({'error': 'Error creating task'}), 400

@app_bp.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    task_data = request.json
    task_data['id'] = task_id
    updated_task = DBOperations().update({'Task': task_data})
    if updated_task:
        return jsonify ({'message': 'Task updated successfully'})
    else:
        return jsonify ({'error': 'Error updating task'}), 400

@app_bp.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_to_delete = DBOperations().delete('Task', id=task_id)
    if task_to_delete:
        return jsonify ({'message': 'Task deleted successufully'})
    else:
        return jsonify ({'error': 'Error deleting task'}), 400

