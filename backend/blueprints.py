from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route("/login")
def login_page():
    return render_template("login.html")

@main_bp.route("/signup")
def signup_page():
    return render_template("signup.html")
