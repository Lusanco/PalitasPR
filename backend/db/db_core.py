'''
    Main queries and logic function for 
    the main App functionalities.

    We think of this file as the main usage of the "User's stories"
    1) Landing page search bar
    2) Settings menu
    3) Profile secttion
    4) etc...

'''
from email_validator import validate_email, EmailNotValidError
from db_init import get_session
from db.db_promotion import Db_promotion
from db.db_request import Db_request
from models import User
from sqlalchemy.exc import SQLAlchemyError
import asyncio
from sqlalchemy import func
from unidecode import unidecode
from aws_bucket import create_model_folder
from db_init import get_session
from models import (
    User,
    Service,
    Town,
    Promo_Towns,
    Review,
    Task,
    Promotion,
    Request,
    Request_Towns,
    Promotion,
) 


class Db_core:
    '''
        Class to call when using any MAIN APP 
        functionality like the main search of the landing and other complex queries
        related to the main app functions

        Examples:
        * Searchbar of landing
    '''
    def __init__(self):
        self.session = get_session()

    def landing_searchBar(self, model=None, service=None, town_id = 0):
        """
        Main search for services provided in specific towns based on the provided model, service, and town ID.
        This represents the user typing inside the landing page searchbar looking for a certain service.
        Example:
            result = Db_core().landing_searchbar(model='promotions', service='cleaning', town_id=1)
        """
        if town_id == 'all' or town_id == '-1':
            town_id = 0

        if model is None and service is None:
            return {'error':'model or service missing'}, 400

        service_name = unidecode(service).lower() # Normalize text
        # Find service given the name typed on the searchbar
        service_obj = (
            self.session.query(Service)
            .filter(func.lower(Service.name).op("~")(f"{service_name}"))
            .first()
        )
        if not service_obj:
            return {'error': f'No service found with name: {service_name}'}, 404 

        my_service_id = service_obj.id
        service_name = service_obj.name
        if model == "promotions":
            rows = Db_promotion().get_promos_byTowns(my_service_id, town_id)
        if model == "requests":
            rows = Db_request().get_requests_byTowns(my_service_id, town_id)

        list_of_models = []

        # append dicts of models to list_of_models based on query results
        for row in rows:
            if model == "promotions":
                model_dict = {
                    "promo_id": str(row.promo_id),
                    "service": service_name,
                    "title": row.title,
                    "description": row.description,
                    "price_min": row.price_min,
                    "price_max": row.price_max,
                    "first_name": row.first_name,
                    "last_name": row.last_name,
                    "towns": row[3],
                    "created_at": row.created_at.strftime("%Y-%m-%d"),
                }
                list_of_models.append(model_dict)
            else: # Requests dict...
                model_dict = {
                    "request_id": str(row.request_id),
                    "service": service_name,
                    "title": row.title,
                    "description": row.description,
                    "first_name": row.first_name,
                    "last_name": row.last_name,
                    "towns": row[3],
                    "created_at": row.created_at.strftime("%Y-%m-%d"),
                }
                list_of_models.append(model_dict)

        return {'results': list_of_models}, 200

    async def dashboard_get_promos_requests(self, user_id):
        """
        Query promotions and requests from a specified user to
        present on his dashboard
        """

        tasks = [
            Db_promotion().get_user_promos(self.session, user_id),
            Db_request().get_user_requests(self.session, user_id)
        ]
        promotions, requests = await asyncio.gather(*tasks)
        return (promotions, requests)
