from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass

sender = "your_email@gmail.com"
username = "Your Name"
password = getpass.getpass("Password: ")
host = "smtp.gmail.com"
port = 587
recipient = input("Student email: ")
score = float(input("Score: "))
body = f"Your score on the last exam is {score}\n"

if score <= 50:
    body += "To do better next time, why not visit the tutoring center?"
elif score >= 90:
    body += "Fantastic job! Keep it up."

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = "Exam score"
msg.attach(MIMEText(body, "plain"))

# Sending the message
try:
    with smtplib.SMTP(host, port) as server:
        server.starttls()  # Secure communication with TLS
        server.login(username, password)
        server.send_message(msg)
        print("Email sent successfully.")
except Exception as e:
    print("An error occurred:", e)

