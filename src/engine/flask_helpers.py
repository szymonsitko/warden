from functools import wraps
from flask import redirect, g, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not g.user:
            redirect(url_for('login_page.login'))
        return func(*args, **kwargs)
    return wrapper
