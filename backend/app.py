#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, current_app
from flask_cors import CORS
from sqlalchemy import create_engine
from base_model import Base
from db_operations import DBOperations
from blueprints import main_bp
from api_blueprint import api_bp
from flask_mail import Mail
from flask_login import LoginManager, user_logged_in, logout_user, user_logged_out
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

@user_logged_in.connect_via(app)
def on_user_logged_in(sender, user):
    update_last_activity(user)

def check_user_inactivity():
    with app.app_context():
        now = datetime.utcnow()
        inactive_threshold = timedelta(seconds=30)  # Adjusted to 30 seconds

        for user_id, last_activity in last_user_activity.items():
            user = DBOperations().search('User', user_id)
            if user and user.is_authenticated:
                if (now - last_activity).total_seconds() > inactive_threshold.total_seconds():
                    with app.test_request_context():  # Ensure request context is available
                        logout_user()  # Logout the user
                    print(f"User {user.email} logged out due to inactivity.")

# Create and configure scheduler within a function that runs in app context
def initialize_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(check_user_inactivity, 'interval', seconds=30)

# Ensure scheduler initialization within Flask application context
with app.app_context():
    initialize_scheduler()

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
