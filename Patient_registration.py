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
