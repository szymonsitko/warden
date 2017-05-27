from peewee import *
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
from config.config import DATABASE_FULL_PATH


DATABASE = SqliteDatabase(DATABASE_FULL_PATH)


class BaseModel(Model):

    class Meta:
        database = DATABASE


class User(BaseModel, UserMixin):
    username = CharField(max_length=120, primary_key=True, unique=True)
    password = CharField(max_length=80)
    created = DateTimeField()
    authorised = BooleanField(default=False)

    @classmethod
    def new_user(cls, username, password, created):
        cls.create(
            username=username,
            password=generate_password_hash(password),
            created=created,
        )

    def is_active(self):
        if self.authorised:
            return True
        else:
            return False

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()
