from flask import Flask, render_template, request, flash
from flask_wtf_extension_forms import ContactForm
#this is related to flask_wtf_extension_forms.py, contact.html and success.html
#this doesn't work -> uses old methods

app = Flask(__name__)
app.secret_key = 'devlopment key'

@app.route('/contact', methods = ['POST','GET'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required')
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    if request.method == 'GET':
        return render_template('contact.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)