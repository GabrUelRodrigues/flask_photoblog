from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

auth = Blueprint("auth", __name__)

@auth.route("/sign_up", methods=["POST", "GET"])
def sign_up():
	if request.method == "POST":
		email = request.form.get("email")
		username = request.form.get("username")
		password = request.form.get("password")
		confirm_password = request.form.get("confirmPassword")

		email_exists = User.query.filter_by(email=email).first()
		username_exists = User.query.filter_by(username=username).first()

		if email_exists:
			flash("Email already used.", category="error")
		
		elif username_exists:
			flash("Username already used.", category="error")
		
		elif len(str(username)) < 4:
			flash("Username must have at least 4 characters.", category="error")
		
		elif len(str(password)) < 8:
			flash("Password must have at least 8 characters.", category="error")
		
		elif password != confirm_password:
			flash("Passwords don't match.", category="error")
		
		else:
			new_user = User(email=email, username=username, password=generate_password_hash(str(password), method="scrypt"))
			db.session.add(new_user)
			db.session.commit()

			login_user(new_user, remember=True)

			flash("Account created!", category="success")

			return redirect(url_for("views.home"))

	return render_template("sign_up.html")

@auth.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")

		user = User.query.filter_by(username=username).first()

		if user:
			if check_password_hash(user.password, str(password)):
				login_user(user, remember=True)
				flash("Login successfully!", category="success")

				return redirect(url_for("views.home"))
			
			else:
				flash("Incorrect password.", category="error")
			
		else:
			flash("User does not exist.", category="error")

	return render_template("login.html")

@auth.route("/logout", methods=["GET"])
@login_required
def logout():
	logout_user()
	return redirect(url_for("views.home"))