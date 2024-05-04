#!/usr/bin/python3
"""MAIN APP WITH FLASK"""

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from sqlalchemy import create_engine
from base_model import Base
from db_operations import DBOperations  # Import the method for creating new objects
from routes import app_bp
from flask_mail import Mail
from emails import confirm_email


# Create Flask app instance
app = Flask(__name__)
# Configure Flask app for sending emails using Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "antoniofdjs@gmail.com"
app.config["MAIL_PASSWORD"] = "syhk sijd eoli tgba"
app.register_blueprint(app_bp)
mail = Mail(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
CORS(app)

# Create the engine
engine = create_engine('postgresql://demo_dev:demo_dev_pwd@demodb.ctossyay6vcz.us-east-2.rds.amazonaws.com/postgres')

# Bind the engine to the Base class
Base.metadata.bind = engine

# VERIFY EMAIL ROUTE
@app.route("/verify_email/<token>", methods=["GET"])
def verify_email(token):

    if not token:
        return "Verification token is missing"

    verified = confirm_email(token)

    if not verified:
        return "Invalid verification token"

    return "Email verification successful"


@app.route("/")
def index():
    # Serve the built index.html from the frontend directory
    # return serve_static("index.html")
    return app.send_static_file("index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    """Serves static files from the configured static directory, or returns a 404 for unmatched files."""
    try:
        return app.send_static_file(filename)
    except FileNotFoundError:
        # Handle non-existent files gracefully
        return "File not found", 404


@app.route("/api/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    response = DBOperations().login(email, password)
    return jsonify(response)

@app.route('/api/explore', methods=['GET'])
def explore():
    model = request.args.get('model')
    service = request.args.get('search')
    town = request.args.get('town')
    print("AFTER GET ARGS REQUESTS")
    print(model)
    print(service)
    print(town)
    search_results = DBOperations().filter(model, service, town)
    if search_results:
        return jsonify(search_results)
    else:
        return jsonify("No Results"), 404

@app.route("/api/create_object", methods=["POST"])
def create_object():
    form_data = request.get_json()

    # If user is signing up
    if (
        "first_name" in form_data
        and "last_name" in form_data
        and "email" in form_data
        and "password" in form_data
    ):
        user_data = {
            "first_name": form_data["first_name"],
            "last_name": form_data["last_name"],
            "email": form_data["email"],
            "password": form_data["password"],
        }
        new_obj = DBOperations().sign_up(user_data)
    else:
        new_obj = DBOperations().new(form_data)

    # Check if object was created
    if new_obj:
        return {"response": "success"}
    else:
        pass
        # return render_template("error.html", error="Error creating object"), 400
    return


@app.route("/api/filter", methods=["POST"])
def search_filter():
    """
    Front has to send {'Service': {'name': 'Nails, 'town': 'Ponce'}}
    town is an optional argument for dict

    Usage:  {'object_id': {'parameter1': 'value1', 'parameter2': 'value2'}}

    example:
        filtered_objs = db.filter({'User': {'name': 'service_name', 'town': 'town_name'}})
    """
    data = request.json
    dictionary = DBOperations().filter(data)
    print(data)
    print(1, dictionary)

    if dictionary:
        return jsonify(dictionary)
    else:
        return jsonify({"error": "Error filtering data"})


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
