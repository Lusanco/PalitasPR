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
    Review,
    Task
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

    async def get_user_promos(self, session, my_user_id):
        """
        Main query to filter promotions
        """
        rows = (
            session.query(
                Promo_Towns.promo_id,
                User.first_name,
                User.last_name,
                func.array_agg(Town.name),
                Promotion.created_at,
                Promotion.title,
                Promotion.description,
                Promotion.price_min,
                Promotion.price_max,
                Service.name,
            )
            .select_from(Promotion)
            .join(User, Promotion.user_id == User.id)
            .join(Promo_Towns, Promotion.id == Promo_Towns.promo_id)
            .join(Town, Promo_Towns.town_id == Town.id)
            .join(Service, Promotion.service_id == Service.id)
            .filter((Promotion.user_id == my_user_id))
            .group_by(
                Promo_Towns.promo_id,
                User.first_name,
                User.last_name,
                Promotion.created_at,
                Promotion.description,
                Promotion.title,
                Promotion.price_min,
                Promotion.price_max,
                Service.name,
            )
            .order_by(Promo_Towns.promo_id)
            .all()
        )
        promos_dict = []
        for row in rows:
            inner_dict = {
                "promo_id": str(row.promo_id),
                "service": row.name,
                "title": row.title,
                "description": row.description,
                "price_min": row.price_min,
                "price_max": row.price_max,
                "first_name": row.first_name,
                "last_name": row.last_name,
                "towns": row[3],
                "created_at": row.created_at.strftime("%Y-%m-%d"),
            }
            promos_dict.append(inner_dict)
        return promos_dict

    def get_promo_reviews(self, promo_id):
        """
        Retrieves reviews for a specific promo.

        Args:
            promo_id (str): The ID of the promo.

        Returns:
            list: A list of dictionaries containing review details.
        """
        reviews = (
            self.session.query(
                Review
            )
            .join(Task, Review.task_id == Task.id)
            .join(Promotion, Task.promo_id == Promotion.id)
            .filter(Promotion.id == promo_id)
            .all()
        )

        review_list = []
        for review in reviews:
            user = review.reviewer
            review_dict = {
                'id': review.id,
                'description': review.description,
                'rating': review.rating,
                'pictures': review.pictures,
                'created_at': review.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            print(f'Review:{review_dict}\n')
            review_list.append(review_dict)

        return review_list
