import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debugging: Print to check if variables are loaded correctly
print("Sender Email:", os.getenv("sender"))
print("Password:", os.getenv("password"))
print("Receiver Email:", os.getenv("receiver"))

class Notifications:
    def __init__(self, sender_email, receiver_email, password, subject, body):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.account_password = password
        self.subject = subject
        self.body = body
    
    def email_alert(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = self.subject
        msg['To'] = self.receiver_email
        msg['From'] = self.sender_email  # FIXED: Use sender email here

        # Ensure credentials are set
        if not self.sender_email or not self.account_password:
            raise ValueError("Email credentials are missing. Check your .env file.")

        # Send email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.sender_email, self.account_password)
            server.send_message(msg)
            server.quit()
            print(f"✅ Email sent successfully to {self.receiver_email}")
        except Exception as e:
            print(f"X Error sending email: {e}")


class Sending_reminders(Notifications):
    def sending_reminders(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = self.subject
        msg['To'] = self.receiver_email
        msg['From'] = self.sender_email  # FIXED: Use sender email here

        # Ensure credentials are set
        if not self.sender_email or not self.account_password:
            raise ValueError("Email credentials are missing. Check your .env file.")

        # Send email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.sender_email, self.account_password)
            server.send_message(msg)
            server.quit()
            print(f"✅ Email sent successfully to {self.receiver_email}")
        except Exception as e:
            print(f"X Error sending email: {e}")



if __name__ == '__main__':
    notification = Notifications(
        sender_email=os.getenv("sender"),
        receiver_email=os.getenv("receiver"),
        password=os.getenv("password"),
        subject="Medical record",
        body="Attached is the medical report"
    )
    notification.email_alert()
