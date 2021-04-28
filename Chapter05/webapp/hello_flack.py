from flack import Flack

app = Flack(__name__)

@app.route('/')

def hello_world() -> str:
    return 'Hello world from Flack'

app.run()