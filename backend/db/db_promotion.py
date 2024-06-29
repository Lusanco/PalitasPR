'''
    All related functions for Promotion class that involves the database
    and routes from flask.
'''
from sqlalchemy.orm import joinedload
from models import User
from sqlalchemy import func, or_
from models import (
    User, Service, Town, Promo_Towns, 
    Promotion, Review, Task
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
    def __init__(self, db_session):
        self.session = db_session

    def get_promos_byTowns(self, my_service_id, town_id, page, limit):
        """
        Query promotions based on service ID and town ID.
        Searches for specific Promotions in a specified town with all the info related.
        """
        query = (
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
                Promotion.user_id,
                Promotion.pictures
            )
            .select_from(Promotion)
            .join(User, Promotion.user_id == User.id)
            .join(Promo_Towns, Promotion.id == Promo_Towns.promo_id)
            .join(Town, Promo_Towns.town_id == Town.id)
            .filter(Promotion.service_id == my_service_id)
            .group_by(
                Promo_Towns.promo_id,
                User.first_name,
                User.last_name,
                Promotion.created_at,
                Promotion.title,
                Promotion.description,
                Promotion.price_min,
                Promotion.price_max,
                Promotion.user_id,
                Promotion.pictures
            )
            .order_by(Promo_Towns.promo_id)
        )
        # If a town sent, make query by towns
        if town_id != 0:
            query = query.filter(Town.id == town_id)

        total_count = query.count()

        offset = (page - 1) * limit
        # .all() submtis the request for the query
        rows = query.offset(offset).limit(limit).all()
        return total_count, rows

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
        reviews = (
            self.session.query(Review)
            .join(Task, Review.task_id == Task.id)
            .join(Promotion, Task.promo_id == Promotion.id)
            .options(joinedload(Review.reviewer))  # Eager load the 'reviewer' relationship
            .filter(Promotion.id == promo_id)
            .all()
        )

        review_list = []
        for review in reviews:
            review_dict = {
                'id': review.id,
                'description': review.description,
                'rating': review.rating,
                'pictures': review.pictures,
                'created_at': review.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                'first_name': review.reviewer.first_name,  # Access loaded 'reviewer' directly
                'last_name': review.reviewer.last_name
            }
            review_list.append(review_dict)
        return review_list

    def get_all_promotions(self, town_id, page, limit):
        print(f"All promotions for town_id {town_id}")
        query = (
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
                Promotion.user_id,
                Promotion.pictures,
                Service.name
            )
            .select_from(Promotion)
            .join(User, Promotion.user_id == User.id)
            .join(Promo_Towns, Promotion.id == Promo_Towns.promo_id)
            .join(Town, Promo_Towns.town_id == Town.id)
            .join(Service, Promotion.service_id == Service.id)
            .group_by(
                Promo_Towns.promo_id,
                User.first_name,
                User.last_name,
                Promotion.created_at,
                Promotion.title,
                Promotion.description,
                Promotion.price_min,
                Promotion.price_max,
                Promotion.user_id,
                Promotion.pictures,
                Service.name
            )
            .order_by(Promo_Towns.promo_id)
        )
        # If a town sent, make query by towns
        if town_id != 0:
            query = query.filter(or_(Town.id == town_id, Town.id == 0))

        # Count total results before pagination
        total_count = query.count()

        offset = (page - 1) * limit
        # '.all()' submtis the request for the query
        rows = query.offset(offset).limit(limit).all()
        return total_count, rows
