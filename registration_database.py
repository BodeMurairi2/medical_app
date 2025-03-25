import sqlite3
from datetime import datetime

def connect_db():
    conn = sqlite3.connect('hospital.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            middle_name TEXT,
            address TEXT NOT NULL,
            national_id TEXT NOT NULL,
            email TEXT NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL,
            dob DATE NOT NULL,
            registration_date DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_patient(patient):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (first_name, last_name, middle_name, address,
                              national_id, email, gender, phone, dob, registration_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (patient.first_name, patient.last_name, patient.middle_name, patient.address,
          patient.national_id, patient.email, patient.gender, patient.phone,
          patient.dob, patient.registration_date))
    conn.commit()
    conn.close()