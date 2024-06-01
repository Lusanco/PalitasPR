'''
    All related functions for Promotion class that involves the database
    and routes from flask.
'''
from db_init import get_session
from models import User
from sqlalchemy import func
from models import (
    User,
    Service,
    Town,
    Promo_Towns,
    Promotion,
    Promotion,
) 


class Db_promotion:
    '''
        Class to call when using any Promotion functionality
        required.

        Examples:
        * Promotion queries or mainly related to Promotion
        * Functionalites to filter certain Promotions
        * etc..
    '''
    def __init__(self):
        self.session = get_session()

    def get_promos_byTowns(self, my_service_id, town_id):
        """
            Query promotions based on service ID and town ID.
            Searches for specific Promotions in a specified town with all the info related.
        """
        if town_id == 0: # Do all towns
            rows = (
                self.session.query(
                    Promo_Towns.promo_id,
                    User.first_name,
                    User.last_name,
                    func.array_agg(Town.name),
                    Promotion.created_at,
                    Promotion.title,
                    Promotion.description,
                    Promotion.price_min,
                    Promotion.price_max,
                )
                .select_from(Promotion)
                .join(User, Promotion.user_id == User.id)
                .join(Promo_Towns, Promotion.id == Promo_Towns.promo_id)
                .join(Town, Promo_Towns.town_id == Town.id)
                .filter((Promotion.service_id == my_service_id))
                .group_by(
                    Promo_Towns.promo_id,
                    User.first_name,
                    User.last_name,
                    Promotion.created_at,
                    Promotion.description,
                    Promotion.title,
                    Promotion.price_min,
                    Promotion.price_max,
                )
                .order_by(Promo_Towns.promo_id)
                .all()
            )
            return rows
        else: # Specific town
            rows = (
                self.session.query(
                    Promo_Towns.promo_id,
                    User.first_name,
                    User.last_name,
                    func.array_agg(Town.name),
                    Promotion.created_at,
                    Promotion.title,
                    Promotion.description,
                    Promotion.price_min,
                    Promotion.price_max,
                )
                .select_from(Promotion)
                .join(User, Promotion.user_id == User.id)
                .join(Promo_Towns, Promotion.id == Promo_Towns.promo_id)
                .join(Town, Promo_Towns.town_id == Town.id)
                .filter(
                    (Promotion.service_id == my_service_id)
                    & ((Town.id == town_id))
                )
                .group_by(
                    Promo_Towns.promo_id,
                    User.first_name,
                    User.last_name,
                    Promotion.created_at,
                    Promotion.title,
                    Promotion.description,
                    Promotion.price_min,
                    Promotion.price_max,
                )
                .order_by(Promo_Towns.promo_id)
                .all()
            )
            return rows
