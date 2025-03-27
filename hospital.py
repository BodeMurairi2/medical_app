#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone 
import uuid

# Define the database URL
DATABASE_URL = "sqlite:///hospital.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Define the ORM Model
Base = declarative_base()

class Patient(Base):  # SQLAlchemy Model
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String)
    address = Column(String, nullable=False)
    national_id = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    registration_date = Column(Date, nullable=False, default=datetime.now)

    # Establish relationship with MedicalRecord
    medical_records = relationship("MedicalRecord", back_populates="patient", lazy='dynamic')

class MedicalRecord(Base):
    __tablename__ = "medical_records"
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    diagnosis = Column(String)
    prescription = Column(String)
    doctor_name = Column(String, nullable=False)
    exam_name = Column(String, nullable=False)
    exam_no = Column(String, nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationship to the Patient table
    patient = relationship("Patient", back_populates="medical_records")

# Ensure the database tables exist
Base.metadata.create_all(engine)

class PatientRegistration:
    def __init__(self):
        pass

    def register_patient(self):
        """Registers a new patient in the database."""
        session = Session()
        print("Enter patient details:")
        first_name = input("First Name: ").upper()
        last_name = input("Last Name: ").upper()
        middle_name = input("Middle Name (optional): ").upper()
        address = input("Address: ")
        national_id = input("National ID or Passport ID: ")
        email = input("Email Address: ")
        gender = input("Gender: ")
        phone = input("Phone Number: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        registration_date = datetime.now().date()  # Use date directly

        # Create a Patient instance
        new_patient = Patient(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            address=address,
            national_id=national_id,
            email=email,
            gender=gender,
            phone=phone,
            dob=datetime.strptime(dob, "%Y-%m-%d").date(),  # Convert to date
            registration_date=registration_date
        )

        # Check for existing patient
        existing_patient = session.query(Patient).filter_by(
            first_name=first_name,
            last_name=last_name,
            email=email
        ).first()

        if existing_patient:
            print(f"Patient {first_name} {last_name} ({email}) is already registered.")
            session.close()
            return

        try:
            session.add(new_patient)
            session.commit()
            print("Patient registered successfully!")
        except IntegrityError:
            session.rollback()
            print("Error: Unable to register patient.")
        finally:
            session.close()

    def read_patient(self):
        """Reads and displays patient information from the database."""
        session = Session()
        first_name = input("Enter the patient's first name: ").upper()
        last_name = input("Enter the patient's last name: ").upper()

        patient = session.query(Patient).filter_by(first_name=first_name, last_name=last_name).first()

        if patient:
            print("_____________________________________________________________________")
            print("Patient Information\n")
            print(
                f"FIRST NAME: {patient.first_name}\n"
                f"LAST NAME: {patient.last_name}\n"
                f"MIDDLE NAME: {patient.middle_name}\n"
                f"ADDRESS: {patient.address}\n"
                f"NATIONAL ID: {patient.national_id}\n"
                f"EMAIL: {patient.email}\n"
                f"GENDER: {patient.gender}\n"
                f"PHONE: {patient.phone}\n"
                f"DOB: {patient.dob}\n"
                f"REGISTRATION DATE: {patient.registration_date}"
            )
        else:
            print("Patient not found.")
        session.close()


class MedicalRecordManagement:
    def __init__(self):
        pass

    def add_medical_record(self):
        """Adds a new medical record to the database."""
        session = Session()
        first_name = input("Enter the patient's first name: ").strip().upper()
        last_name = input("Enter the patient's last name: ").strip().upper()

        # Find the patient by name
        patient = session.query(Patient).filter_by(first_name=first_name, last_name=last_name).first()

        if not patient:
            print("ERROR! Patient not found. Please ensure the patient's details are correct.")
            return

        diagnosis = input("Enter the diagnosis: ").strip()
        prescription = input("Enter the prescription: ").strip()
        doctor_name = input("Enter the doctor's name: ").strip()
        exam_name = input("Enter the exam name: ").strip()
        exam_no = str(uuid.uuid4()).split('-')[0]

        if not diagnosis or not prescription or not doctor_name or not exam_name or not exam_no:
            print("Error! All the fields should not be empty")
            return 


        new_record = MedicalRecord(
            patient_id=patient.id,
            diagnosis=diagnosis,
            prescription=prescription,
            doctor_name=doctor_name,
            exam_name=exam_name,
            exam_no=exam_no
        )

        try:
            session.add(new_record)
            session.commit()
            print("Medical record added successfully.")
        except IntegrityError:
            session.rollback()
            print("Error: Unable to add medical record.")
        finally:
            session.close()

    def read_medical_record(self):
        """Reads and displays a medical record from the database."""
        session = Session()
        first_name = input("Enter the patient's first name: ").strip().upper()
        last_name = input("Enter the patient's last name: ").strip().upper()

        # Find the patient by name
        patient = session.query(Patient).filter_by(first_name=first_name, last_name=last_name).first()

        if not patient:
            print("ERROR! Patient not found. Please ensure the patient's details are correct.")
            return

        record = session.query(MedicalRecord).filter_by(patient_id=patient.id).first()

        if record:
            print("____________________________________________________________")
            print("Medical Record:")
            print(
                f"Record ID: {record.id}\n"
                f"Patient ID: {record.patient_id}\n"
                f"Diagnosis: {record.diagnosis}\n"
                f"Prescription: {record.prescription}\n"
                f"Doctor Name: {record.doctor_name}\n"
                f"Exam Name: {record.exam_name}\n"
                f"Exam Order: {record.exam_no}\n"
                f"Date: {record.date}"
            )
        else:
            print("Record not found.")
        session.close()

if __name__ == "__main__":
    patient_registration = PatientRegistration()
    medical_record_management = MedicalRecordManagement()