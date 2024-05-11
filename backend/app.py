#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, jsonify, render_template, request, current_app
from flask_cors import CORS
from sqlalchemy import create_engine
from base_model import Base
from db_operations import DBOperations
from blueprints import main_bp
from api_blueprint import api_bp
from flask_mail import Mail
from flask_login import LoginManager, login_user, user_logged_in, logout_user, current_user
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from user_activity import update_last_activity, last_user_activity



# Create Flask app instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "demo_dev_pwd"
# Configure Flask app for sending emails using Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "antoniofdjs@gmail.com"
app.config["MAIL_PASSWORD"] = "syhk sijd eoli tgba"
app.register_blueprint(main_bp)
app.register_blueprint(api_bp, url_prefix='/api')
mail = Mail(app)
login_manager = LoginManager(app)


CORS(app)

engine = create_engine('postgresql://demo_dev:demo_dev_pwd@demodb.ctossyay6vcz.us-east-2.rds.amazonaws.com/postgres')

Base.metadata.bind = engine


# last_user_activity = {}

# def update_last_activity(user):
#     """
#     Update the last activity time for the given user.
#     """
#     last_user_activity[user.id] = datetime.utcnow()

# Connect the update_last_activity function to the user_logged_in signal
@user_logged_in.connect_via(app)
def on_user_logged_in(sender, user):
    update_last_activity(user)


def check_user_inactivity():
    with current_app.app_context():
        now = datetime.utcnow()
        inactive_threshold = timedelta(seconds=60)  # 1 hour (in seconds) 3600

        for user_id, last_activity in last_user_activity.items():
            # user = current_user
            user = DBOperations().search('User', user_id)
            if user and user.is_authenticated and (now - last_activity).total_seconds() > inactive_threshold:
                logout_user()
                print(f"User {user.email} logged out due to inactivity.")

scheduler = BackgroundScheduler()
scheduler.add_job(check_user_inactivity, 'interval', minutes=1)
scheduler.start()



@login_manager.user_loader
def load_user(user_id):
    user = DBOperations().search('User', user_id)
    if user:
        return user
    return None


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    """Serves static files from the configured static directory, or returns a 404 for unmatched files."""
    try:
        return app.send_static_file(filename)
    except FileNotFoundError:
        # Handle non-existent files gracefully
        return "File not found", 404


if __name__ == "__main__":
    app.run(debug=True)