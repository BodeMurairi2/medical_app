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

# Ensure the database table exists
Base.metadata.create_all(engine)

class DoctorRegistration:  # Renamed to avoid conflict
    def __init__(self):
        self.doctors = {
            "First Name": input('Enter your first name: ').upper(),
            "Last Name": input('Enter your second name: ').upper(),
            "Sex": input("Enter your sex (F or M): ").upper(),
            "Date of Birth": input("Enter your date of birth in yy-mm-dd: "),
            "Doctor license": input("Enter your license: ").upper(),
            "email": input("Enter your email address: "),
            "Specialization": input("What's your specialization? ").upper(),
            "Phone Number": input('Enter your phone number (with country code): '),
            "Home Address": input('Enter your home address: ')
        }
