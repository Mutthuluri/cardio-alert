from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mrravikoya@gmail.com'
app.config['MAIL_PASSWORD'] = 'ipzlytdwszblacgq'

mail = Mail(app)

with app.app_context():
    try:
        msg = Message("Test Email", 
                      sender=app.config['MAIL_USERNAME'], 
                      recipients=['koyaravishankar521215@gmail.com'])
        msg.body = "✅ This is a test email from Flask!"
        mail.send(msg)
        print("✅ Email sent successfully")
    except Exception as e:
        print("❌ Email failed:", str(e))
