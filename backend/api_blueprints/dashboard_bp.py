"""
    Routes for Dashboard(User's personal items, posts, etc).
    These routes allow modifications for anything related to
    the user that is signed in
"""

from flask import Blueprint, jsonify, request, make_response, g
from werkzeug.utils import secure_filename
from db.db_operations import DBOperations
from db.db_core import Db_core
import aws_bucket
import asyncio
from flask_login import (
    login_required,
    current_user,
)

my_bp = Blueprint("my", __name__)

@my_bp.route("/promotion-request", methods=["GET", "POST", "PUT"])
@login_required
def promo_request():
    """
        Handle every object related to the user from
        Promotion,Request, and pictures for these.
        All C.R.U.D methods
    """
    user_id = current_user.id

    # ---------------GET METHOD--------------------------------------------- 
    if request.method == "GET":
        async def dashboard_handler():
            return await Db_core(g.db_session).dashboard_get_promos_requests(user_id)

        results = asyncio.run(dashboard_handler())
        return make_response(jsonify({"results": results}), 200)
    # -----------------------------------------------------------------

    # ----------------PUT METHOD-----------------------------------
    if request.method == "PUT":

        data = dict(request.form)
        model = data.get("model")
        data_to_update = data.pop('model')
        response, status = DBOperations(g.db_session).update({model:data_to_update})
        if status != 200:
            g.db_session.rollback()
            return make_response(jsonify(response), status)

        # Check if image(s) is received and put into AWS
        if 'image' in request.files:
            image = request.files
            image = image['image']
            pic_name =  secure_filename(image.filename)
            pic_bytes = image.read()

            if pic_name == '':
                return make_response(jsonify({'error': 'Empty File Name'}), 400)

            response, status = aws_bucket.put_picture(user_id, model, model_id, pic_name, pic_bytes)
            if status != 201:
                g.db_session.rollback()
                return make_response(jsonify(response), status)

            # Save picture path name on the model object
            response, status = DBOperations(g.db_session).update({model: {'id': model_id, 'pictures': pic_name}})
            if status != 200:
                g.db_session.rollback()
                return make_response(jsonify(response), status)

        g.db_session.commit()
        return make_response(jsonify({'results': 'ok'}), 200)
    # -----------------------------------------------------------

    # --------------POST METHOD---------------------------------------
    if request.method == "POST":
        """
            Used to create Promotion or Request and Promo_Towns or Request_Towns
            Also can upload pictures to aws for said Classes before.
            Example: Makes promotion, associate towns, and also put pictures
        """
        keys_required = ["service_id", "model", "title", "description", "town"]

        # Get list of tuples from .form, cast into a 'dict'
        data = dict(request.form)
        print(data)

        if not data:
            return make_response(jsonify({"error": "No data sent via json"}), 400)

        for key in keys_required:
            if key not in data:
                return make_response(
                    jsonify({"error": f"Field: {key} not detected"}), 400
                )

        # Get model and towns, add user id to put into data dict
        data["user_id"] = user_id
        model = data.get("model")
        towns = data.get("town")
        towns_id = towns.split(',')
        towns_id = [int(id.strip()) for id in towns_id]

        data.pop("town")
        data.pop("model")

        # 1) Create (Promo or Request)
        response, status = DBOperations(g.db_session).new({model: data})

        if status != 201:
            g.db_session.rollback()
            return make_response(jsonify({"error": response}), status)
        g.db_session.flush()
        obj = response["results"]
        model_id = obj.id

        # 2) Associate town(s) with <promo/request> just made in step: 1)
        for town_id in towns_id:
            response, status = DBOperations(g.db_session).new(
                {"Promo_Towns": {"promo_id": model_id, "town_id": town_id}}
            )

            if status != 201:
                g.db_session.rollback()
                return make_response(jsonify({"error": f"Adding town_id: {town_id} error"}), 500)
            g.db_session.flush()
        # 3) Check if image(s) is received and put into AWS
        if 'image' in request.files:
            image = request.files
            image = image['image']
            pic_name =  secure_filename(image.filename)
            pic_bytes = image.read()
            if pic_name == '':
                return make_response(jsonify({'error': 'Empty File Name'}), 400)

            response, status = aws_bucket.put_picture(user_id, model, model_id, pic_name, pic_bytes)
            if status != 200:
                g.db_session.rollback()
                return make_response(jsonify(response), status)

            # 4) Save picture path name
            response, status = DBOperations(g.db_session).update({model: {'id': model_id, 'pictures': pic_name}})
            if status != 200:
                g.db_session.rollback()
                return make_response(jsonify(response), status)
        g.db_session.commit()
        return make_response(jsonify({'results': 'Created Succesfully'}), 201)

    # -----------------------END-------------------------------------------