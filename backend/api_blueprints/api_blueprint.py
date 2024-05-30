from flask import Blueprint, jsonify, request, make_response, session
from db_operations import DBOperations
import emails
from flask_login import login_user, logout_user, login_required, current_user,LoginManager
from werkzeug.utils import secure_filename
import aws_bucket
from db_init import get_session

api_bp = Blueprint('api', __name__)

@api_bp.before_request
def keep_session_alive():
    session.modified = True # Before requests, keep alive session if it hasnt expired

@api_bp.route("/verify_email/<token>", methods=["GET"])
def verify_email(token):
    if not token:
        return make_response(jsonify({'error':'Verification token is missing'}), 400)

    response, status = emails.confirm_email(token)
    return(make_response(jsonify(response)), status)

@api_bp.route('/explore', methods=['GET'])
def explore():
    """
        FRONT END send: {
            'model': <'Promotion'> or <'Request'>,
            'search': '<service_name>',
            'town' : <'town_name'> or <null>    
            }
    """
    session = get_session()
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
    # session = get_session()
    # Log out the current user
    logout_user()
    return make_response(jsonify({'results':'Logged out'}), 200)

@api_bp.route("/filter", methods=["POST"])
def search_filter():
    """
    Front has to send {'Service': {'name': 'Nails, 'town': 'Ponce'}}
    town is an optional argument for dict

    Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}

    example:
        filtered_objs = db.filter({'User': {'name': 'service_name', 'town': 'town_name'}})
    """
    # session = get_session()
    data = request.json
    dictionary = DBOperations().filter(data)
    if dictionary:
        return jsonify(dictionary)
    else:
        return jsonify({"error": "Error filtering data"})


@api_bp.route('/login', methods=['GET'])
def login():
    # session = get_session()
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
    # session = get_session()
    form_data = request.get_json()

    if (
        "first_name" in form_data
        and "last_name" in form_data
        and "email" in form_data
        and "password" in form_data
    ):
        response, status = DBOperations().sign_up(form_data)

        if status != 201:
            return make_response(jsonify(response), status)

        return make_response(jsonify({"results": "ok"}), status)
    else:
        return make_response(jsonify({'message': 'Missing a required field'}), 400)


@api_bp.route("/Promotion/<id>", methods=["GET"])
def show_promo(id):
    # session = get_session()
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