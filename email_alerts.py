import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env


class Notifications:
    def __init__(self, sender_email, receiver_email, password, subject, body, to):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.account_password = password
        self.subject = subject
        self.body = body
        self.to =  to
    
    def email_alert(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = self.subject
        msg['To'] = self.to

        # Get credentials from environment variables
        self.sender_email = os.getenv("EMAIL_USER")
        self.account_password = os.getenv("EMAIL_PASS")
        msg['From'] = self.account_password

        if not self.sender_email or not self.account_password:
            raise ValueError("Email credentials are missing. Set EMAIL_USER and EMAIL_PASS as environment variables.")

        # Send email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
            server.quit()
            print(f"Email sent successfully to {to}")
        except Exception as e:
            print(f"Error sending email: {e}")




def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to

    
if __name__ == '__main__':
    email_alert("Medical record", "Attached is the medical report", "f.irakoze2@alustudent.com")