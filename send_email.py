#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from doctor_registration import Doctor
from sqlalchemy import engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

sender_email = ""
receiver_email = sender_email
password = ""


# Email content
subject = "Test Email from Python"
body = "This is a test email sent from Python using smtplib."


# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))


class Send_email:
    ''' This class manages send email 
        and notification using smtplib
    '''

    def __init__(self, sender_email, receiver_email, password, subject, body):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.account_password = password
        self.subject = subject
        self.body = body


    def send_email(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(self.sender_email, self.account_password)  # Login to your email account
            server.sendmail(from_addr = self.sender_email,
                        to_addrs = self.receiver_email, msg= message.as_string())  # Send email
            print("Email sent successfully!")


# Run the script
if __name__ == "__main__":
    send_email = Send_email(sender_email, receiver_email, password, subject, body)
    send_email.send_email()
