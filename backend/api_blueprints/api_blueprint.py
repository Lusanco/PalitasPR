from flask import Blueprint, jsonify, request, make_response, g
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from db.db_operations import DBOperations
from db.db_core import Db_core
import aws_bucket
import asyncio

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
    response, status = Db_core(g.db_session).landing_searchBar(model, service, town)
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
    promo = DBOperations(g.db_session).search('Promotion', id)
    if promo:
        promo_dict = {}
        promo_dict.update(promo.all_columns())
        promo_dict['first_name'] = promo.user.first_name
        promo_dict['last_name'] = promo.user.last_name
        picNames = promo_dict['pictures']
        promo_id = promo_dict['id']
        user_id = promo_dict['user_id']
        urls = []
        # Get all pic names
        if promo_dict['pictures']:
            pic_list = picNames.split('|')

            async def handler_getPictures(pic_list, user_id, promo_id):
                tasks = []

                for pic in pic_list:
                    task = asyncio.create_task(aws_bucket.get_picture_async(user_id, 'Promotion', promo_id, pic))
                    tasks.append(task)
                awsResults = await asyncio.gather(*tasks)
                urls = [response[0]['results'] for response in awsResults if response[1] == 200]
                if not urls:
                    urls = []
                return urls

            urls = asyncio.run(handler_getPictures(pic_list, user_id, promo_id))

        if len(urls) == 0:
            urls == None 

        promo_dict['pictures'] = urls
        return make_response(jsonify({'results': promo_dict}), 200)
    else:
        return make_response(jsonify({"error": f"No Promotion object found with ID {id}"}), 404)

@api_bp.route("/request/<id>", methods=["GET"])
def show_request(id):
    request = DBOperations(g.db_session).search('Request', id)
    if request:
        request_dict = {}
        request_dict.update(request.all_columns())
        request_dict['first_name'] = request.user.first_name
        request_dict['last_name'] = request.user.last_name
        picNames = request_dict['pictures']
        request_id = request_dict['id']
        user_id = request_dict['user_id']
        urls = []
        # Get all pic names
        if request_dict['pictures']:
            pic_list = picNames.split('|')

            async def handler_getPictures(pic_list, user_id, request_id):
                tasks = []

                for pic in pic_list:
                    task = asyncio.create_task(aws_bucket.get_picture_async(user_id, 'Request', request_id, pic))
                    tasks.append(task)
                awsResults = await asyncio.gather(*tasks)
                urls = [response[0]['results'] for response in awsResults if response[1] == 200]
                if not urls:
                    urls = []
                return urls

            urls = asyncio.run(handler_getPictures(pic_list, user_id, request_id))

        if len(urls) == 0:
            urls == None 

        request_dict['pictures'] = urls
        return make_response(jsonify({'results': request_dict}), 200)
    else:
        return make_response(jsonify({"error": f"No Request object found with ID {id}"}), 404)


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

@api_bp.route('/initial-contact', methods=['POST', 'PUT'])
@login_required
def send_contact():
    '''
        Create initial-contact message
    '''
    if request.method == 'POST':
        data = request.get_json()
        if 'receiver_id' not in data or 'promo_id' not in data:
            return make_response(jsonify({'error': 'Missing a key'}), 400)
        if not DBOperations(g.db_session).search('User', data['receiver_id']):
            return make_response(jsonify({'error': 'Receiver doesnt exist'}), 404)
        if not DBOperations(g.db_session).search('Promotion', data['promo_id']):
            return make_response(jsonify({'error': 'Promotion doesnt exist'}), 404)
        
        data['sender_id'] = current_user.id
        response, status = DBOperations(g.db_session).new({'Initial_Contact': data})
        if status != 201:
            return make_response(jsonify(response), status)
        return make_response(jsonify({'results': 'ok'}), 201)
    
    if request.method == 'PUT':
        data = request.get_json()
        keys = ['receiver_id', 'sender_id','promo_id']
        for key in keys:
            if key in data:
                return make_response(jsonify({'error': 'Cannot update ilegal value'}), 400)

        response, status = DBOperations(g.db_session).update({'Initial_Contact': data})
        return make_response(jsonify(response), status)
