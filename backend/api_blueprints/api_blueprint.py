from flask import Blueprint, jsonify, request, make_response, g, current_app
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from db.db_operations import DBOperations
from db.db_core import Db_core
import aws_bucket
from hashlib import md5

api_bp = Blueprint('api', __name__)


def make_cache_key():
    # Generate a cache key based on model and service without hashing
    key = f"search_storage"
    return key

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
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))
 
    # Use cache from current app
    cache = current_app.extensions['cache'][list(current_app.extensions['cache'].keys())[0]]

    if not cache.get('search_storage'):
        cache_key = make_cache_key()
    else:
        cache_key = 'search_storage'

    # Fetch cached data
    cache = current_app.extensions['cache'][list(current_app.extensions['cache'].keys())[0]]
    cached_data = cache.get(cache_key)
    print('OLD cached data')
    print(cached_data)
    if cached_data:
        # Compare cached model and service with current request parameters
        cached_model = cached_data['model']
        cached_service = cached_data['service']

        if cached_model != model or cached_service != service:
            print('DATA HAS CHANGED')
            page = 1
    print('My cache:')
    print(cache.get(cache_key))
    # Store the current model and service in the cache
    cache.set(cache_key, {'model': model, 'service': service}, timeout=300)
    cached_data = cache.get(cache_key)
    print('NEW cached data')
    print(cached_data)

    response, status = Db_core(g.db_session).landing_searchBar(model, service, town, page, limit)
    print(f"Response from landing_searchBar: {response}")
    if response['results'] is  None:
        return make_response(jsonify({'results': None}), 404)
    if status != 200:
        return make_response(jsonify(response), status)
    else:
        # empty list from query, return None and 404 
        if len(response['results']) == 0:
            return make_response(jsonify({'results': None}), 404)
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
        print('MY DATA')
        print(data)
        # Check validation errors:
        if 'request_id' not in data and 'promo_id' not in data:
            return make_response(jsonify({'error': 'Missing a key'}), 400)
        if not DBOperations(g.db_session).search('User', data['receiver_id']):
            return make_response(jsonify({'error': 'Receiver doesnt exist'}), 404)
        if 'promo_id' in data:
            if not DBOperations(g.db_session).search('Promotion', data['promo_id']):
                return make_response(jsonify({'error': 'Promotion doesnt exist'}), 404)
        else:
            if not DBOperations(g.db_session).search('Request', data['request_id']):
                return make_response(jsonify({'error': 'Request doesnt exist'}), 404)

        data['sender_id'] = current_user.id
        response, status = DBOperations(g.db_session).new({'Initial_Contact': data})
        if status != 201:
            return make_response(jsonify(response), status)
        g.db_session.commit()
        return make_response(jsonify({'results': 'ok'}), 201)

    if request.method == 'PUT':
        data = request.get_json()
        keys = ['receiver_id', 'sender_id','promo_id']
        for key in keys:
            if key in data:
                return make_response(jsonify({'error': 'Cannot update ilegal value'}), 400)

        response, status = DBOperations(g.db_session).update({'Initial_Contact': data})
        if status == 200:
            g.db_session.commit()
        return make_response(jsonify(response), status)
