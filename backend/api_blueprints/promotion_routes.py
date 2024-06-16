from flask import Blueprint, jsonify, request, make_response, session
from db.db_user import Db_user
from db.db_operations import DBOperations
import emails
from flask_login import login_user, logout_user, login_required, current_user
from db.db_promotion import Db_promotion

promotion_bp = Blueprint('promotion', __name__)

@promotion_bp.before_request
def keep_session_alive():
    session.modified = True

@promotion_bp.route("/promo_review/<promo_id>", methods=["GET"])
def promotion_reviews(promo_id):
    '''
        Get all promotion reviews
    '''
    review_obj = Db_promotion().get_promo_reviews(promo_id)
    if not review_obj:
        return make_response(jsonify({'results': None}), 200)

    return make_response(jsonify({'results': review_obj}), 200)
