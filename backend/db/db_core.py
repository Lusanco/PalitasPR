'''
    Main queries and logic function for 
    the main App functionalities.

    We think of this file as the main usage of the "User's stories"
    1) Landing page search bar
    2) Settings menu
    3) Profile secttion
    4) etc...

'''
from db.db_promotion import Db_promotion
from db.db_request import Db_request
from sqlalchemy import func
from unidecode import unidecode
from models import Service
import asyncio
import math


class Db_core:
    '''
        Class to call when using any MAIN APP 
        functionality like the main search of the landing and other complex queries
        related to the main app functions

        Examples:
        * Searchbar of landing
    '''
    def __init__(self, db_session):
        self.session = db_session

    def landing_searchBar(self, model=None, service=None, town_id = 0, page=1, limit=5):
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
        
        offset = (page -1) * limit

        if service == None or service == '':
            if model == 'promotions':
                total_count, rows = Db_promotion(self.session).get_all_promotions(town_id, page, limit)
            else:
                total_count, rows = Db_request(self.session).get_all_requests(town_id, page, limit)
            service_name = None
        else: # With service specific to find
            service_name = unidecode(service).lower() # Normalize text
            tsquery = func.to_tsquery('english', f'{service_name}:*')
            # Find service using full-text search
            service_obj = (
                self.session.query(Service)
                .filter(Service.tsv.op('@@')(tsquery))
                .all()
            )

            # Testing here, best match search
            print('My services: ')
            print(len(service_obj))
            if len(service_obj) > 0:
                for service in service_obj:
                    print(f'{service.name}')
                service_obj = service_obj[0]
            if not service_obj:
                return {'error': f'No service found with name: {service_name}'}, 404 

            my_service_id = service_obj.id
            service_name = service_obj.name
            if model == "promotions":
                total_count, rows = Db_promotion(self.session).get_promos_byTowns(my_service_id, town_id, page, limit)
            if model == "requests":
                total_count, rows = Db_request(self.session).get_requests_byTowns(my_service_id, town_id, page, limit)

        list_of_models = []

        # append dicts of models to list_of_models based on query results
        for row in rows:
            if service_name: # doing a specific service ------------------------------
                if model == "promotions":
                    model_dict = {
                        "promo_id": str(row.promo_id),
                        'user_id': row.user_id,
                        "service": service_name,
                        "title": row.title,
                        "description": row.description,
                        "price_min": row.price_min,
                        "price_max": row.price_max,
                        "first_name": row.first_name,
                        "last_name": row.last_name,
                        "towns": row[3],
                        "created_at": row.created_at.strftime("%Y-%m-%d"),
                        'pictures': row.pictures
                    }
                    list_of_models.append(model_dict)
                else: # Requests dict...
                    model_dict = {
                        "request_id": str(row.request_id),
                        'user_id': row.user_id,
                        "service": service_name,
                        "title": row.title,
                        "description": row.description,
                        "first_name": row.first_name,
                        "last_name": row.last_name,
                        "towns": row[3],
                        "created_at": row.created_at.strftime("%Y-%m-%d"),
                        'pictures': row.pictures
                    }
                    list_of_models.append(model_dict)
            else: # no specific service---------------------------------------------
                if model == "promotions":
                    model_dict = {
                        "promo_id": str(row.promo_id),
                        'user_id': row.user_id,
                        "service": row.name, # Service name
                        "title": row.title,
                        "description": row.description,
                        "price_min": row.price_min,
                        "price_max": row.price_max,
                        "first_name": row.first_name,
                        "last_name": row.last_name,
                        "towns": row[3],
                        "created_at": row.created_at.strftime("%Y-%m-%d"),
                        'pictures': row.pictures
                    }
                    list_of_models.append(model_dict)
                else: # Requests dict...
                    model_dict = {
                        "request_id": str(row.request_id),
                        'user_id': row.user_id,
                        "service": row.name, #Service name
                        "title": row.title,
                        "description": row.description,
                        "first_name": row.first_name,
                        "last_name": row.last_name,
                        "towns": row[3],
                        "created_at": row.created_at.strftime("%Y-%m-%d"),
                        'pictures': row.pictures
                    }
                    list_of_models.append(model_dict)
            # ------------------------------------------------------------------------------
        return {
                'results': list_of_models,
                'total_count': total_count,
                'page': page,
                'limit': limit,
                'total_pages': math.ceil(total_count / limit)
                }, 200

    async def dashboard_get_promos_requests(self, user_id):
        """
        Query promotions and requests from a specified user to
        present on his dashboard
        """

        tasks = [
            Db_promotion(self.session).get_user_promos(self.session, user_id),
            Db_request(self.session).get_user_requests(self.session, user_id)
        ]
        promotions, requests = await asyncio.gather(*tasks)
        return (promotions, requests)
