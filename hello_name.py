#VARIABLE RULES

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s' %name

if __name__ == '__main__':
    app.run(debug = True)

#when url is 127.0.0.1:5000/hello/dilshan -> o/p: hello dilshan
#here, name is ‘dilshan’