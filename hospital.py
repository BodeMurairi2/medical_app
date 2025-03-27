#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone

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
    exam_order = Column(String, nullable=False)
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