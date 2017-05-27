from flask import Blueprint, redirect, url_for
from flask_login import logout_user


logout_page = Blueprint(
    'logout_page',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@logout_page.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('main_page.main'))
