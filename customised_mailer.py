#customised mailer
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

with open('person.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        emails.append((row[0], row[1]))  # assuming name is in the first column and email is in the second column

with app.app_context():
    for i, (name, email) in enumerate(tqdm(emails, desc="Sending emails", unit="email")):
        msg = Message(subject='Accepted! | Hope Horizon Foundation  ', sender='sesidadi.nssc@gmail.com', recipients=[email])
        with open('email_body.txt', 'r') as file:
            email_body = file.read()
        msg.body = f"Dear {name},\n\n{email_body}"
        mail.send(msg)
        print(f"Email {i+1} sent to {email}")
print("All emails sent successfully!")



