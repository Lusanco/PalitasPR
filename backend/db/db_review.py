'''
    All related operations to reviews
'''
from models import Review


class Db_review:
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

    def get_review_by_TaskID(self, taskID):
        '''
            Find a Review by its task_id
        '''
        review = self.session.query(Review).filter(Review.task_id == taskID).first()
        if not review:
            return None
        return review

    def get_all_reviews(self):
        '''
            Get all reviews from database
        '''
        reviews = self.session.query(Review).all()
        if not reviews:
            return None
        reviews_list = []
        for review in reviews:
            reviews_list.append(review.all_columns())
        return reviews_list
