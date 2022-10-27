#go to flaskenv using cmd
#pip install flask_sqlalchemy
#this is related to show_all.html and new.html
#this doesn't work -> flask_sqlalchemy module is missing

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sql_alchemy import SQLAlchemy #old method -> doesn't work

#application configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3' #name of the database
app.config['SECRET_KEY'] = 'random string'
db = SQLAlchemy(app)

class students(db.Model): #inheritance
    #structure of the table
    id = db.Column('student_id', db.Integer, primary_key = True) #primary key
    name = db.Column(db.String(100)) #data_type(size)
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10)) #pincode

    def __init__(self, name, city, addr, pin): #constructor
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def now():
    if request.method == 'POST': #post method
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all fields', 'error')
        else: #get method
            student = students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))

    return render_template('new.html')
