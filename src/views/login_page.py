from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


login_page = Blueprint(
    'login_page',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@login_page.route('/login', methods=['GET', 'POST'])
def login():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)