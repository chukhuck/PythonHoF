from flask import session, render_template
from functools import wraps

def check_log_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return render_template('info.html', the_info ='You are not logged in.')

    return wrapper