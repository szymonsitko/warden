from flask import Flask
from flask_login import LoginManager
from views.main_page import main_page
from views.login_page import login_page
from views.register_page import register_page
from views.settings_page import settings_page
from views.dashboard_page import dashboard_page
from config.config import DATABASE_PATH


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s' % DATABASE_PATH


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# @app.before_request
# def before_request():
#     # opens connection with database
#     g.db = models.DATABASE
#     g.db.connect()
#
#
# @app.after_request
# def after_request(response):
#     # closes connections with database
#     g.db.close()
#     return response


if __name__ == "__main__":
    app.register_blueprint(main_page)
    app.register_blueprint(login_page)
    app.register_blueprint(register_page)
    app.register_blueprint(settings_page)
    app.register_blueprint(dashboard_page)
    app.run(
        debug=True,
        host='localhost',
        port=8080,
    )
