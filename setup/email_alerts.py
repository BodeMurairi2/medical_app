#!/usr/bin/env python3

import os
import smtplib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
from hospital import Patient, MedicalRecord
from fpdf import FPDF
from datetime import datetime

# ..........................connecting with the database..............

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

# Load environment variables from .env file
load_dotenv()

# Format date and time
formatted_date = record.date.strftime('%Y-%m-%d %H:%M')


class Notifications:
    def __init__(self, sender_email, receiver_email, password, subject, body, attachment_path=None):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.account_password = password
        self.subject = subject
        self.body = body
        self.attachment_path = attachment_path

    def email_alert(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = self.subject
        msg['To'] = self.receiver_email
        msg['From'] = self.sender_email

        if self.attachment_path:
            with open(self.attachment_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(self.attachment_path)
                msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

        # Ensure credentials are set
        if not self.sender_email or not self.account_password:
            print("Email credentials are missing. Check your .env file.")
            return

        if not patient_record:
            print(f"Patient with name {first_name} {last_name} not in our database: ")
            return

        # Send email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.sender_email, self.account_password)
            server.send_message(msg)
            server.quit()
            print(f"✅ Report sent successfully to {self.receiver_email}")
        except Exception as e:
            print(f"X Error sending email: {e}")


def create_pdf(patient_record, record, formatted_date):
    gender = patient_record.gender
    if gender == "M":
        receiver_gender = "Mr."
    else:
        receiver_gender = "Ms/Mrs."
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hospital Saint Trinity", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Dear {receiver_gender} {patient_record.first_name} {patient_record.last_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"National ID: {patient_record.national_id}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Exam name: {record.exam_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Exam number: {record.exam_no}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Diagnosis: {record.diagnosis}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Prescription: {record.prescription}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Consultation realized by Dr.{record.doctor_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Date and time of visit: {formatted_date}", ln=True, align='L')
    pdf_output_path = os.path.join(instance_dir, "medical_report.pdf")
    pdf.output(pdf_output_path)
    return pdf_output_path


def send_report():
    formatted_date = record.date.strftime('%Y-%m-%d %H:%M')
    pdf_path = create_pdf(patient_record, record, formatted_date)
    notification = Notifications(
        sender_email=os.getenv("sender"),
        receiver_email=patient_record.email,
        password=os.getenv("password"),
        subject=f"Medical record {formatted_date}",
        body=f"Please find attached your medical record report.",
        attachment_path=pdf_path
    )
    notification.email_alert()


if __name__ == '__main__':
    send_report()
