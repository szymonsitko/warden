from flask import Blueprint, render_template, abort
from flask_login import login_required
from jinja2 import TemplateNotFound


settings_page = Blueprint(
    'settings_page',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@settings_page.route('/settings')
@login_required
def settings():
    try:
        return render_template('settings.html')
    except TemplateNotFound:
        abort(404)