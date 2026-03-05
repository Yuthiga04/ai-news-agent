import os
import smtplib
from email.mime.text import MIMEText

def send_email(summary):

    msg = MIMEText(summary)
    msg["Subject"] = "Daily AI News Brief"
    msg["From"] = "yuthiga04@gmail.com"
    msg["To"] = "yuthiga04@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("yuthiga04@gmail.com", os.getenv("vsmqticbfybynnba"))

    server.send_message(msg)
    server.quit()