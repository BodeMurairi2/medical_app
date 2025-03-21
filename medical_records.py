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
    record_id = Column(Integer,primary_key=True, autoincrement=True, nullable=False)
    patient_id = Column (Integer, ForeignKey=("patient_table.id"), nullable=False)
    diagnosis = Column(String)
    prescription = Column (String)
    doctor_name = Column(String, nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc)) 

# create the database
#Base.metadata.create_all(engine)

#Add data to the table

def add_medical_data():
    session = Session()
    
    patient_id = int(input("Enter patient ID:"))
    diagnosis = input("Enter Diagnosis: ")
    prescription = input("Enter prescription:")
    doctor_name = input("Enter Doctor's Name:")

    new_record = MedicalTable(
        patient_id=patient_id,
        diagnosis=diagnosis,
        prescription=prescription,
        doctor_name=doctor_name
        )

    # Add and commit the new record
    session.add(new_record)
    session.commit()
    print("\n Medical record added successfully!")

if __name__ == "__main__":
    add_medical_data()




    






    

