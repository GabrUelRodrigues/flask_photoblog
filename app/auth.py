from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint("auth", __name__)

@auth.route("/sign_up", methods=["POST", "GET"])
def sign_up():
	return render_template("sign_up.html")

@auth.route("/login", methods=["POST", "GET"])
def login():
	return render_template("login.html")

@auth.route("/logout", methods=["GET"])
@login_required
def logout():
	logout_user()
	return redirect(url_for("views.home"))