class Patient:
    def __init__(self, first_name, last_name, middle_name, address,
                 national_id, email, gender, phone, dob, registration_date):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.address = address
        self.national_id = national_id
        self.email = email
        self.gender = gender
        self.phone = phone
        self.dob = dob
        self.registration_date = registration_date

def register_patient():
    print("Enter patient details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    middle_name = input("Middle Name (optional): ")
    address = input("Address: ")
    national_id = input("National ID or Passport ID: ")
    email = input("Email Address: ")
    gender = input("Gender: ")
    phone = input("Phone Number: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    registration_date = datetime.now().strftime("%Y-%m-%d")

    # Create a Patient instance
    patient = Patient(first_name, last_name, middle_name, address,
                      national_id, email, gender, phone, dob, registration_date)
    
    # Save to the database
    insert_patient(patient)
    print("Patient registered successfully.")

def main():
    create_table()  # Ensure the table is created before starting registration
    while True:
        print("\nHospital Registration System")
        print("1. Register Patient")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_patient()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()