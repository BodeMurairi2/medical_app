#!/usr/bin/env python3
import hashlib
import getpass
import argparse
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Create the database URL
Database_url = "sqlite://login_details.db"
engine = create_engine(Database_url)
Session = sessionmaker(bind=engine)
session = Session()

# Define the database ORM
base = declarative_base()

class LoginDetails(base):
    __tablename__ = "Login Details"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    hospital_name = Column(String)
    hospital_email = Column(String, unique=True)
    hospital_password = Column(String, unique=False)

# Ensure the database table exists
Base.metadata.create_all(engine)


class Authentication:
    def __init__(self):
        pass
    
    def register_hospital(self):
        hospital_details = {
            "Hospital Name": input("Enter the hospital name").upper(),
            "Hospital Email Address": input("Enter hospital email"),
            "Hospital Password": input("Enter hospital password")
        }
        hospital_credentials = LoginDetails(
            hospital_name = hospital_details["Hospital Name"],
            hospital_email = hospital_details["Hospital Email Address"],
            hospital_password = hash_password(hospital_details["Hospital Password"], 
                                              method='scrypt',
                                              salt_length=16)
        )
        session.add(hospital_credentials)
        session.commit()
        session.close()
        print("Hospital registered successfully")
