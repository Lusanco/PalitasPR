from flask import Blueprint, jsonify, request, make_response, session
from db.db_user import Db_user
from db.db_operations import DBOperations
import emails
from flask_login import login_user, logout_user, login_required, current_user
import aws_bucket

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


@user_bp.route('/delete/<model>/<model_id>', methods=['DELETE'])
@login_required
def delete_object(model, model_id):
    """
    Delete a promotion, request, or picture associated with the current user.
    """
    # if model == 'Profile':
    #     model_id = current_user.id
    response, status = DBOperations().delete_object(model, model_id, current_user.id)
    return make_response(jsonify(response), status)

# WORKING DOWN HERE NEED TESTING
@user_bp.route('/initial-contacts', methods=['GET'])
@login_required
def get_contacts():
    '''
        Get all initial contact messages sent to a service provider by a
        requester
    '''
    response, status = Db_user().get_initial_contacts(current_user.id)
    return make_response(jsonify(response), status)

@user_bp.route('/my-profile', methods=['GET', 'PUT'])
@login_required
def get_my_profile():
    '''
        Get the user's profile
    '''
    if request.method == 'GET':
        profile = Db_user().get_profile_by_userId(current_user.id)
        if not profile:
            return make_response(jsonify({'error': 'Profile does not exist'}), 404)
        rating = Db_user().rating(current_user.id)
        profile_dict = {}
        profile_dict.update(profile.all_columns())
        profile_dict['first_name'] = current_user.first_name
        profile_dict['last_name'] = current_user.last_name
        profile_dict['rating'] = rating
        return make_response(jsonify({'results': profile_dict}), 200)

    if request.method == 'PUT':
        #TESTING
        # data = request.data  This must be a dictionary, must validate keys here or in dboperations.update
        data = {'Profile': {'id': 'profile_id', 'bio': 'Updated bio...'}}
        response, status = DBOperations().update({'Profile': {data}})
        return make_response(jsonify(response), status)

    if request.method == 'POST':
        # image_data = request.files  This must be picture, must validate keys here or in dboperations.update
        pic_bytes = bytes
        pic_name = 'pic_names'
        model = 'Gallery, Profile, Cover'
        aws_bucket.put_picture(current_user.id, model, None, pic_name, pic_bytes)

    if request.method == 'DELETE':
        #Testing
        # image_data = request.data  This must be picture names, must validate keys here or in dboperations.update
        pic_name = 'existing pic name'
        model = 'Gallery, Profile, Cover'
        response, status = aws_bucket.delete_picture(current_user.id, model, None, pic_name)
        return make_response(jsonify(response), status)


@user_bp.route('/profile/<profile_id>', methods=['GET'])
@login_required
def get_profile(profile_id):
    '''
        Get a user's profile(not your own)
    '''
    profile = DBOperations().search('Profile', profile_id)
    if not profile:
        return make_response(jsonify({'error': 'Profile does not exist'}), 404)
    user = DBOperations().search('User', profile.user_id)
    rating = Db_user().rating(profile.user_id)
    profile_dict = {}
    profile_dict.update(profile.all_columns())
    profile_dict['first_name'] = user.first_name
    profile_dict['last_name'] = user.last_name
    profile_dict['rating'] = rating
    return make_response(jsonify({'results': profile_dict}), 200)
