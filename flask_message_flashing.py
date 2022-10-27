#this is related to index1.html and login1.html

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = 'random string'

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid username or pw. try again!'
        else:
            flash('successfully logged in')
            flash('log out before login again')
            return redirect(url_for('index'))
    return render_template('login1.html', error = error)

if __name__ == '__main__':
    app.run(debug = True)