from flask import Flask
from flask_login import LoginManager

def create_app() -> Flask:
	app = Flask(__name__)
	app.config["SECRET_KEY"] = "wLqeImKU6ljtlaFRCPle"

	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix="/")
	app.register_blueprint(auth, url_prefix="/")

	login_manager = LoginManager()
	login_manager.login_view = "auth.login" # type: ignore
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return print(id)

	return app