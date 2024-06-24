'''
    All related functions for Request_Towns class that involves the database
    and routes from flask.
'''
from sqlalchemy.orm import joinedload
from models import User
from sqlalchemy import func
from models import (
    User, Service, Town, Request_Towns, 
    Promotion, Review, Task,
) 


class Db_request_towns:
    '''
        Class to call when using any Request_Towns functionality
        required.
    '''
    def __init__(self, db_session):
        self.session = db_session

    def get_towns_for_request(self, promoID):
        '''
            Returns List of all town names where request is being solicited or None 
        '''
        town_names = self.session.query(Town.name)\
            .join(Request_Towns, Request_Towns.town_id == Town.id)\
            .filter(Request_Towns.promo_id == promoID)\
            .all()
        if not town_names:
            return None
        list_ofTowns = []
        for town in town_names:
            list_ofTowns.append(town[0])
        return list_ofTowns
