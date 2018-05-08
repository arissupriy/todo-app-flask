from functools import wraps
from flask import g, request, redirect, url_for, session


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        session.permanent = True
        try:
            if session['user'] is None:
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        except KeyError:
            session['next_url'] = request.url
            return redirect(url_for('login', url=request.url))
    return wrap
