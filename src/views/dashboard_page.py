from flask import Blueprint, render_template, abort, g
from jinja2 import TemplateNotFound
from flask_login import current_user, login_required


dashboard_page = Blueprint(
    'dashboard_page',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@dashboard_page.route('/dashboard')
@login_required
def dashboard():
    try:
        return render_template('dashboard.html', user=current_user.get_id())
    except TemplateNotFound:
        abort(404)