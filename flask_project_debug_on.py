#DEBUG MODE: ON

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug = True) #debug: on

#when debugger is ‘on’, we can make changes to our code and they will be automatically changed in the server
# if debugger is ‘off’, we have to stop the server, make the changes and then run the server again
