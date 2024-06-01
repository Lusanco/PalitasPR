from flask import Blueprint, jsonify, request, make_response
from db.db_operations import DBOperations
from werkzeug.utils import secure_filename
import aws_bucket

api_bp = Blueprint('api', __name__)

@api_bp.route('/explore', methods=['GET'])
def explore():
    """
        Return al promotions or requests from a specific service
        searched in the main search bar.
        Filtered also by towns.
    """
    model = request.args.get('model')
    service = request.args.get('search')
    town = request.args.get('town')
    search_results = DBOperations().filter(model, service, town)
    if search_results:
        return make_response(jsonify({'results': search_results}), 200)
    else:
        return make_response(jsonify({'message':"No Results"}), 404)


@api_bp.route("/Promotion/<id>", methods=["GET"])
def show_promo(id):
    promo_obj = DBOperations().search('Promotion', id)
    if promo_obj:
        obj_dict = promo_obj.all_columns()
        return make_response(jsonify({'results': obj_dict}), 200)
    else:
        return make_response(jsonify({"error": f"No Promotion object found with ID {id}"}), 404)


@api_bp.route("/Request/<id>", methods=["GET"])
def show_request(id):
    request_obj = DBOperations().search('Request', id)
    if request_obj:
        return jsonify(request_obj), 200
    else:
        return jsonify({"error": f"No Request object found with ID {id}"}), 404


@api_bp.route("/Review/<id>", methods=["GET"])
def show_review(id):
    review_obj = DBOperations().search('Review', id)
    if review_obj:
        return jsonify(review_obj), 200
    else:
        return jsonify({"error": f"No Review object found with ID {id}"}), 404


@api_bp.route('/pic', methods=['POST'])
def put_pic():    
    print("Pic ROUTE ACTIVATED")
    if 'image' not in request.files:
        return make_response({'message': 'No file part'}, 400)
        
    file = request.files['image']
    print(file)
    if file.filename == '':
        return make_response({'message': 'No selected file'}, 400)
        
    if file:
        filename = secure_filename(file.filename)  # Secure the filename
        content = file.read()
        print('My content: ')
        print(content)
        response = aws_bucket.put_picture('007', 'Promotion', '005', filename, content)
        return make_response(response)
