#this is related to upload.html
#uploader func doesn't work -> problem in 'security'?

from flask import Flask, render_template, request
from werkzeug import security #secure_filename -> older version

app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(security(f.filename))
        return 'file uploaded'

if __name__ == '__main__':
    app.run(debug = True)