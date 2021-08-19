from flask import Flask, request, escape, session
from vsearch import search4letters
from flask import render_template
from DBcm import UseDatabase
from checker import check_log_in


app = Flask(__name__)

app.secret_key = 'ImgonnasecretYOU'

app.config['dbconfig'] = {'host':'127.0.0.1', 
                'user':'vsearch',
                'password':'vsearchpasswd', 
                'database': 'vsearchlogDB',}


@app.route('/search4', methods=['POST'])
def do_seach() -> 'html':
    title = 'Ваши результаты:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title = title, the_results = results, the_phrase=phrase, the_letters = letters,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='vsearch. web version')

@app.route('/viewlog')
@check_log_in
def view_the_log() -> 'html':

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select 
                phrase, letters, ip, browserstring, results
                from log"""

        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', 'IP', 'User agent', 'Result')

    return render_template('log.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)

def log_request(req: 'flask_request', res: str) -> None:
    """Log web-request and return the results."""

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log 
                    (phrase, letters, ip, browserstring, results) 
                    values (%s,%s,%s,%s,%s)"""

        cursor.execute(_SQL, (req.form['phrase'],
                         req.form['letters'],
                         req.remote_addr,
                         req.user_agent.browser,
                         res,))

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'Now you are log in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'Now you are NOT log in.'



if __name__ == '__main__': 
 app.run(debug=True)