#!/usr/bin/env python 3
from medical_records import MedicalTable, add_medical_record, read_medical_record
from doctor_registration import DoctorRegistration, UpdateRecord
from Patient_registration import PatientRegistration

def main():
    while True:
        print("Welcome to the Hospital Database")
        print("1. Register a new patient")
        print("2. Read a patient's data")
        print("3. Register a new doctor")
        print("4. Read a doctor's infomation")
        print("5. Update a doctor's information")
        print("6. Add a medical record")
        print("7. Read a medical record")
        
        choice = input("Enter the option: ")