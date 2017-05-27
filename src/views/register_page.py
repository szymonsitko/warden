from flask import Blueprint, render_template, request, redirect, url_for
from forms.register_form import RegisterForm
from models.data_models import User
from messages.msg import REGISTER_SUCCESS, REGISTER_FAILURE, FORM_INVALID
from peewee import DoesNotExist

import datetime


register_page = Blueprint(
    'register_page',
    __name__,
    template_folder='templates',
    static_folder='static',
)


def register_validation(new_user):
    try:
        user_query = User.get(User.username == new_user)
        if user_query:
            return False
    except DoesNotExist:
        return True


@register_page.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm(request.form)
    if request.method == 'POST':
        if register_form.validate():
            username = request.form['username']
            password = request.form['password']
            created = datetime.datetime.now()
            if register_validation(username):
                User.new_user(
                    username, password, created,
                )
                return redirect(url_for('login_page.login', register_redirect=REGISTER_SUCCESS))
            else:
                return render_template(
                    'register.html', form=register_form, message=REGISTER_FAILURE,
                )
        else:
            return render_template(
                'register.html', form=register_form, message=FORM_INVALID,
            )
    else:
        return render_template('register.html', form=register_form,)
