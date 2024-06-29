"""
    Routes for Dashboard(User's personal items, posts, etc).
    These routes allow modifications for anything related to
    the user that is signed in
"""

from flask import Blueprint, jsonify, request, make_response, g
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from db.db_operations import DBOperations
from db.db_core import Db_core
from models import Profile, Promotion, User, Service, Promo_Towns, Town
import aws_bucket
import asyncio
from sqlalchemy.orm import joinedload
from sqlalchemy import func


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
        response, status = DBOperations(
            g.db_session).update({model: data_to_update})
        if status != 200:
            g.db_session.rollback()
            return make_response(jsonify(response), status)

        # Check if image(s) is received and put into AWS
        if 'image' in request.files:
            image = request.files
            image = image['image']
            pic_name = secure_filename(image.filename)
            pic_bytes = image.read()

            if pic_name == '':
                return make_response(jsonify({'error': 'Empty File Name'}), 400)

            response, status = aws_bucket.put_picture(
                user_id, model, model_id, pic_name, pic_bytes)
            if status != 201:
                g.db_session.rollback()
                return make_response(jsonify(response), status)

            # Save picture path name on the model object
            response, status = DBOperations(g.db_session).update(
                {model: {'id': model_id, 'pictures': pic_name}})
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
        towns_id = [id.strip() for id in towns_id]

        if '' in towns_id:
            return make_response(jsonify({'error': 'No town was selected'}))
        if 'all' in towns_id:
            towns_id = [0]
        else:
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
            if model == 'Promotion':
                response, status = DBOperations(g.db_session).new(
                    {"Promo_Towns": {"promo_id": model_id, "town_id": town_id}}
                )
            else:
                response, status = DBOperations(g.db_session).new(
                    {"Request_Towns": {"request_id": model_id, "town_id": town_id}}
                )
            if status != 201:
                g.db_session.rollback()
                return make_response(jsonify({"error": f"Adding town_id: {town_id} error"}), 500)
            g.db_session.flush()

        # 3) Check if image(s) is received and put into AWS
        if 'image' in request.files:
            image = request.files
            image = image['image']
            pic_name = secure_filename(image.filename)
            pic_bytes = image.read()
            if pic_name == '':
                return make_response(jsonify({'error': 'Empty File Name'}), 400)

            response, status = aws_bucket.put_picture(
                user_id, model, model_id, pic_name, pic_bytes)
            if status != 200:
                g.db_session.rollback()
                return make_response(jsonify(response), status)

            # 4) Save picture path name
            response, status = DBOperations(g.db_session).update(
                {model: {'id': model_id, 'pictures': pic_name}})
            if status != 200:
                g.db_session.rollback()
                return make_response(jsonify(response), status)
        g.db_session.commit()
        return make_response(jsonify({'results': 'Created Succesfully'}), 201)

    # -----------------------END-------------------------------------------


@my_bp.route("/profile-promotions/<profile_id>", methods=["GET"])
@login_required
def get_profile_promotions(profile_id):
    """
    Retrieve all promotions associated with a given profile_id.
    """
    profile = g.db_session.query(Profile).filter(
        Profile.id == profile_id).first()

    if not profile:
        return make_response(jsonify({'error': f'No profile found with id: {profile_id}'}), 404)

    user_id = profile.user_id

    # Get all promotions for the user, including service and town information
    promotions = (g.db_session.query(Promotion, User, Service, func.array_agg(Town.name).label('towns'))
                  .join(User, Promotion.user_id == User.id)
                  .join(Service, Promotion.service_id == Service.id)
                  .outerjoin(Promo_Towns, Promotion.id == Promo_Towns.promo_id)
                  .outerjoin(Town, Promo_Towns.town_id == Town.id)
                  .filter(Promotion.user_id == user_id)
                  .group_by(Promotion.id, User.id, Service.id)
                  .all())

    promotion_list = []
    for promo, user, service, towns in promotions:
        promo_dict = {
            "promo_id": str(promo.id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "service": service.name,
            "title": promo.title,
            "description": promo.description,
            "pictures": promo.pictures,
            "created_at": promo.created_at.strftime("%Y-%m-%d"),
            # "price_max": promo.price_max,
            # "price_min": promo.price_min,
            # "user_id": promo.user_id,
            "towns": towns if towns[0] is not None else []
        }
        promotion_list.append(promo_dict)

    return make_response(jsonify({'results': promotion_list}), 200)
