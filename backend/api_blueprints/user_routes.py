from flask import Blueprint, jsonify, request, make_response, g
from flask_login import login_user, logout_user, login_required, current_user
from db.db_operations import DBOperations
from db.db_user import Db_user
import emails
import aws_bucket

user_bp = Blueprint('user', __name__)

@user_bp.route("/signup", methods=["POST"])
def user_sign_up():
    form_data = request.get_json()

    if (
        "first_name" in form_data
        and "last_name" in form_data
        and "email" in form_data
        and "password" in form_data
    ):
        response, status = Db_user(g.db_session).sign_up(form_data)
        if status != 201:
            g.db_session.rollback()
            return make_response(jsonify(response), status)
        g.db_session.commit()
        return make_response(jsonify({'results': 'ok'}), 201)
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
    response, status = Db_user(g.db_session).login(email, password)
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
    response, status = DBOperations(g.db_session).delete_object(model, model_id, current_user.id)
    return make_response(jsonify(response), status)


@user_bp.route('/contacts', methods=['GET']) # initial contacts (messages) display
@login_required
def get_contacts():
    '''
        Get all initial contact messages for the user and tasks
    '''
    response, status = Db_user(g.db_session).get_contacts_section(current_user.id)
    # MODIFY i need to retrieve the tasks of this user and
    # associate the task with the initial contact
    return make_response(jsonify(response), status)

@user_bp.route('/my-profile', methods=['GET', 'PUT'])
@login_required
def get_my_profile():
    '''
        Get the user's profile
    '''
    if request.method == 'GET':
        profile = Db_user(g.db_session).get_profile_by_userId(current_user.id)
        if not profile:
            return make_response(jsonify({'error': 'Profile does not exist'}), 404)
        rating = Db_user(g.db_session).rating(current_user.id)
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
        response, status = DBOperations(g.db_session).update({'Profile': {data}})
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
    profile = DBOperations(g.db_session).search('Profile', profile_id)
    if not profile:
        return make_response(jsonify({'error': 'Profile does not exist'}), 404)
    user = DBOperations(g.db_session).search('User', profile.user_id)
    rating = Db_user(g.db_session).rating(profile.user_id)
    profile_dict = {}
    profile_dict.update(profile.all_columns())
    profile_dict['first_name'] = user.first_name
    profile_dict['last_name'] = user.last_name
    profile_dict['rating'] = rating
    return make_response(jsonify({'results': profile_dict}), 200)

@user_bp.route('/update', methods=['GET'])
@login_required
def update_bio():
    response, status = DBOperations(g.db_session).update({'User': {'last_name': 'Doe', 'id': current_user.id}})
    if status != 200:
        g.db_session.rollback()
    g.db_session.commit()
    return make_response(jsonify(response), status)

@user_bp.route('/status', methods=['GET'])
@login_required
def get_user_status():
    if current_user.is_anonymous:
        return make_response(jsonify(False), 501)
    else:
        user_info = {}
        user_info.update(current_user.all_columns())
        user_info.pop('password')
        user_info.pop('verified')
        user_info.pop('verification_token')
        user_info.pop('updated_at')
        user_info.pop('created_at')
        profile = Db_user(g.db_session).get_profile_by_userId(user_info.get('id'))
        user_info['profile_id'] = profile.id
        
        return make_response(jsonify(user_info), 200)
