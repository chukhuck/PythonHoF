from flask import Flask, request, escape
from vsearch import search4letters
from flask import render_template
from utils import log_request
from DBcm import UseDatabase


app = Flask(__name__)

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
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'IP', 'User agent', 'Result')

    return render_template('log.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)


if __name__ == '__main__': 
 app.run(debug=True)