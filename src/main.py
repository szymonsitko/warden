from flask import Flask, g
from flask_login import LoginManager, current_user
from peewee import DoesNotExist
from views.main_page import main_page
from views.login_page import login_page
from views.register_page import register_page
from views.settings_page import settings_page
from views.dashboard_page import dashboard_page
from views.logout_page import logout_page
from models.data_models import DATABASE, User, initialize


app = Flask(__name__)
app.secret_key = '2sadxaaa4sakcSDx21vJ'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_page.login'


@app.before_request
def before_request():
    g.db = DATABASE
    g.db.get_conn()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@login_manager.user_loader
def user_loader(userid):
    try:
        return User.get(User.username == userid)
    except DoesNotExist:
        return None


if __name__ == "__main__":
    initialize()
    app.register_blueprint(main_page)
    app.register_blueprint(login_page)
    app.register_blueprint(register_page)
    app.register_blueprint(settings_page)
    app.register_blueprint(dashboard_page)
    app.register_blueprint(logout_page)
    app.run(
        debug=True,
        host='localhost',
        port=8080,
    )
