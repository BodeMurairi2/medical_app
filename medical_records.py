#Imports 
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from sqlalchemy import DateTime
from datetime import datetime, timezone

#create your database
engine = create_engine("sqlite:///medicalrecords.db",echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Define models
class MedicalTable(Base):
    __tablename__="medical_record"
    record_id = Column(Integer,primary_key=True, nullable=False)
    patient_id = Column (Integer, ForeignKey=True, nullable=False)
    diagnosis = Column(String)
    prescription = Column (String)
    doctor_name = Column(String, nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))



    


