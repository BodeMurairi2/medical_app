#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database URL
DATABASE_URL = "sqlite:///hospital.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Define the ORM Model
Base = declarative_base()

class Patient(Base):  # SQLAlchemy Model
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String)
    address = Column(String, nullable=False)
    national_id = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    registration_date = Column(Date, nullable=False)

    # Ensure the database table exists
Base.metadata.create_all(engine)

class PatientRegistration:
    def register_patient(self):
        session = Session()
        print("Enter patient details:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        middle_name = input("Middle Name (optional): ")
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

        session.add(new_patient)
        session.commit()
        session.close()
        print("Patient registered successfully!")

        def read_patient(self):
        session = Session()
        first_name = input("Enter the patient's first name: ")
        last_name = input("Enter the patient's last name: ")

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
