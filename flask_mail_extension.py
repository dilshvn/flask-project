#MAIL EXTENSION

#install mail extension using cmd
#if it will already installed -> it will let u know

#go to scripts in flaskenv (in cmd)
#pip install flask_mail

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

#configuration settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com' #server name
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'xyz@gmail.com' #username
app.config['MAIL_PASSWORD'] = '***' #pw
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('hello', sender = 'xyz@gmail.com', recipients = ['abc@gmail.com'])
    msg.body = 'this msg is sent using flask mail'
    mail.send(msg)
    return 'msg sent'

if __name__ == '__main__':
    app.run(debug = True)

#before running the app, turn on less secure apps -> google.com/settings/security/lesssecureapps
#email can be sent to gmail