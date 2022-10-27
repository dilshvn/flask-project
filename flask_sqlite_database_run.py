#we need sqlitestudio
#here, sample database is used
#this is related to home.html, student1.html, result1.html, list.html and database.db
#this won't work -> sample database not available

from flask import Flask, render_template, request
import sqlite3 as sql #no need to additionally install this module

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew') #adding new record
def new_student():
    return render_template('student1.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)', (nm, addr, city, pin)) #this is a sql command
                con.commit()
                msg = 'Record successfully added'
        except:
            con.rollback()
            msg = 'Error in insert operation'
        finally:
            return render_template('result1.html', msg = msg)
            con.close()

@app.route('/list') #show student table data using sql command
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM students') #sql command
    rows = cur.fetchall();
    return render_template('list.html', rows = rows)

if __name__ == '__main__':
    app.run(debug = True)
