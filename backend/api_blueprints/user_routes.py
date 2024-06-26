from flask import Blueprint, jsonify, request, make_response, session
from db.db_user import Db_user
import emails
from flask_login import login_user, logout_user, login_required

user_bp = Blueprint('user', __name__)

@user_bp.before_request
def keep_session_alive():
    session.modified = True


@user_bp.route("/signup", methods=["POST"])
def user_sign_up():
    form_data = request.get_json()

    if (
        "first_name" in form_data
        and "last_name" in form_data
        and "email" in form_data
        and "password" in form_data
    ):
        response, status = Db_user().sign_up(form_data)

        if status != 201:
            return make_response(jsonify(response), status)

        return make_response(jsonify({"results": "ok"}), status)
    else:
        return make_response(jsonify({'message': 'Missing a required field'}), 400)


@user_bp.route("/verify_email/<token>", methods=["GET"])
def verify_email(token):
    if not token:
        return make_response(jsonify({'error':'Verification token is missing'}), 400)

    response, status = emails.confirm_email(token)
    return(make_response(jsonify(response)), status)


@user_bp.route('/login', methods=['GET'])
def user_login():
    email = request.args.get('af1')
    password = request.args.get('af2')
    response, status = Db_user().login(email, password)
    if status == 200:
        user = response['message']
        response['message'] = 'OK'
        login_user(user)
    return make_response(jsonify(response), status)


@user_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return make_response(jsonify({'results':'Logged out'}), 200)

