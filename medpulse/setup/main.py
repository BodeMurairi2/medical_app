#!/usr/bin/env python3

import time
from hospital import PatientRegistration, MedicalRecordManagement
from doctor_registration import DoctorRegistration


def main():
    while True:
        patient_registration = PatientRegistration()
        medical_record_management = MedicalRecordManagement()
        doctor_registration = DoctorRegistration()

        print("WELCOME TO MEDPULSE")
        print("MAIN MENU")
        print("________________________________________________________\n")
        print("1. Register a new patient")
        print("2. Read a patient's data")
        print("3. Register a new doctor")
        print("4. Read a doctor's infomation")
        print("5. Update a doctor's information")
        print("6. Add a medical record")
        print("7. Read a medical record")
        print("8. Exit")

        choice = int(input("Enter the option: "))
        if choice == 1:
            patient_registration.register_patient()
        elif choice == 2:
            patient_registration.read_patient()
        elif choice == 3:
            doctor_registration.registration()
        elif choice == 4:
            doctor_registration.read_data()
        elif choice == 5:
            doctor_registration.update()
        elif choice == 6:
            medical_record_management.add_medical_record()
        elif choice == 7:
            medical_record_management.read_medical_record()
        elif choice == 8:
            print("Exiting Application...")
            time.sleep(2)
            print("Exit successfully!!")
            break
        else:
            print("Error! Choose between 1-8")
            continue


if __name__ == "__main__":
    main()
