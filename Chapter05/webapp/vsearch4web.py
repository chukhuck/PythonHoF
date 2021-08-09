from flask import Flask, request, escape
from vsearch import search4letters
from flask import render_template
from utils import log_request


app = Flask(__name__)


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
def view_the_log() -> str:
    with open('vsearch.log') as log
        contents = log.read()
    return escape(contents)


if __name__ == '__main__': 
 app.run(debug=True)