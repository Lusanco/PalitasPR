from flask import Blueprint, jsonify, request, make_response
from flask_login import current_user, login_required
from db.db_operations import DBOperations
from db.db_core import Db_core
from db.db_initial_contact import Db_initial_contact
from werkzeug.utils import secure_filename
import aws_bucket

api_bp = Blueprint('api', __name__)

@api_bp.route('/explore', methods=['GET'])
def explore():
    """
        Return al promotions or requests from a specific service
        searched in the landing search bar.
        Filtered also by towns.
    """
    model = request.args.get('model')
    service = request.args.get('search')
    town = request.args.get('town')
    search_results = Db_core().landing_searchBar(model, service, town)
    if search_results:
        return make_response(jsonify({'results': search_results}), 200)
    else:
        return make_response(jsonify({'message':"No Results"}), 404)


@api_bp.route("/Promotion/<id>", methods=["GET"])
def show_promo(id):
    promo = DBOperations().search('Promotion', id)
    if promo:
        promo_dict = {}
        promo_dict.update(promo.all_columns())
        promo_dict['first_name'] = promo.user.first_name
        promo_dict['last_name'] = promo.user.last_name

        return make_response(jsonify({'results': promo_dict}), 200)
    else:
        return make_response(jsonify({"error": f"No Promotion object found with ID {id}"}), 404)


@api_bp.route("/Request/<id>", methods=["GET"])
def show_request(id):
    request_obj = DBOperations().search('Request', id)
    if request_obj:
        return jsonify(request_obj), 200
    else:
        return jsonify({"error": f"No Request object found with ID {id}"}), 404

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

@api_bp.route('initial-contact', methods=['POST'])
@login_required
def send_contact():
    data = {
        'receiver_id': '<RECEIVER USER ID>',
        'sender_id': current_user.id,
        'promo_id': '<PROMOTION ID>'
        }

    if not DBOperations().search('User', data['receiver_id']):
        return make_response(jsonify({'error': 'Receiver doesnt exist'}), 404)
    if not DBOperations().search('Promotion', data['promo_id']):
        return make_response(jsonify({'error': 'Promotion doesnt exist'}), 404)

    response, status = DBOperations().new({'Initial_contact': data})
    return response, status
