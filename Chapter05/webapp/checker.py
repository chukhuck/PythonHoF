from flask import session

def check_log_in(func):
    def wrapper():
        if 'logged_in' in session:
            return func()
        return 'You are not logged in'

    return wrapper