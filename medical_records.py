#Imports 
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
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
    patient_id = Column (Integer, nullable=False)
    diagnosis = Column(String)
    prescription = Column (String)
    doctor_name = Column(String, nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc)) 

# create the database
Base.metadata.create_all(engine)

# A function to add data to the table
# class MedicalData:
#     def __init__(self, patient_id, diagnosis, prescription, doctor_name):
#         self.patient_id = patient_id
#         self.diagnosis = diagnosis
#         self.prescription = prescription
#         self.doctor_name = doctor_name
        
def add_medical_records():
    patient_id = input("Enter the patient ID: ").strip()
    diagnosis = input("Enter the diagnosis: ").strip()
    prescription = input("Enter the prescription: ").strip()
    doctor_name = input("Enter the doctor's name: ").strip()
    
    if not patient_id or not diagnosis or not prescription or not doctor_name:
        print("ERROR! All the field are required.")
        return
    
    # patient_exists = session.query(patient_table).filter_by(id=patient_id).first()

    # if not patient_exists:
    #     print("ERROR! Patient ID does not exist. Enter a valid ID")
    #     return
    
    new_record = MedicalTable(
        patient_id=patient_id,
        diagnosis=diagnosis,
        prescription=prescription,
        doctor_name=doctor_name
    )


    try:
        session.add(new_record)
        session.commit()
        print("Record added successfuly")

    except Exception as e:
        session.rollback()
        print(f"Database error {e}")
    session.close()

add_medical_records()

# A function to read data from the medical records table

def read_medical_record():
    session = Session() 
    patient_id = input("Enter patient_id: ")
    
    record = session.query(MedicalTable).filter_by(patient_id = patient_id).first()

    if record:
        print("____________________________________________________________")
        print("Medical Record:")
        print(
            f"Record ID: {record.record_id}\n"
            f"Patient ID: {record.patient_id}\n"
            f"Diagnosis: {record.diagnosis}\n"
            f"Prescription: {record.prescription}\n"
            f"Doctor Name: {record.doctor_name}\n"
            f"Date: {record.date}"

        )
    else:
        print("Record not found")
    session.close()

read_medical_record()
