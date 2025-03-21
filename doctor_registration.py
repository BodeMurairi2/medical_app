#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the database URL
DATABASE_URL = "sqlite:///doctors_data.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define the ORM Model
Base = declarative_base()

class Doctor(Base):  # SQLAlchemy Model
    __tablename__ = "Doctors"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    FIRST_NAME = Column(String)
    LAST_NAME = Column(String)
    SPECIALIZATION = Column(String)
    LICENSE = Column(String, unique=True)
    DATE_OF_BIRTH = Column(String)
    SEX = Column(String)
    EMAIL = Column(String, unique=False)
    PHONE_NUMBER = Column(String, unique=True)
    HOME_ADDRESS = Column(String)
    IS_EMPLOYED = Column(String)

# Ensure the database table exists
Base.metadata.create_all(engine)

class DoctorRegistration:  # Renamed to avoid conflict
    def __init__(self):
        pass

    def registration(self):
        doctors = {
            "First Name": input('Enter your first name: ').upper(),
            "Last Name": input('Enter your second name: ').upper(),
            "Sex": input("Enter your sex (F or M): ").upper(),
            "Date of Birth": input("Enter your date of birth in yy-mm-dd: "),
            "Doctor license": input("Enter your license: ").upper(),
            "email": input("Enter your email address: "),
            "Specialization": input("What's your specialization? ").upper(),
            "Phone Number": input('Enter your phone number (with country code): '),
            "Home Address": input('Enter your home address: '),
            "Is employed": input("Type (yes) if employed or (no) if not").upper()
        }
        # Check if the doctor already exists
        existing_doctor = session.query(Doctor).filter_by(
            FIRST_NAME=doctors["First Name"],
            LAST_NAME=doctors["Last Name"],
            EMAIL=doctors["email"]
            ).first()

        if existing_doctor:
            print(f"Doctor {doctors['First Name']} {doctors['Last Name']} ({doctors['email']}) is already registered.")
            return

        # New record into the database
        new_doctor = Doctor(
            FIRST_NAME= doctors["First Name"],
            LAST_NAME= doctors["Last Name"],
            SPECIALIZATION= doctors["Specialization"],
            LICENSE= doctors["Doctor license"],
            DATE_OF_BIRTH= doctors["Date of Birth"],
            SEX= doctors["Sex"],
            EMAIL= doctors["email"],
            PHONE_NUMBER= doctors["Phone Number"],
            HOME_ADDRESS= doctors["Home Address"],
            IS_EMPLOYED= doctors["Is employed"]
        )
        session.add(new_doctor)
        session.commit()
        session.close()
        print("Doctor registered successfully!")


    def read_data(self):
        first_name = input("Write the doctor first name\n").upper()
        last_name = input("Write the doctor last name\n").upper()

        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()

        if doctor:
            # Convert SQLAlchemy object to dictionary and exclude private attributes
            doctor_data = {column.name: getattr(doctor, column.name) for column in doctor.__table__.columns}

            print("_____________________________________________________________________")
            print("Doctor Information\n")
            print(
                f"FIRST NAME: {doctor_data['FIRST_NAME']}\n"
                f"LAST NAME: {doctor_data['LAST_NAME']}\n"
                f"SPECIALIZATION: {doctor_data['SPECIALIZATION']}\n"
                f"LICENSE: {doctor_data['LICENSE']}\n"
                f"EMAIL: {doctor_data['EMAIL']}\n"
                f"PHONE NUMBER: {doctor_data['PHONE_NUMBER']}\n"
                f"HOME ADDRESS: {doctor_data['HOME_ADDRESS']}\n"
                f"IS EMPLOYED: {doctor_data["IS_EMPLOYED"]}"
            )
        else:
            print("Doctor not found.")

    def delete_record(self):
        first_name = input("Enter the first name: ").upper()
        last_name = input("Enter second name:  ").upper()
        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()
        choice = input("Do you want to delete?  (y or n)").lower()
        if choice == "y":
            session.delete(doctor)
            session.commit()
            session.close()
            print(f"Doctor: {first_name} {last_name} deleted successfully")
        else:
            print("No information deleted")

class Update_record(DoctorRegistration):
    def is_retired():
        pass



a_doc = DoctorRegistration()
#a_doc.registration()
#a_doc.read_data()
a_doc.delete_record()