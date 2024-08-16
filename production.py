# #customised mailer
# from flask import Flask
# from flask_mail import Mail, Message
# import csv
# import time
# from tkinter import filedialog, simpledialog, Tk, Label, StringVar
# from tkinter.ttk import Progressbar
# # ntcy ulcf ktpo pold sasankkumardadi1103@gmail.com

# app = Flask(__name__)
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465

# # Create a Tkinter dialog for entering email and password
# root = Tk()
# root.withdraw()  # Hide the main window
# app.config['MAIL_USERNAME'] = simpledialog.askstring("Input", "Enter your email:", parent=root)
# app.config['MAIL_PASSWORD'] = simpledialog.askstring("Input", "Enter your password:", show='*', parent=root)

# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL']=True
# mail = Mail(app)

# # Open file dialog to select the email body file
# email_body_file_path = filedialog.askopenfilename(title="Please select the email body file")

# # Open file dialog to select the CSV file
# csv_file_path = filedialog.askopenfilename(title="Please select the CSV file with email addresses")

# emails = []

# with open(csv_file_path, 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if len(row) >= 2:  # Check that the row has at least two columns
#             emails.append((row[0], row[1]))  # assuming name is in the first column and email is in the second column

# from tkinter import Scrollbar, Text, Frame
# from tkinter.ttk import Style

# # Create a new tkinter window for showing the status
# status_window = Tk()
# status_window.title("Email Sending Status")
# status_window.geometry("800x600")  # Increase the size of the window

# # Set a style for the progress bar
# style = Style()
# style.configure("TProgressbar", thickness=50, troughcolor='gray', background='green', )

# # Create a frame for the progress bar
# progress_frame = Frame(status_window)
# progress_frame.pack(fill="x", pady=20)

# # Create a progress bar
# progress = Progressbar(progress_frame, length=500, style="TProgressbar")
# progress.pack(fill="x")

# # Create a scrollbar
# scrollbar = Scrollbar(status_window)
# scrollbar.pack(side="right", fill="y")

# # Create a text widget for the status label
# status_label = Text(status_window, wrap="word", yscrollcommand=scrollbar.set, bg="black", fg="white", font=("Helvetica", 16))
# status_label.pack(fill="both", expand=True)

# total_emails = len(emails)
# start_time = time.time()
# sent_emails = []


# with app.app_context():
#     for i, (name, email) in enumerate(emails):
#         msg = Message(subject='Inquiry About Research Projects or Internships  ', sender=('Dadi Sasank Kumar', app.config['MAIL_USERNAME']), recipients=[email])
#         with open(email_body_file_path, 'r') as file:
#             email_body = file.read()
#         # msg.body = f"Dear {name},\n\n{email_body}"
#         msg.body = f"{email_body}"
#         mail.send(msg)
#         sent_emails.append(email)

#         # Update progress bar
#         progress['value'] = (i+1) / total_emails * 100
#         elapsed_time = time.time() - start_time
#         estimated_time_left = elapsed_time / (i+1) * (total_emails-i-1)
#         status_label.insert("end", f"Email {i+1} sent to {email}\n{total_emails-i-1} emails left to send\nEstimated time left: {estimated_time_left:.2f} seconds\nSent emails: {', '.join(sent_emails)}\n")
#         status_window.update()

# status_label.insert("end", "All emails sent successfully!")



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