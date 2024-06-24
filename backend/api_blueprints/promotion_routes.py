from flask import Blueprint, jsonify, make_response, g
from db.db_promotion import Db_promotion
import asyncio
from db.db_operations import DBOperations
from db.db_user import Db_user
from db.db_promo_towns import Db_promo_towns
import aws_bucket

promotion_bp = Blueprint('promotion', __name__)


@promotion_bp.route("/promo_review/<promo_id>", methods=["GET"])
def promotion_reviews(promo_id):
    '''
        Get all promotion reviews
    '''
    reviews = Db_promotion(g.db_session).get_promo_reviews(promo_id)
    if not reviews:
        return make_response(jsonify({'results': None}), 200)

    return make_response(jsonify({'results': reviews}), 200)

@promotion_bp.route("/<id>", methods=["GET"])
def show_promo(id):
    promo = DBOperations(g.db_session).search('Promotion', id)
    if promo:
        promo_dict = {}
        promo_dict.update(promo.all_columns())
        promo_dict['first_name'] = promo.user.first_name
        promo_dict['last_name'] = promo.user.last_name
        profile = Db_user(g.db_session).get_profile_by_userId(promo.user.id)
        promo_dict['profile_id'] = profile.id
        promo_dict['towns'] = Db_promo_towns(g.db_session).get_towns_for_promo(promo_dict['id'])
        picNames = promo_dict['pictures']
        promo_id = promo_dict['id']
        user_id = promo_dict['user_id']
        urls = []
        # Get all pic names
        if promo_dict['pictures']:
            pic_list = picNames.split('|')

            async def handler_getPictures(pic_list, user_id, promo_id):
                tasks = []

                for pic in pic_list:
                    task = asyncio.create_task(aws_bucket.get_picture_async(user_id, 'Promotion', promo_id, pic))
                    tasks.append(task)
                awsResults = await asyncio.gather(*tasks)
                urls = [response[0]['results'] for response in awsResults if response[1] == 200]
                if not urls:
                    urls = []
                return urls

            urls = asyncio.run(handler_getPictures(pic_list, user_id, promo_id))

        if len(urls) == 0:
            urls == None 

        promo_dict['pictures'] = urls
        return make_response(jsonify({'results': promo_dict}), 200)
    else:
        return make_response(jsonify({"error": f"No Promotion object found with ID {id}"}), 404)
