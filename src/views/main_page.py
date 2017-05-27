from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


main_page = Blueprint(
    'main_page',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@main_page.route('/')
def main():
    try:
        return render_template('main.html')
    except TemplateNotFound:
        abort(404)