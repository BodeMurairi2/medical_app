#!/usr/bin/env python3
import os
import time
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hospital import Patient, MedicalRecord
from dotenv import load_dotenv
from datetime import datetime



#..........................connecting with the database..............

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Ensure the 'instance' directory exists within the setup directory
instance_dir = os.path.join(script_dir, "instance")
os.makedirs(instance_dir, exist_ok=True)

# Define the database URL using a relative path within the setup directory
DATABASE_URL = f"sqlite:///{os.path.join(instance_dir, 'hospital.db')}"

# Create SQLAlchemy engines
engine = create_engine(DATABASE_URL, echo=True)


# Create session factories
SessionLocal1 = sessionmaker(bind=engine)


session = SessionLocal1()


first_name = input("Enter the patient first name: \n").upper()
last_name = input("Enter the patient last name: \n").upper()

# Search for the patient
patient_record = session.query(Patient).filter_by(first_name=first_name, last_name=last_name).first()

if not patient_record:
    print("ERROR! Patient not found. Please ensure the patient's details are correct.")
else:
    # Retrieve medical record only if patient exists
    record = session.query(MedicalRecord).filter_by(patient_id=patient_record.id).first()

    if not record:
        print("ERROR! Medical record not found for this patient.")

# Close sessions
session.close()
session.close()

# Load environment variables from .env file
load_dotenv()

formatted_date = record.date.strftime('%Y-%m-%d %H:%M')


class SendingReminders:
    def __init__(self, sender_email, receiver_email, password, subject, body, attachment_path=None):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.account_password = password
        self.subject = subject
        self.body = body

    def sending_reminders(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = self.subject
        msg['To'] = self.receiver_email
        msg['From'] = self.sender_email

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
            print(f"✅ Reminders sent successfully {self.receiver_email}")
        except Exception as e:
            print(f"X Error sending email: {e}")

def send_reminder():
    formatted_date = record.date.strftime('%Y-%m-%d %H:%M')
    reminders = SendingReminders(
        sender_email=os.getenv("sender"),
        receiver_email=patient_record.email,
        password=os.getenv("password"),
        subject=f"Reminder {formatted_date}",
        body=f"Dear {patient_record.first_name} {patient_record.last_name}\n"
        f"This is your daily reminder to take your medecation: \n"
        f"{record.prescription}\n"
        "Hospital Saint Trinity",
    )
    reminders.sending_reminders()



if __name__ == "__main__":
    send_reminder()