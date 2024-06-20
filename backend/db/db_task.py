'''
    All related functions for Tasks class that involves the database
    and routes from flask.
'''
from db_init import get_session
from models import User
from sqlalchemy import func, or_
from models import (
    User,
    Task,
    Initial_Contact
) 


class Db_task:
    '''
        Class to call when using any Tasks(Contract) functionality
        required.
    '''
    def __init__(self, db_session):
        self.session = db_session

    def get_tasks_by_userId(self, userId):
        '''
            Get all tasks of a user by his userId
        '''
        tasks = self.session.query(Task)\
            .join(User, or_(User.id == Task.receiver_id, User.id == Task.provider_id))\
            .filter(or_(Task.receiver_id == userId, Task.provider_id == userId))\
            .all()
        return tasks

    def get_task_by_contactId(self, contactID):
        '''
            Get a task by contact_id
        '''
        task = self.session.query(Task)\
            .filter(Task.initial_contact_id== contactID)\
            .first()
        return task
