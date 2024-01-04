from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
	return render_template("home.html")

@views.route("/posts/<username>")
def user_page(username):
	return render_template("posts.html")

@views.route("/create_post", methods=["GET", "POST"])
@login_required
def create_post():
	return render_template("create_post.html")

@views.route("/delete_post")
@login_required
def delete_post():
	return redirect(request.referrer)