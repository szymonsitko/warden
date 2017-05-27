from flask import Blueprint, render_template, request, redirect, url_for
from flask_bcrypt import check_password_hash
from flask_login import login_user
from forms.login_form import LoginForm
from models.data_models import User
from messages.msg import LOGIN_MESSAGE, LOGIN_FAILURE, FORM_INVALID
from peewee import DoesNotExist

login_page = Blueprint(
    'login_page',
    __name__,
    template_folder='templates',
    static_folder='static'
)


def login_validation(username, password):
    try:
        validate_user = User.get(User.username == username)
        if check_password_hash(validate_user.password, password):
            return validate_user
        else:
            return False
    except DoesNotExist:
        return False


@login_page.route('/login', methods=['GET', 'POST'])
def login():
    # Determine initial welcome message (bonus point)
    register_redirect = request.args.get('register_redirect')
    if register_redirect is not None:
        login_message = register_redirect
    else:
        login_message = LOGIN_MESSAGE
    # Main logic
    login_form = LoginForm(request.form)
    if request.method == 'POST':
        if login_form.validate():
            username = request.form['username']
            password = request.form['password']
            validated_user = login_validation(username, password)
            if validated_user:
                login_user(validated_user)
                return redirect(url_for('dashboard_page.dashboard'))
            else:
                return render_template(
                    'login.html', form=login_form, error_message=LOGIN_FAILURE,
                )
        else:
            return render_template(
                'login.html', form=login_form, error_message=FORM_INVALID,
            )
    else:
        return render_template(
            'login.html', form=login_form, register_redirect=login_message,
        )
