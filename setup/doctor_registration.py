#!/usr/bin/env python3

import os
import time
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Ensure the 'instance' directory exists within the setup directory
instance_dir = os.path.join(script_dir, "instance")
os.makedirs(instance_dir, exist_ok=True)
DATABASE_URL = f"sqlite:///{os.path.join(instance_dir, 'doctors.db')}"

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
    '''
    Class to handle doctors information
    '''

    def __init__(self):
        pass

    def registration(self):
        '''
        Registration function
        '''
        session = Session()
        doctors = {
            "FIRST_NAME": input('Enter your first name: ').upper(),
            "LAST_NAME": input('Enter your second name: ').upper(),
            "SEX": input("Enter your sex (F or M): ").upper(),
            "DATE_OF_BIRTH": input("Enter your date of birth in yyyy-mm-dd: "),
            "LICENSE": input("Enter your license: ").upper(),
            "EMAIL": input("Enter your email address: "),
            "SPECIALIZATION": input("What's your specialization? ").upper(),
            "PHONE_NUMBER": input('Enter your phone number (with country code): '),
            "HOME_ADDRESS": input('Enter your home address: '),
            "IS_EMPLOYED": input("Type (yes) if employed or (no) if not: ").upper()
        }

        existing_doctor = session.query(Doctor).filter_by(
            FIRST_NAME=doctors["FIRST_NAME"],
            LAST_NAME=doctors["LAST_NAME"],
            EMAIL=doctors["EMAIL"]
        ).first()

        if existing_doctor:
            print(f"Doctor {doctors['FIRST_NAME']} {doctors['LAST_NAME']} ({doctors['EMAIL']}) is already registered.")
            session.close()
            return

        new_doctor = Doctor(**doctors)
        session.add(new_doctor)
        session.commit()
        session.close()
        print("Doctor registered successfully!\n")
        print("Returning to the main menu...\n")
        time.sleep(2)

    def read_data(self):
        '''
        Read Doctor information
        Function
        Loading data from sqlite
        '''
        session = Session()
        first_name = input("Enter the first name: ").upper()
        last_name = input("Enter second name:  ").upper()
        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()

        if not doctor:
            print("Doctor not found.")
            print("Main Menu...\n")
            session.close()
            return

        print("Loading doctor information...\n")
        time.sleep(2)
        print("_________________________________________________________")
        print(f"Doctor First Name: {doctor.FIRST_NAME}\n"
              f"Doctor Last Name: {doctor.LAST_NAME}\n"
              f"Doctor Specialization: {doctor.SPECIALIZATION}\n"
              f"Doctor License: {doctor.LICENSE}\n"
              f"Doctor Email: {doctor.EMAIL}\n"
              f"Doctor Phone Number: {doctor.PHONE_NUMBER}\n"
              f"Doctor Home Address: {doctor.HOME_ADDRESS}\n"
              f"Doctor Employment status: {doctor.IS_EMPLOYED}\n"
              )
        print("________________________________________________________")
        print("Doctor information reads successffuly\n")
        print("Returning to the main menu...\n")
        time.sleep(2)

        session.close()

    def update(self):
        '''
        Function to handle update information
        '''
        session = Session()
        first_name = input("Enter the first name: ").upper()
        last_name = input("Enter the second name: ").upper()
        doctor = session.query(Doctor).filter_by(FIRST_NAME=first_name, LAST_NAME=last_name).first()

        if not doctor:
            print("Doctor not found.")
            print("Main menu...\n")
            session.close()
            time.sleep(2)
            return

        user_choice = input(
            "What do you want to update (phone number, 2.home address, 3.email, 4.employment status): ").upper()
        if user_choice == "PHONE NUMBER":
            doctor.PHONE_NUMBER = input("Insert new phone number: ")
            print(f"Phone number for {doctor.FIRST_NAME} {doctor.LAST_NAME} changed successfully\n")
            print(f"Returning to the main menu...\n")
            time.sleep(2)
        elif user_choice == "HOME ADDRESS":
            doctor.HOME_ADDRESS = input("Insert updated Home Address: ")
            print(f"Home Address for {doctor.FIRST_NAME} {doctor.LAST_NAME} changed successfully\n")
            print(f"Returning to the main menu...\n")
            time.sleep(2)
        elif user_choice == "EMAIL":
            doctor.EMAIL = input("Insert new email address: ")
            print(f"Email Address for {doctor.FIRST_NAME} {doctor.LAST_NAME} changed successfully\n")
            print(f"Returning to the main menu...\n")
            time.sleep(2)
        elif user_choice == "EMPLOYMENT STATUS":
            doctor.IS_EMPLOYED = input("Insert updated employment status")
            print(f"Employment status for {doctor.FIRST_NAME} {doctor.LAST_NAME} changed successfully")
            print(f"Returning to the main menu...\n")
            time.sleep(2)
        else:
            print("No change.\n")
            print(f"Returning to the main menu...\n")
            time.sleep(2)

        session.commit()
        session.close()


if __name__ == "__main__":
    doctor_registration = DoctorRegistration()
