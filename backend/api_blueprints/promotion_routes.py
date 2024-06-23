from flask import Blueprint, jsonify, make_response, g
from db.db_promotion import Db_promotion

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
