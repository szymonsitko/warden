from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
from main import app


db = SQLAlchemy(app)


class User(db.Model, UserMixin):

    __tablename__ = "user"

    username = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(80))
    created = db.Column(db.String(20))
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, created):
        self.username = username
        self.password = generate_password_hash(password)
        self.created = created
        self.authenticated = False

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def __str__(self):
        return "User: %s, created on: %s, is authenticated: %s." % (
            self.username, self.created, self.authenticated
        )
