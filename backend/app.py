#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, session, g
from flask_cors import CORS
from db.db_operations import DBOperations
from api_blueprints.api_blueprint import api_bp
from api_blueprints.dashboard_bp import my_bp
from api_blueprints.user_routes import user_bp
from api_blueprints.promotion_routes import promotion_bp
from flask_mail import Mail
from flask_login import LoginManager
from datetime import timedelta
from db_init import init_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "demo_dev_pwd"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "antoniofdjs@gmail.com"
app.config["MAIL_PASSWORD"] = "syhk sijd eoli tgba"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(my_bp, url_prefix='/api/dashboard')
app.register_blueprint(user_bp, url_prefix='/api/user')
app.register_blueprint(promotion_bp, url_prefix='/api/promotion')
mail = Mail(app)
login_manager = LoginManager(app)

CORS(app)

@app.before_request
def keep_session_alive():
    session.modified = True


@login_manager.user_loader
def load_user(user_id):
    # Assuming `user_id` is the primary key of the user in your database
    # Implement your logic to load a user from the database based on `user_id`
    user = DBOperations().search('User', user_id)
    return user


# This function will be called after each request to close the session
@app.teardown_request
def close_session(exception=None):
    session = g.pop('session', None)
    if session is not None:
        session.close()


if __name__ == "__main__":
    init_db()
    app.run(debug=True)