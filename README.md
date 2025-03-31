 Medical_app System

Description
This is a Python-based Hospital Management System that allows patient registration, medical record management, and email notifications for medical reports. The system utilizes SQLite for database storage and SQLAlchemy as the ORM. It also supports automated email notifications using Gmail SMTP.

Features
- Patient Registration: Register new patients with details like name, address, national ID, email, gender, phone, and date of birth.
- Medical Record Management: Add and retrieve medical records associated with patients.
- Email Notifications: Automatically send medical reports to patients via email.
- PDF Report Generation: Generate medical reports in PDF format before sending them via email.

 Project Structure

    doctor_registration.py : Manages doctor registration (if applicable)
    email_alerts.py: Handles email notifications and PDF generation
    hospital.py : Defines database models and medical record management
    pyvenv.cfg : Python virtual environment configuration
    instance/ : Contains the SQLite database and generated PDFs
    README.md : Project documentation


Installation
1.Clone the repository
   
   git clone https://github.com/BodeMurairi2/medical_app.git
   cd medical_app
   

2. Create and activate a virtual environment
   
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies

   pip install -r requirements.txt
   

4. Set up environment variables
   Create a `.env` file in the root directory and add the following:

   sender=your-email@gmail.com
   password=your-email-password
   

5. Run the application
   
   python hospital.py : Initializes the database
   python email_alerts.py : Starts the email notification process
   

Usage
- Register a new patient: Run `hospital.py` and follow the prompts.
- Add a medical record: Input patient details and enter their medical history.
- Send a medical report via email: `email_alerts.py` retrieves a patient's record, generates a PDF, and emails it.

Requirements
- Python 3.x
- SQLite
- SQLAlchemy
- FPDF
- dotenv

 
Contributors
- Blessing Ingabire  (b.ingabire1@alustudent.com)
- Faith Irakoze  (f.irakoze2@alustudent.com)
- Tifare Kaseke (t.kaseke@alustudent.com)
- Divine Kuzo (d.kuzo@alustudent.com)
- Pascal Nsigo (p.nsigo@alustudent.com)
- Maurice Nshimyumukiza (m.nshimyumu@alustudent.com)
- Bode Murairi (b.murairi@alustudent.com)




