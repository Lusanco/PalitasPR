from datetime import datetime

last_user_activity = {}

def update_last_activity(user):
    """
    Update the last activity time for the given user.
    """
    last_user_activity[user.id] = datetime.utcnow()