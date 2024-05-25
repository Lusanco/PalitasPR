"""
    Routes for Dashboard(User's personal items, posts, etc).
    These routes allow modifications for anything related to
    the user that is signed in
"""

from flask import Blueprint, jsonify, request, make_response, session
from db_operations import DBOperations
import emails
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
    LoginManager,
)
from werkzeug.utils import secure_filename
import aws_bucket

my_bp = Blueprint("my", __name__)


@my_bp.before_request
def keep_session_alive():
    session.modified = True  # Before requests, keep alive session if it hasnt expired


@my_bp.route("/promotion-request", methods=["GET", "POST", "PUT"])
@login_required
def promo_request():
    """
    Route to get all promo and request posted by a user
    """

    # GET METHOD:
    if request.method == "GET":

        # Retrieve all promotions and requests from a user
        results = DBOperations().promo_request(current_user.id)
        return (
            make_response({"results": results}),
            200,
        )  # 2 dicts, (<{promos}>, <{requests}>)

    # PUT METHOD:
    if request.method == "PUT":
        frontend_data = {
            "model": "Promotion",
            "id": "7533c8eb-6b8a-4bf5-a301-a064d1bc21c3",
            "title": "Modified Title",
            "price_min": 30,
        }
        model = frontend_data.get("model")
        frontend_data.pop("model")
        response, status = DBOperations().update({model: frontend_data})

        return make_response(jsonify(response), status)

    # POST METHOD:
    if request.method == "POST":

        keys_required = ["service_id", "model", "title", "description", "town"]

        data = request.get_json()
        print(data)
        if not data:
            return make_response(jsonify({"error": "No data sent via json"}), 400)

        # Check if missing keys from request
        for key in keys_required:
            if key not in data:
                return make_response(
                    jsonify({"error": f"Field: {key} not detected"}), 400
                )

        # Add user id to dict and pop unwanted data
        data["user_id"] = current_user.id
        model = data.get("model")
        town_id = data.get("town")

        data.pop("town")
        data.pop("model")

        # Create (Promo or Request)
        response, status = DBOperations().new({model: data})

        if status == 201:  # Ok status
            objectDict = response

            # Associate town with <promo/request> just made
            response, status = DBOperations().new(
                {"Promo_Towns": {"promo_id": objectDict["id"], "town_id": town_id}}
            )
            if status != 201:
                return make_response(jsonify({"error": "Adding town error"}), 500)

            # # Check if image is received
            # if 'image' in request.files:

            #     file = request.files['image']
            #     if file.filename == '':
            #         return make_response({'message': 'No selected file'}, 400)

            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify({"error": response}), status)

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

    #     # C) Make folder only
    #     if ('model_id') not in data and not picture:
