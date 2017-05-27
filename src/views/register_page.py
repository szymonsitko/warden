from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


register_page = Blueprint(
    'register_page',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@register_page.route('/register', methods=['GET', 'POST'])
def register():
    try:
        return render_template('register.html')
    except TemplateNotFound:
        abort(404)