
# from flask_mail import Mail, Message
# from flask import Flask
# from tqdm import tqdm

# app = Flask(__name__)
# mail = Mail(app)

# app.config["MAIL_SERVER"]='smtp.gmail.com'
# app.config["MAIL_PORT"]=465

# app.config['MAIL_USERNAME'] = input("Enter your email: ")
# app.config['MAIL_PASSWORD'] = input("Enter your password: ")
# app.config['MAIL_USE_TLS']=False
# app.config['MAIL_USE_SSL']=True
# mail = Mail(app)

# import csv

# emails = []

# with open('emails.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         emails.append(row[0])  # assuming email is in the first column  # hardcoded list of emails
# msg = Message(subject='Bulk Email', sender='sesidadi.nssc@gmail.com', recipients=emails)
# # msg.body = 'This is a bulk email message.'
# with open('email_body.txt', 'r') as file:
#     msg.body = file.read()
# with app.app_context():
#     mail.send(msg)

# print("Emails sent successfully!")

#customised mailer
from flask import Flask
from flask_mail import Mail, Message
from tqdm import tqdm
import csv
import getpass
from tkinter import filedialog
from tkinter import Tk

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = input("Enter your email: ")
app.config['MAIL_PASSWORD'] = input("Enter your password: ")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL']=True
mail = Mail(app)

# Hide the main tkinter window
root = Tk()
root.withdraw()

# Open file dialog to select the email body file
print("Please select the email body file...")
email_body_file_path = filedialog.askopenfilename()

# Open file dialog to select the CSV file
print("Please select the CSV file with email addresses...")
csv_file_path = filedialog.askopenfilename()

emails = []

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        emails.append(row[0])  # assuming email is in the first column

msg = Message(subject='Notice: Development Email - Not for Professional Use', 
              sender=('Sam Altman', app.config['MAIL_USERNAME']), 
              recipients=emails)
with open(email_body_file_path, 'r') as file:
    msg.body = file.read()

with app.app_context():
    mail.send(msg)

print("Emails sent successfully!")