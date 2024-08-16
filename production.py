# Description: This script is used to send customised emails to multiple recipients using a CSV file with email addresses and an email body file.
#
# The script uses the Flask-Mail extension to send emails via SMTP. The email body is read from a text file, and the recipient's name is inserted into the email body before sending the email.
#
# The script prompts the user to enter their email address and password, as well as select the email body file and CSV file with email addresses using a file dialog.
#
# The script then iterates over the email addresses in the CSV file, reads the email body from the text file, inserts the recipient's name into the email body, and sends the email using Flask-Mail.
#
# The progress of sending emails is displayed using a progress bar and status label in a separate tkinter window.
#
# The script is designed to be run from the command line or an IDE like PyCharm. It requires the Flask and Flask-Mail libraries to be installed.
#
# Usage:
# 1. Run the script in a Python environment with the required libraries installed.
# 2. Enter your email address and password when prompted.
# 3. Select the email body file and CSV file with email addresses using the file dialogs.
# 4. The script will send customised emails to the recipients in the CSV file and display the progress in a tkinter window.
# 5. Once all emails are sent, the script will display a success message.
#
# Note: Make sure to enable less secure apps access in your Gmail account settings to send emails using SMTP.
#




#customised mailer
from flask import Flask
from flask_mail import Mail, Message
import csv
import time
from tkinter import filedialog, simpledialog, Tk, Label, StringVar, Scrollbar, Text, Frame
from tkinter.ttk import Progressbar, Style

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465

# Create a Tkinter dialog for entering email and password
root = Tk()
root.withdraw()  # Hide the main window
app.config['MAIL_USERNAME'] = simpledialog.askstring("Input", "Enter your email:", parent=root)
app.config['MAIL_PASSWORD'] = simpledialog.askstring("Input", "Enter your password:", show='*', parent=root)

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Open file dialog to select the email body file
email_body_file_path = filedialog.askopenfilename(title="Please select the email body file")

# Open file dialog to select the CSV file
csv_file_path = filedialog.askopenfilename(title="Please select the CSV file with email addresses")

emails = []

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) >= 3:  # Check that the row has at least three columns
            emails.append((row[1], row[2]))  # assuming name is in the second column and email is in the third column

# Create a new tkinter window for showing the status
status_window = Tk()
status_window.title("Email Sending Status")
status_window.geometry("800x600")  # Increase the size of the window

# Set a style for the progress bar
style = Style()
style.configure("TProgressbar", thickness=50, troughcolor='gray', background='green')

# Create a frame for the progress bar
progress_frame = Frame(status_window)
progress_frame.pack(fill="x", pady=20)

# Create a progress bar
progress = Progressbar(progress_frame, length=500, style="TProgressbar")
progress.pack(fill="x")

# Create a scrollbar
scrollbar = Scrollbar(status_window)
scrollbar.pack(side="right", fill="y")

# Create a text widget for the status label
status_label = Text(status_window, wrap="word", yscrollcommand=scrollbar.set, bg="black", fg="white", font=("Helvetica", 16))
status_label.pack(fill="both", expand=True)

total_emails = len(emails)
start_time = time.time()
sent_emails = []

with app.app_context():
    for i, (name, email) in enumerate(emails):
        try:
            msg = Message(subject='Inquiry About Research Projects or Internships', sender=('Dadi Sasank Kumar', app.config['MAIL_USERNAME']), recipients=[email])
            with open(email_body_file_path, 'r') as file:
                email_body = file.read()
            # msg.body = f"Dear {name},\n\n{email_body}"
            msg.body = f"{email_body}"
            mail.send(msg)
            sent_emails.append(email)

            # Update progress bar
            progress['value'] = (i + 1) / total_emails * 100
            elapsed_time = time.time() - start_time
            estimated_time_left = elapsed_time / (i + 1) * (total_emails - i - 1)
            status_label.insert("end", f"Email {i + 1} sent to {email}\n{total_emails - i - 1} emails left to send\nEstimated time left: {estimated_time_left:.2f} seconds\nSent emails: {', '.join(sent_emails)}\n")
            status_window.update()
        except Exception as e:
            status_label.insert("end", f"Failed to send email to {email}: {e}\n")
            status_window.update()

status_label.insert("end", "All emails sent successfully!")
status_window.mainloop()