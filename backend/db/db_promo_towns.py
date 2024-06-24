'''
    All related functions for Promo_Towns class that involves the database
    and routes from flask.
'''

from models import Town, Promo_Towns


class Db_promo_towns:
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

    def get_towns_for_promo(self, promoID):
        '''
            Returns List of all town names where promo is available or None 
        '''
        town_names = self.session.query(Town.name)\
            .join(Promo_Towns, Promo_Towns.town_id == Town.id)\
            .filter(Promo_Towns.promo_id == promoID)\
            .all()
        if not town_names:
            return None
        list_ofTowns = []
        for town in town_names:
            list_ofTowns.append(town[0])
        return list_ofTowns
