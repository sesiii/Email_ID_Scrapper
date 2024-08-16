
from flask import Flask
from flask_mail import Mail, Message
from tqdm import tqdm
import csv

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL']=True
mail = Mail(app)

emails = []

with open('emails.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        emails.append(row[0])  # assuming email is in the first column

with app.app_context():
    for i, email in enumerate(tqdm(emails, desc="Sending emails", unit="email")):
        msg = Message(subject='National Students Space Challenge ', sender='sesidadi.nssc@gmail.com', recipients=[email])
        with open('email_body.txt', 'r') as file:
            msg.body = file.read()
        mail.send(msg)
        print(f"Email {i+1} sent to {email}")

print("All emails sent successfully!")