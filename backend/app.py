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
from datetime import timedelta, datetime
from db_init import Session, init_db
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


# Create Flask app instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "demo_dev_pwd"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "antoniofdjs@gmail.com"
app.config["MAIL_PASSWORD"] = "syhk sijd eoli tgba"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=15) # Session expires in 15 minutes
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(my_bp, url_prefix='/api/dashboard')
mail = Mail(app)
login_manager = LoginManager(app)
CORS(app)



@login_manager.user_loader
def load_user(user_id):
    return DBOperations().search('User', user_id)

@app.before_request
def keep_session_alive():
    now = datetime.utcnow()
    if 'last_activity' in session:
        last_activity = session['last_activity']
        if isinstance(last_activity, str):
            last_activity = datetime.fromisoformat(last_activity)

        # Convert to naive datetime by stripping timezone info
        if last_activity.tzinfo is not None:
            last_activity = last_activity.replace(tzinfo=None)

        expiration_time = last_activity + app.config['PERMANENT_SESSION_LIFETIME']
        if now > expiration_time:
            logging.info(f"Session expired for user {session.get('user_id', 'unknown')}")
            print("Session Expired")
            session.clear()

    session['last_activity'] = now.isoformat()
    session.modified = True  # Keep session alive if it hasn't expired


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
        return jsonify({"message": "File not found"}), 404



if __name__ == "__main__":
    init_db()
    app.run(debug=True)

