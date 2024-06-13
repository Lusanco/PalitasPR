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
    if review_obj:
        return make_response(jsonify(review_obj), 200)
    else:
        return make_response(jsonify({"error": f"No reviews found for Promo_ID {promo_id}"}), 404)
