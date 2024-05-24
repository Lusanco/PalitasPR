from flask import Blueprint, jsonify, request, make_response, session
from db_operations import DBOperations
import emails
from flask_login import login_user, logout_user, login_required, current_user,LoginManager
from werkzeug.utils import secure_filename
import aws_bucket
my_bp = Blueprint('my', __name__)

@my_bp.before_request
def keep_session_alive():
    session.modified = True # Before requests, keep alive session if it hasnt expired

@my_bp.route('/promotion-request', methods=['GET'])
@login_required
def promo_request():
    '''
        Route to get all promo and request posted by a user
    '''
    # GET Method
    if request.method == 'GET':
        results = DBOperations().promo_request(current_user.id)
        return(make_response({'results': results}), 200) # 2 dicts, (<{promos}>, <{requests}>)


@my_bp.route('/promotion-request', methods=['POST'])
@login_required
def promo_request():
    '''
        Route to get all promo and request posted by a user
    '''
    frontend_data= {
        'user_id': current_user.id,
        'model': 'Promotion',
        'service_id': 8, # Plumbing
        'title': 'NEW PLUMBING SERVICE',
        'description': 'New specials for our new customers up to $50 discounts',
        'price_min': 40,
        'price_max': 120,
        'towns': [22, 23]
        }
    model = frontend_data.get('model')
    frontend_data.pop('model')

    newObject = DBOperations().new({model:frontend_data})

    if newObject[1] == 201: # (object, statusCode)
        return make_response({'results': 'ok'}, 201)
    else:
        return make_response({'error': newObject[0]}, 500)


    # # GET Method
    # if request.method == 'GET':
    #     results = DBOperations().promo_request(current_user.id)
    #     return(make_response({'results': results}), 200) # 2 dicts, (<{promos}>, <{requests}>)

    # POST Method
    # if request.method == 'POST':
    #     if not request.get_json():
    #         return (make_response({'message': 'No data received'}), 400)

    #     data = request.get_json()
    #     picture = request.files['image']

    #     # A): Picture upload only
    #     if ('model_id') in data and picture:
    #         model = data['model']
    #         model_id = ['model_id']
    #         pic_name = secure_filename(picture.filename)
    #         pic_bytes = picture.read()

    #         response = aws_bucket.put_picture(current_user.id, model, model_id, pic_name, pic_bytes)

    #         if response[1] == 200:
    #             # Put pic name in database for the model column 'pictures'
    #             response = DBOperations.update({model_id: {'pictures': pic_name}})

    #             if response[1] == 200:
    #                 make_response({'message': 'ok'}, 200)
    #             # Data Base error
    #             else:
    #                 make_response({'message': 'error in database'}, 500)
    #         # AWS error
    #         else:
    #             make_response(response)
    #     # B): Make new (promo or request), folder in aws made in DBOperations.new() and then upload pic
    #     if ('model_id') not in data and picture:
    #         pic_name = secure_filename(picture.filename)
    #         pic_bytes = picture.read()
    #         model = data['model']
    #         data.pop('model')
    #         newModel = DBOperations().new({model: data}) # Data should be a dictionary

    #         response = aws_bucket.put_picture(current_user.id, model, newModel.id, pic_name, pic_bytes)

    #         if response[1] == 200: # OK, procceed to put name of pic in database for the <promo> or <request>
    #             response = DBOperations.update({newModel.id: {'pictures': pic_name}})

    #             if response[1] == 200:
    #                 return(make_response({'message': 'ok'}, 200))
    #             # error from DBOperations
    #             else:
    #                 return make_response(response) # Fail error
    #         # error from aws bucket
    #         else:
    #             return make_response(response) # Fail error

        # C) Make folder only
        # if ('model_id') not in data and not picture:
