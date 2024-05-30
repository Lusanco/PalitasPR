#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, jsonify, render_template, request, session, g
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from base_model import Base
from db_operations import DBOperations
from api_blueprints.api_blueprint import api_bp
from api_blueprints.dashboard_bp import my_bp
from flask_mail import Mail
from flask_login import LoginManager, login_user
from datetime import timedelta
from db_init import Session, init_db

# Create Flask app instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "demo_dev_pwd"
# Configure Flask app for sending emails using Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "antoniofdjs@gmail.com"
app.config["MAIL_PASSWORD"] = "syhk sijd eoli tgba"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15) # Session expires in 15 minutes
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(my_bp, url_prefix='/api/dashboard')
mail = Mail(app)
login_manager = LoginManager(app)


CORS(app)


@app.before_request
def keep_session_alive():
    session.modified = True  # Before requests, keep alive session if it hasnt expired



@login_manager.user_loader
def load_user(user_id):
    # Assuming `user_id` is the primary key of the user in your database
    # Implement your logic to load a user from the database based on `user_id`
    user = DBOperations().search('User', user_id)
    return user


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
    

# This function will be called after each request to close the session
@app.teardown_request
def remove_session(exception=None):
    session = g.pop('session', None)
    if session is not None:
        session.close()

# This function will be called when the application context is torn down
# (e.g., when@app.teardown_appcontext
def close_session(exception=None):
    session = g.pop('session', None)
    if session is not None:
        session.close()


if __name__ == "__main__":
    init_db()
    app.run(debug=True)