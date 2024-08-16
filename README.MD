# Description: 

This script is used to send customized emails to multiple recipients using a CSV file with email addresses and an email body file.

The script utilizes the Flask-Mail extension to send emails via SMTP. The email body is read from a text file, and the recipient's name is inserted into the email body before sending the email.

The script prompts the user to enter their email address and password, as well as select the email body file and CSV file with email addresses using a file dialog.

The script then iterates over the email addresses in the CSV file, reads the email body from the text file, inserts the recipient's name into the email body, and sends the email using Flask-Mail.

The progress of sending emails is displayed using a progress bar and status label in a separate tkinter window.

The script is designed to be run from the command line or an IDE like PyCharm. It requires the Flask and Flask-Mail libraries to be installed.

# Usage:

1. Run the script in a Python environment with the required libraries installed.
2. Enter your email address and password when prompted.
3. Select the email body file and CSV file with email addresses using the file dialogs.
4. The script will send customized emails to the recipients in the CSV file and display the progress in a tkinter window.
5. Once all emails are sent, the script will display a success message.

Note: Make sure to enable less secure apps access in your Gmail account settings to send emails using SMTP.
