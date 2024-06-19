from flask import Blueprint, jsonify, request, make_response
from flask_login import current_user, login_required
from db.db_operations import DBOperations
from db.db_core import Db_core
from db.db_initial_contact import Db_initial_contact
from werkzeug.utils import secure_filename
import aws_bucket
import shlex
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
    response, status = Db_core().landing_searchBar(model, service, town)
    if status != 200:
        return make_response(jsonify(response), status)
    else:
        # empty list from query, return None and 404 
        if len(response['results']) == 0:
            response['results'] = None
            status = 404
        # Get first picture name to fetch from aws
        for model in response['results']:
            if model['pictures']:
                pic_names = model['pictures']
                if 'promo_id' in model:
                    modelFolder = 'Promotion'
                    model_id = model['promo_id']
                else:
                    modelFolder = 'Request'
                    model_id = model['request_id']
                # Serve only one picture as thumbnail
                pic1, separator, pic2 = pic_names.partition('|')
                responseAWS, statusAWS = aws_bucket.get_picture(model['user_id'], modelFolder, model_id, pic1)
                if statusAWS == 200:
                    # put url into the pictures column of the model
                    urlPic = responseAWS['results']
                    model['pictures'] = urlPic
                else:
                    model['pictures'] = None

        return make_response(jsonify(response), status)


@api_bp.route("/promotion/<id>", methods=["GET"])
def show_promo(id):
    promo = DBOperations().search('Promotion', id)
    if promo:
        promo_dict = {}
        promo_dict.update(promo.all_columns())
        promo_dict['first_name'] = promo.user.first_name
        promo_dict['last_name'] = promo.user.last_name
        picNames = promo_dict['pictures']
        promo_id = promo_dict['promo_id']
        user_id = promo_dict['user_id']
        
        # Iterate all pic names to get them from aws
        if promo_dict['pictures']:
            urls = []
            loop = True
            while loop:
                pic, seperator, pics = picNames.partition('|')
                responseAWS, statusAWS = aws_bucket.get_picture(user_id, 'Promotion', promo_id, pic)
                if statusAWS == 200:
                    # put url into the pictures column of the model
                    urlPic = responseAWS['results']
                    urls.append(urlPic)
                if not pics:
                    loop = False
                else:
                    pic = pics

        promo_dict['pictures'] = urls
        return make_response(jsonify({'results': promo_dict}), 200)
    else:
        return make_response(jsonify({"error": f"No Promotion object found with ID {id}"}), 404)

@api_bp.route("/request/<id>", methods=["GET"])
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

@api_bp.route('/initial-contact', methods=['POST'])
@login_required
def send_contact():
    '''
        Create initial-contact message
    '''
    data = request.get_json()
    if 'receiver_id' not in data or 'promo_id' not in data:
        return make_response(jsonify({'error': 'Missing a key'}), 400)
    if not DBOperations().search('User', data['receiver_id']):
        return make_response(jsonify({'error': 'Receiver doesnt exist'}), 404)
    if not DBOperations().search('Promotion', data['promo_id']):
        return make_response(jsonify({'error': 'Promotion doesnt exist'}), 404)
    data['sender_id'] = current_user.id
    response, status = DBOperations().new({'Initial_Contact': data})
    if status != 201:
        return make_response(jsonify(response), status)
    return make_response(jsonify({'results': 'ok'}), 201)
