#!/usr/bin/env python 3
from medical_records import add_medical_records, read_medical_record
from Patient_registration import PatientRegistration
from doctor_registration import DoctorRegistration, UpdateRecord


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
    

if __name__ == "__main__":
    main()