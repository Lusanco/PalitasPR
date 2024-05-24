from flask import Blueprint, jsonify, request, render_template, make_response, session
from db_operations import DBOperations
from emails import confirm_email
import emails
import uuid
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from user_activity import update_last_activity
import logging



api_bp = Blueprint('api', __name__)


session_expired = False  # Flag to track session expiration


@api_bp.before_request
def check_session_expiration():
    if current_user.is_authenticated:
        if session.get('user_id') != current_user.id:
            # If session user_id does not match the current user's ID, assume session expired
            logout_user()  # Log out the current user
            print("Logged out")
            return jsonify({"message": "Session Expired"}), 401
    elif request.endpoint not in ['login', 'static', None]:
        # For non-authenticated users trying to access protected endpoints
        if not current_user.is_anonymous:
            return jsonify({"message": "Unauthorized"}), 401                                       


@api_bp.before_request
def keep_session_alive():
    session.modified = True # Before requests, keep alive session if it hasnt expired

@api_bp.route('/session_status')
def session_status():
    return jsonify({"session_expired": session_expired})

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
    model = request.args.get('model')
    service = request.args.get('search')
    town = request.args.get('town')
    search_results = DBOperations().filter(model, service, town)
    if search_results:
        return jsonify(search_results)
    else:
        return jsonify("No Results"), 404

@api_bp.route("/logout")
@login_required
def logout():
    # Log out the current user
    logout_user()
    session.pop('user_id', None)  # Clear user ID from session
    return jsonify({"message": "Logged out"}), 200

@api_bp.route("/create_object", methods=["POST"])
def create_object():
    form_data = request.get_json()
    new_obj = DBOperations().new(form_data)

    if new_obj:
        return {"response": "success"}
    else:
        pass
    return jsonify({"error": "Error creating a new object"}), 500


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
    if status == 200:
        user = response['message']
        response['message'] = 'OK'
        login_user(user)
        session['user_id'] = user.id  # Set user ID in session
        update_last_activity(user)
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
    required_fields = ["first_name", "last_name", "email", "password"]

    if not all(field in form_data for field in required_fields):
        return jsonify({"message": "Missing a required field"}), 400
    
    message, status = DBOperations().sign_up(form_data)
    return make_response(jsonify(message), status)


@api_bp.route("/Promotion/<id>", methods=["GET"])
def show_promo(id):
    promo_obj = DBOperations().search('Promotion', id)
    if promo_obj:
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

@api_bp.route('/pic', methods=['POST'])
def put_pic():    
    print("Pic ROUTE ACTIVATED")
    data = request.files
    print(data)
    return make_response({'message': 'OK'}, 200)


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

