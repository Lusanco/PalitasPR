from flask import Blueprint, jsonify, request, render_template
from db_operations import DBOperations
from emails import confirm_email

api_bp = Blueprint('api', __name__)


@api_bp.route("/verify_email/<token>", methods=["GET"])
def verify_email(token):

    if not token:
        return "Verification token is missing"

    verified = confirm_email(token)

    if not verified:
        return "Invalid verification token"

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
    return


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


@api_bp.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    DBOperations().login(email, password)
    response_html = render_template("login_response.html")
    return response_html


@api_bp.route("/<class_name>/<id>", methods=["GET"])
def search_object(class_name, id):
    obj = DBOperations().search(class_name, id)
    if obj:
        return jsonify({"message": f"{class_name} object with ID {id} found"}), 200
    else:
        return jsonify({"error": f"No {class_name} object found with ID {id}"}), 404
