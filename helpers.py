from flask import redirect, render_template, request, session
from functools import wraps
from questionPack import qBank


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def mark(results):
    score = 0
    for k,v in results.items():
        if v == '1':
            score += 1
    return score
