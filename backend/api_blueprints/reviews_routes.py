from flask import Blueprint, jsonify, request, make_response, session, g
from db.db_operations import DBOperations
from flask_login import login_required, current_user
from db.db_review import Db_review
review_bp = Blueprint('reviews', __name__)

@review_bp.before_request
def keep_session_alive():
    session.modified = True

@review_bp.route("/", methods=["GET", "POST", "PUT"])
@login_required
def review_crud():
    '''
        Review route CRUD methods
    '''
    metodo = 'GET'
    if metodo == 'GET':
        print('Inside GET reviews')
        reviews_list = Db_review(g.db_session).get_all_reviews()
        if not reviews_list:
            return make_response(jsonify({'results': None}), 200)
        return make_response(jsonify({'results': reviews_list}), 200)
    if request.method == 'POST':
        data = request.get_json()
        data['user_id'] = current_user.id # Reviewer
        keys = [
            'description',
            'rating',
            'task_id',
            ]
        for key in keys:
            if key not in data:
                return make_response(jsonify({'error': f"Missing key: {key}"}), 400)

        # Check if task has no review and task status is closed
        review = Db_review(g.db_session).get_review_by_TaskID(data['task_id'])
        if review:
            return make_response(jsonify({'error': f"A review has already been made for the task {data['task_id']}"}))
        task = DBOperations(g.db_session).search('Task', data['task_id'])
        if not task:
            return make_response(jsonify({'error': f"No task found: {data['task_id']}"}), 400)
        if task.status == 'closed':
            return make_response(jsonify({'error': f"Task status is not closed: -{task.status}-"}), 400)

        # Create Review
        response, status = DBOperations(g.db_session).new({'Review': {data}})
        if status != 201:
            return make_response(jsonify(response), status)
        g.db_session.commit()
        return make_response(jsonify({'results': 'ok'}), 201)