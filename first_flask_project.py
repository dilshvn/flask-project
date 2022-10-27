#FLASK

#required items: python, pip, cmd, virtualenv (installed using pip)

#setting up flask
    #install python
    #install pip
    #install pipenv -> pip3 install pipenv (in cmd)

#FIRST FLASK PROJECT

#setting up
    #create virtual environment called 'flaskenv' for the project
    #go to project dir (in cmd)
    #python -m venv flaskenv
    #flaskenv\Scripts\activate
    #pip install flask

#FIRST FLASK APP: HELLO WORLD!

from flask import Flask

app = Flask(__name__) #create obj app from Flask class

@app.route('/') #decorator
def hello_world():
    return 'hello world!' 

if __name__ == '__main__':
    app.run() #debug mode: off

#run the code and go to url in browser
