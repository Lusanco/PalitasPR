'''
    All related functions for Sending Initial_contact class
    and routes from flask.
'''
from db_init import get_session
from models import User
from sqlalchemy import func
from db.db_operations import DBOperations
from models import (
    Initial_Contact
) 


class Db_initial_contact:
    '''
        Handle sending initial_contacts objects 
        and relating with task.
    '''
    def __init__(self):
        self.session = get_session()

    def send_contact(self, receiver_id, sender_id, promo_id):
        '''
            Create initial contact to send to another user,
            contains reference to an exisiting promotion(or request maybe)
        '''
        response, status = DBOperations().new({'Initial_contact'})
        return response, status
