from celery import Celery
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv(".env")

app = Celery('app', broker='pyamqp://guest:guest@rabbitmq//')

@app.task
def send_confirmation_email(user_email):
    msg = MIMEMultipart()
    msg['From'] = os.environ["YOUR_GMAIL"]
    msg['To'] = user_email
    msg['Subject'] = 'Register confirmation'

    body = 'Thank you for registering!'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(os.environ["YOUR_GMAIL"], os.environ["EMAIL_TOKEN"])
    server.send_message(msg)
    server.quit()