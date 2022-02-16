import smtplib, getpass, ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender_email = input("Enter Sender Email: ")
receiver_email = input("Enter Receiver Email: ")
password = getpass.getpass("Enter Password: ")
subject = "CLOC Output File"
content = "Email Sent from Python"


msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

filename = 'output.txt'
with open(filename,'r') as f:
    attachment = MIMEApplication(f.read(), Name=basename(filename))
    attachment['Content-Disposition'] = 'attachement; filename="{}"'.format(basename(filename))


msg.attach(attachment)



server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, password)
server.send_message(msg, sender_email, receiver_email)