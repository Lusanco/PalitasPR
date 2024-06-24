#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

import os
from flask import Flask, send_from_directory, session, g
from flask_cors import CORS
from flask_mail import Mail
from flask_login import LoginManager
from datetime import timedelta
from db.db_operations import DBOperations
import db_init

from api_blueprints.api_blueprint import api_bp
from api_blueprints.dashboard_bp import my_bp
from api_blueprints.user_routes import user_bp
from api_blueprints.promotion_routes import promotion_bp
from api_blueprints.tasks_routes import task_bp
from api_blueprints.reviews_routes import review_bp
from api_blueprints.requests_routes import request_bp
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__, static_folder="static")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USER")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PWD")
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=15)

app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(my_bp, url_prefix="/api/dashboard")
app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(promotion_bp, url_prefix="/api/promotion")
app.register_blueprint(task_bp, url_prefix="/api/tasks")
app.register_blueprint(review_bp, url_prefix="/api/reviews")
app.register_blueprint(request_bp, url_prefix="/api/request")

login_manager = LoginManager(app)
mail = Mail(app)
CORS(app)


@app.before_request
def keep_session_alive():
    session.modified = True
    g.db_session = db_init.get_session()

@login_manager.user_loader
def load_user(user_id):
    # Assuming `user_id` is the primary key of the user in your database
    # Implement your logic to load a user from the database based on `user_id`
    user = DBOperations(g.db_session).search("User", user_id)
    return user

# This function will be called after each request to close the session
@app.teardown_request
def close_session(exception=None):
    session = g.pop("session", None)
    if session is not None:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)
