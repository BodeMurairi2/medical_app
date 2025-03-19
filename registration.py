#!/usr/bin/env python3
# This script handles doctors data in our medical files database
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
    id = Column(Integer, primary_key= True, unique=True, autoincrement=True)
    FIRST_NAME = Column(String)
    LAST_NAME = Column(String)
    SPECIALIZATION = Column(String)
    LICENSE = Column(String, unique= True)
    DATE_OF_BIRTH = Column(String)
    SEX = Column(String)
    EMAIL = Column(String, unique= True)
    PHONE_NUMBER = Column(String, unique= True)
    HOME_ADDRESS = Column(String)



# Create tables
Base.metadata.create_all(engine)


class DocteurRegistration:
    '''
    Class that handles docteur registration
    '''
    def __init__(self):
        pass


    def registration(self):

        '''
        This function records the registration
        :return: Registration status/complete
        '''


        nbr_doctors = int(input("Enter the number of doctors you want to register: "))
        doctors = {
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


        for count in range(nbr_doctors):
            new_doctor = Doctor(
                FIRST_NAME= doctors["first_name"],
                LAST_NAME = doctors["last_name"],
                SPECIALIZATION = doctors["specialization"],
                LICENSE = doctors["license"],
                DATE_OF_BIRTH = doctors["date_of_birth"],
                SEX = doctors["sex"],
                EMAIL = doctors["email"],
                PHONE_NUMBER = doctors["phone"],
                HOME_ADDRESS = doctors["home_address"]
            )
            session.add(new_doctor)
            session.commit()
            session.close()

        print("Registration successful!")


    def read_record(self):
        all_doctors = session.query(Doctor).all()
        doctor_list = [doctor.__dict__ for doctor in all_doctors]
        for i in doctor_list:
            print(i.values())
        #print(first_element)


    def update_record(self):
        pass


    def delete_record(self):
        pass

if __name__ == "__main__":
    doc = DocteurRegistration()
    doc.read_record()
