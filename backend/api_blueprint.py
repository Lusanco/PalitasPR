from flask import Blueprint, jsonify, request, make_response, session
from db_operations import DBOperations
import emails
from flask_login import login_user, logout_user, login_required, current_user,LoginManager
from werkzeug.utils import secure_filename
import aws_bucket
api_bp = Blueprint('api', __name__)

@api_bp.before_request
def keep_session_alive():
    session.modified = True # Before requests, keep alive session if it hasnt expired

@api_bp.route("/verify_email/<token>", methods=["GET"])
def verify_email(token):
    if not token:
        return "Verification token is missing"

    response = emails.confirm_email(token)

    if not response:
        return "Invalid verification token or error"

    return "Email verification successful"


@api_bp.route('/explore', methods=['GET'])
def explore():
    """
        FRONT END send: {
            'model': <'Promotion'> or <'Request'>,
            'search': '<service_name>',
            'town' : <'town_name'> or <null>    
            }
    """
    model = request.args.get('model')
    service = request.args.get('search')
    town = request.args.get('town')
    search_results = DBOperations().filter(model, service, town)
    if search_results:
        return make_response(jsonify({'results': search_results}), 200)
    else:
        return make_response(jsonify({'message':"No Results"}), 404)
@api_bp.route("/logout")
@login_required
def logout():
    # Log out the current user
    logout_user()
    return 'Logged out'

@api_bp.route("/create_object", methods=["POST"])
def create_object():
    form_data = request.get_json()

    if (
        "first_name" in form_data
        and "last_name" in form_data
        and "email" in form_data
        and "password" in form_data
    ):
        user_data = {
            "first_name": form_data["first_name"],
            "last_name": form_data["last_name"],
            "email": form_data["email"],
            "password": form_data["password"],
        }
        new_obj = DBOperations().sign_up(user_data)
    else:
        new_obj = DBOperations().new(form_data)

    if new_obj:
        return {"response": "success"}
    else:
        pass
    return jsonify({"error": "Error creating a new object"})


@api_bp.route("/filter", methods=["POST"])
def search_filter():
    """
    Front has to send {'Service': {'name': 'Nails, 'town': 'Ponce'}}
    town is an optional argument for dict

    Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}

    example:
        filtered_objs = db.filter({'User': {'name': 'service_name', 'town': 'town_name'}})
    """
    data = request.json
    dictionary = DBOperations().filter(data)
    if dictionary:
        return jsonify(dictionary)
    else:
        return jsonify({"error": "Error filtering data"})


@api_bp.route('/login', methods=['GET'])
def login():
    email = request.args.get('af1')
    password = request.args.get('af2')
    response, status = DBOperations().login(email, password)
    print("After login response fetched")
    if status == 200:
        user = response['message']
        response['message'] = 'OK'
        login_user(user)
    return make_response(jsonify(response), status)

# @api_bp.route("/<class_name>/<id>", methods=["GET"])
# def search_object(class_name, id):

#     obj = DBOperations().search(class_name, id)
#     if obj:
#         # Convert the object to a dictionary
#         obj_dict = obj.__dict__
#         # Remove the '_sa_instance_state' key (SQLAlchemy internal state)
#         obj_dict.pop('_sa_instance_state', None)
#         return jsonify(obj_dict), 200
#     else:
#         return jsonify({"error": f"No {class_name} object found with ID {id}"}), 404



#--------------------------------------------------------------------------


@api_bp.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.get_json()

    if (
        "first_name" in form_data
        and "last_name" in form_data
        and "email" in form_data
        and "password" in form_data
    ):
        message, status = DBOperations().sign_up(form_data)
        return make_response(jsonify(message), status)
    else:
        return make_response(jsonify({'message': 'Missing a required field'}), 400)


@api_bp.route("/Promotion/<id>", methods=["GET"])
def show_promo(id):
    promo_obj = DBOperations().search('Promotion', id)
    if promo_obj:
        # obj_dict = promo_obj.all_columns()
        return jsonify(promo_obj), 200
    else:
        return jsonify({"error": f"No Promotion object found with ID {id}"}), 404

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

# pic route does put pictures in aws, furthing testing needed and we can use for other routes
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

@api_bp.route('/promotion-request/<id>', methods=['GET'])
@login_required
def promo_request(id=None):
    '''
        Route to get all promo and request posted by a user
    '''
    if current_user.id == id:
        # GET Method
        if request.method == 'GET':
            results = DBOperations().promo_request(id)
            return(make_response({'results': results}), 200) # 2 dicts, (<{promos}>, <{requests}>)

        # POST Method
        if request.method == 'POST':
            if not request.get_json():
                return (make_response({'message': 'No data received'}), 400)

            data = request.get_json()
            picture = request.files['image']

            # A): Picture upload only
            if ('model_id') in data and picture:
                model = data['model']
                model_id = ['model_id']
                pic_name = secure_filename(picture.filename)
                pic_bytes = picture.read()

                response = aws_bucket.put_picture(current_user.id, model, model_id, pic_name, pic_bytes)

                if response[1] == 200:
                    # Put pic name in database for the model column 'pictures'
                    response = DBOperations.update({model_id: {'pictures': pic_name}})

                    if response[1] == 200:
                        make_response({'message': 'ok'}, 200)
                    # Data Base error
                    else:
                        make_response({'message': 'error in database'}, 500)
                # AWS error
                else:
                    make_response(response)
            # B): Make new (promo or request), folder in aws made in DBOperations.new() and then upload pic
            if ('model_id') not in data and picture:
                pic_name = secure_filename(picture.filename)
                pic_bytes = picture.read()
                model = data['model']
                data.pop('model')
                newModel = DBOperations().new({model: data}) # Data should be a dictionary

                response = aws_bucket.put_picture(current_user.id, model, newModel.id, pic_name, pic_bytes)

                if response[1] == 200: # OK, procceed to put name of pic in database for the <promo> or <request>
                    response = DBOperations.update({newModel.id: {'pictures': pic_name}})

                    if response[1] == 200:
                        return(make_response({'message': 'ok'}, 200))
                    # error from DBOperations
                    else:
                        return make_response(response) # Fail error
                # error from aws bucket
                else:
                    return make_response(response) # Fail error

            # C) Make folder only
            if ('model_id') not in data and not picture:
                print('Make logic for creating folder only')
    else:
        return(make_response({'message': 'Acces denied'}), 403)

# @api_bp.route("/Promotion", methods=["GET"])
# def get_all_promotion():
#     """
#     comment
#     """
#     promotions = DBOperations().search_all_objects()
#     promotions_dicts = []

#     for promo in promotions:
#         promo_dict = promo.all_columns()
#         promotions_dicts.append(promo_dict)
#         return jsonify(promotions_dicts), 200

