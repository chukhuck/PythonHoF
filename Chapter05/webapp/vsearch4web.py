from flask import Flask, request, escape, session, copy_current_request_context
from vsearch import search4letters
from flask import render_template
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_log_in
from threading import Thread


app = Flask(__name__)

app.secret_key = 'ImgonnasecretYOU'

app.config['dbconfig'] = {'host':'127.0.0.1', 
                'user':'vsearch',
                'password':'vsearchpasswd', 
                'database': 'vsearchlogDB',}


@app.route('/search4', methods=['POST'])
def do_seach() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """Log web-request and return the results."""
        try:

            with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """insert into log 
                            (phrase, letters, ip, browserstring, results) 
                            values (%s,%s,%s,%s,%s)"""

                cursor.execute(_SQL, (req.form['phrase'],
                                 req.form['letters'],
                                 req.remote_addr,
                                 req.user_agent.browser,
                                 res,))

        except ConnectionError as err:
            print('Is your DB switched on? Error: ', str(err))
        except CredentialsError as err:
            print('User name/password is failed. Error: ', str(err))
        except SQLError as err:
            print('Is your query correct? Error:', str(err))
        except Exception as err:
            print('Something went wrong: ', str(err))

    title = 'Ваши результаты:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        return print('Something went wrong: ', err)
    return render_template('results.html', the_title = title, the_results = results, the_phrase=phrase, the_letters = letters,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='vsearch. web version')

@app.route('/viewlog')
@check_log_in
def view_the_log() -> 'html':
    try:
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

    except ConnectionError as err:
        print('<h2>Is your DB switched on? Error: ', str(err))
    except CredentialsError as err:
        print('<h2>User name/password is failed. Error: ', str(err))
    except SQLError as err:
        print('<h2>Is your query correct? Error:', str(err))
    except Exception as err:
        print('<h2>Something went wrong: ', str(err))
    return render_template('log.html',
                                the_title='Error',)

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return render_template('info.html', the_info ='Now you are log in.')

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return render_template('info.html', the_info='Now you are NOT log in.')



if __name__ == '__main__': 
 app.run(debug=True)