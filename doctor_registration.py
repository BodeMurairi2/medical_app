#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database URL
DATABASE_URL = "sqlite:///doctors_data.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

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

class DoctorRegistration:
    def registration(self):
        session = Session()
        doctors = {
            "First Name": input('Enter your first name: ').upper(),
            "Last Name": input('Enter your second name: ').upper(),
            "Sex": input("Enter your sex (F or M): ").upper(),
            "Date of Birth": input("Enter your date of birth in yyyy-mm-dd: "),
            "Doctor license": input("Enter your license: ").upper(),
            "email": input("Enter your email address: "),
            "Specialization": input("What's your specialization? ").upper(),
            "Phone Number": input('Enter your phone number (with country code): '),
            "Home Address": input('Enter your home address: '),
            "Is employed": input("Type (yes) if employed or (no) if not: ").upper()
        }
        existing_doctor = session.query(Doctor).filter_by(
            FIRST_NAME=doctors["First Name"],
            LAST_NAME=doctors["Last Name"],
            EMAIL=doctors["email"]
        ).first()
        
        if existing_doctor:
            print(f"Doctor {doctors['First Name']} {doctors['Last Name']} ({doctors['email']}) is already registered.")
            session.close()
            return
        
        new_doctor = Doctor(**doctors)
        session.add(new_doctor)
        session.commit()
        session.close()
        print("Doctor registered successfully!")

    def read_data(self):
        session = Session()
        first_name = input("Write the doctor's first name: ").upper()
        last_name = input("Write the doctor's last name: ").upper()

        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()
        
        if doctor:
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
                f"IS EMPLOYED: {doctor_data['IS_EMPLOYED']}"
            )
        else:
            print("Doctor not found.")
        session.close()

    def delete_record(self):
        session = Session()
        first_name = input("Enter the first name: ").upper()
        last_name = input("Enter second name:  ").upper()
        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()
        
        if not doctor:
            print("Doctor not found.")
            session.close()
            return
        
        choice = input("Do you want to delete? (y or n): ").lower()
        if choice == "y":
            session.delete(doctor)
            session.commit()
            print(f"Doctor: {first_name} {last_name} deleted successfully")
        else:
            print("No information deleted.")
        session.close()

class UpdateRecord(DoctorRegistration):
    def is_retired(self):
        session = Session()
        first_name = input("Enter the first name: ").upper()
        last_name = input("Enter the second name: ").upper()
        age_of_retirement = int(input("Enter the age of retirement: "))
        current_year = datetime.now().year

        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()
        
        if not doctor:
            print("Doctor not found.")
            session.close()
            return
        
        birth_year = int(doctor.DATE_OF_BIRTH.split("-")[0])
        if (current_year - birth_year) > age_of_retirement:
            doctor.IS_EMPLOYED = "RETIRED"
            session.commit()
            print(f"Data updated\nDoctor: {doctor.FIRST_NAME} {doctor.LAST_NAME} is retired")
        else:
            print("No change.")
        session.close()

    def is_dead(self):
        session = Session()
        first_name = input("Enter the first name: ").upper()
        last_name = input("Enter the second name: ").upper()
        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()
        
        if not doctor:
            print("Doctor not found.")
            session.close()
            return
        
        doctor.IS_EMPLOYED = "DEAD"
        session.commit()
        print("Data updated.")
        session.close()

    def detail_changed(self):
        session = Session()
        first_name = input("Enter the first name: ").upper()
        last_name = input("Enter the second name: ").upper()
        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()
        
        if not doctor:
            print("Doctor not found.")
            session.close()
            return

        user_choice = input("What do you want to update (phone number, home address, email): ").upper()
        if user_choice == "PHONE NUMBER":
            doctor.PHONE_NUMBER = input("Insert new phone number: ")
        elif user_choice == "HOME ADDRESS": 
            doctor.HOME_ADDRESS = input("Insert updated Home Address: ")
        elif user_choice == "EMAIL":
            doctor.EMAIL = input("Insert new email address: ")
        else:
            print("No change.")
        
        session.commit()
        session.close()