#!/usr/bin/env python3
# This script handles doctors data in our medical files database
import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


# Define the database URL
DATABASE_URL = "sqlite:///doctors_data.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


# Define the ORM Model
Base = declarative_base()


class Doctor(Base):
    __tablename__ = "Doctors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    FIRST_NAME = Column(String)
    LAST_NAME = Column(String)
    SPECIALIZATION = Column(String)
    LICENSE = Column(String)
    DATE_OF_BIRTH = Column(String)
    SEX = Column(String)
    EMAIL = Column(String)
    PHONE_NUMBER = Column(String)
    HOME_ADDRESS = Column(String)


# Create tables
Base.metadata.create_all(engine)




class DocteurRegistration:
    '''
    Class that handles docteur registration
    '''
    def __init__(self):
        self.docteurs = {
            "first_name": input("Enter first name: "),
            "last_name": input("Enter last name: "),
            "specialization": input("Enter specialization: "),
            "license": input("Enter license: "),
            "date_of_birth": input("Enter date of birth 'YY-MM-DD': "),
            "sex": input("Enter M or F: "),
            "email": input("Enter email: "),
            "phone": input("Enter phone number: "),
            "home_address": input("Enter home address: ")
        }
        pass

    def registration(self):

        '''
        This function records the registration
        :return: Registration status/complete
        '''


        nbr_doctors = int(input("Enter the number of doctors you want to register: "))

        for count in range(nbr_doctors):
            new_doctor = Doctor(
                FIRST_NAME= self.docteurs["first_name"],
                LAST_NAME = self.docteurs["last_name"],
                SPECIALIZATION = self.docteurs["specialization"],
                LICENSE = self.docteurs["license"],
                DATE_OF_BIRTH = self.docteurs["date_of_birth"],
                SEX = self.docteurs["sex"],
                EMAIL = self.docteurs["email"],
                PHONE_NUMBER = self.docteurs["phone"],
                HOME_ADDRESS = self.docteurs["home_address"]
            )
            session.add(new_doctor)
            session.commit()
            session.close()

        print("Registration successful!")


    def read_record(self):
        all_doctors = session.query(Doctor).all()
        doctor_list = [doctor.__dict__ for doctor in all_doctors]
        print(doctor_list)


    def update_record(self):
        pass


    def delete_record(self):
        pass

if __name__ == "__main__":
    doc = DocteurRegistration()
    doc.registration()
    doc.read_record()
