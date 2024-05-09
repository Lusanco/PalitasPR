from flask import Blueprint, jsonify, request, render_template
from db_operations import DBOperations
from emails import confirm_email
import emails
import uuid

api_bp = Blueprint('api', __name__)


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


@api_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    response = DBOperations().login(email, password)
    return jsonify(response), 200


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
        new_obj = DBOperations().sign_up(form_data)

    if new_obj:
        return {"response": "success"}
    else:
        pass
    return jsonify({"error": "Error creating a new object"})

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

