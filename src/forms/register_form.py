from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Regexp, Length


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(), Regexp(r'^[a-zA-Z0-9_]+$'),
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=5),
        ])