from DBcm import UseDatabase

def log_request(req: 'flask_request', res: str) -> None:
    """Log web-request and return the results."""
    
    dbconfig = {'host':'127.0.0.1', 
                'user':'vsearch',
                'password':'vsearchpasswd', 
                'database': 'vsearchlogDB',}

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log 
                    (phrase, letters, ip, browserstring, results) 
                    values (%s,%s,%s,%s,%s)"""

        cursor.execute(_SQL, (req.form['phrase'],
                         req.form['letters'],
                         req.remote_addr,
                         req.user_agent.browser,
                         res,))