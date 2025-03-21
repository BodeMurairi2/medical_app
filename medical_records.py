#Imports 
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#create your database
engine = create_engine("sqlite:///medicalrecords.db",echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Define models
class MedicalTable(Base):
    _tablename_="medical_record"
    record_id = Column(Integer,primary_key=True, nullable=False)
    patient_id = Column (Integer, ForeignKey=True, nullable=False)
    diagnosis = Column(String)
    prescription = Column (String)
    doctor_name = Column(String, nullable=False)
    date = Column(datetime)



    


