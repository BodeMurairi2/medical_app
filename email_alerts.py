import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to

    # Get credentials from environment variables
    user = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    msg['From'] = user

    if not user or not password:
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

if __name__ == '__main__':
    email_alert("Medical record", "Attached is the medical report", "f.irakoze2@alustudent.com")