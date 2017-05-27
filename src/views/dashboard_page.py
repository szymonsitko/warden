from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


dashboard_page = Blueprint(
    'dashboard_page',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@dashboard_page.route('/dashboard')
def dashboard():
    try:
        return render_template('dashboard.html')
    except TemplateNotFound:
        abort(404)