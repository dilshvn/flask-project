#URL BUILDING

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin') #urls must start with open slasj '/'
def hello_admin():
    return 'what\'s up admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello %s (guest)' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin')) #calls hello_admin func
    else:
        return redirect(url_for('hello_guest', guest = name)) #calls hello_guest func

if __name__ == '__main__':
    app.run(debug = True) #debug mode: on
