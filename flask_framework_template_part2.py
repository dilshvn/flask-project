#this is related to hello_world.html

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello_world.html') #hello_world.html must be in the templates dir, css and js files must be stored in static dir

if __name__ == '__main__':
    app.run(debug = True)