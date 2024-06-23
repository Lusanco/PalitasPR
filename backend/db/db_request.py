'''
    All related functions for Request class(service requests) that involves the database
    and routes from flask.
'''
from sqlalchemy import func
from models import (
    User,
    Service,
    Town,
    Request_Towns,
    Request,
) 


class Db_request:
    '''
        Class to call when using any Request functionality
        required.

        Examples:
        * Request queries or mainly related to Promotion
        * Functionalites to filter certain Request
        * etc..
    '''
    def __init__(self, db_session):
        self.session = db_session

    def get_requests_byTowns(self, my_service_id, town_id):
        """
        Query Requests (Service Requests) based on service ID and town ID.
        Searches all requests in a specified town with all the related information.
        """
        query = (
            self.session.query(
                Request_Towns.request_id,
                User.first_name,
                User.last_name,
                func.array_agg(Town.name),
                Request.created_at,
                Request.title,
                Request.description,
                Request.pictures,
                Request.user_id
            )
            .select_from(Request)
            .join(User, Request.user_id == User.id)
            .join(Request_Towns, Request.id == Request_Towns.request_id)
            .join(Town, Request_Towns.town_id == Town.id)
            .filter(Request.service_id == my_service_id)
            .group_by(
                Request_Towns.request_id,
                User.first_name,
                User.last_name,
                Request.created_at,
                Request.title,
                Request.description,
                Request.pictures,
                Request.user_id
            )
            .order_by(Request_Towns.request_id)
        )

        if town_id != 0:
            query = query.filter(Town.id == town_id)

        rows = query.all()
        return rows

    async def get_user_requests(self, session, my_user_id):
        """
        Main query to filter promotions
        """
        rows = (
            session.query(
                Request_Towns.request_id,
                User.first_name,
                User.last_name,
                func.array_agg(Town.name),
                Request.created_at,
                Request.title,
                Request.description,
                Service.name,
            )
            .select_from(Request)
            .join(User, Request.user_id == User.id)
            .join(Request_Towns, Request.id == Request_Towns.request_id)
            .join(Town, Request_Towns.town_id == Town.id)
            .join(Service, Request.service_id == Service.id)
            .filter((Request.user_id == my_user_id))
            .group_by(
                Request_Towns.request_id,
                User.first_name,
                User.last_name,
                Request.created_at,
                Request.description,
                Request.title,
                Service.name,
            )
            .order_by(Request_Towns.request_id)
            .all()
        )
        requests_dict = []
        for row in rows:
            inner_dict = {
                'request_id': str(row.request_id),
                'service': row.name,
                'title': row.title,
                'description': row.description,
                'first_name': row.first_name,
                'last_name': row.last_name,
                'towns': row[3],
                'created_at': row.created_at.strftime("%Y-%m-%d")
            }

            requests_dict.append(inner_dict)

        return requests_dict
