from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    str = '''
    <html>
    <body>
    <h1>Hello world!</h1>
    </body>
    </html>
    '''
    #instead using html code like this, we can use a html file and redirect to that -> store it in templates folder
    return str

if __name__ == '__main__':
    app.run(debug = True)