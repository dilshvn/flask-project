#sending particular html data to particular url
#this is related to student.html and result.html

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST': 
        #GET requests include all required data in the URL
        #POST requests supply additional data from the browser to the server in msg body
        result = request.form
        return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug = True)
