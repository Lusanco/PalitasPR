from flask import jsonify, request
from routes import app_bp
from db_operations import DBOperations
from models import Town


@app_bp.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = DBOperations().filter({'Review': {}})
    return jsonify(reviews)

@app_bp.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = DBOperations().filter({'Review': {'id': review_id}})
    if review:
        return jsonify(review)
    else:
        return jsonify({'error': 'Review not found'}), 404

@app_bp.route('/reviews', methods=['POST'])
def create_review():
    review_data = request.json
    new_review = DBOperations().new(review_data)
    if new_review:
        return jsonify ({'message': 'Review created successfully'}), 201
    else:
        return jsonify ({'error': 'Error creating review'}), 400

@app_bp.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    review_data = request.json
    review_data['id'] = review_id
    updated_review = DBOperations().update({'Review': review_data})
    if updated_review:
        return jsonify ({'message': 'Review updated successfully'})
    else:
        return jsonify ({'error': 'Error updating review'}), 400

@app_bp.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review_to_delete = DBOperations().delete('Review', id=review_id)
    if review_to_delete:
        return jsonify ({'message': 'Review deleted successufully'})
    else:
        return jsonify ({'error': 'Error deleting review'}), 400

