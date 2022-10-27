#install wtf extension inside flaskenv using cmd
#pip install flask_wtf
#this doesn't work -> uses old methods
#this is related to flask_wtf_extension_form_execution.py

from flask_wtf_extension_forms import Form, TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, validators, ValidationError

#designing the form
class ContactForm(Form): #inheriting from Form class
    name = TextField('name of student', [validators.Required('enter your name')])
    Gender = RadioField('Gender', choices = [('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField('Address')
    email = TextField('email', [validators.Required('enter your email address'), validators.Email('enter your email')])
    Age = IntegerField('age')
    language = SelectField('languages', choices = [('cpp', 'c++'), ('py', 'python')])
    submit = SubmitField('send')