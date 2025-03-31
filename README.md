 Hospital Management System

Overview

This project is a Hospital Management System built using Python and SQLAlchemy. It provides functionalities for patient registration, medical record management, hospital authentication, and email notifications.

Features
- Patient Registration: Add, view, and delete patient records.
- Medical Records Management: Store and retrieve patient diagnoses and prescriptions.
- Email Notifications: Send email notifications using SMTP.

File Structure
doctor_registration.py: Handles doctor registration and storage.
email_alerts.py: Manages email notifications for patients.
hospital.py: (Referenced but not provided) Likely manages patient and medical record classes.
.env (Not included in repo): Stores sensitive email credentials.

 Project Structure
```
├── medical_records.py     # Manages patient medical records
├── Patient_registration.py # Manages patient registration
├── send_email.py          # Handles email notifications
```

Setup Instructions
- Prerequisites
- Python 3.x
- SQLite
- Required Python libraries: `sqlalchemy`, `smtplib`, `dotenv`,'fpdf'

Installation
1. Clone this repository:
   ```sh
   git clone <https://github.com/BodeMurairi2/medical_app.git>
   cd hospital-management-system
   ```
2. Install dependencies:
   ```sh
   pip install sqlalchemy python-dotenv
   ```


 Sending Emails
```sh
python send_email.py
```
Contributors
- Blessing Ingabire  (b.ingabire1@alustudent.com)
- Faith Irakoze  (f.irakoze2@alustudent.com)
- Tifare Kaseke (t.kaseke@alustudent.com)
- Divine Kuzo (d.kuzo@alustudent.com)
- Pascal Nsigo (p.nsigo@alustudent.com)
- Maurice Nshimyumukiza (m.nshimyumu@alustudent.com)
- Bode Murairi (b.murairi@alustudent.com)




