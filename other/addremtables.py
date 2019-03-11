import sqlite3 

conn = sqlite3.connect('/home/sarvesh/ML_Github/MedRec/databases/medi_colab.db')
c = conn.cursor()

c.execute("""CREATE TABLE patient (patient_id INT PRIMARY KEY, last_name VARCHAR(20), first_name VARCHAR(20), middle_name VARCHAR(20), dob DATE, sex BOOLEAN, address TEXT, occupation TEXT, contact_no_1 INT, contact_no_2 INT, email VARCHAR(20), allergies TEXT, DHx TEXT, Ca BOOLEAN, IDDM BOOLEAN, NIDDM BOOLEAN, MI BOOLEAN, AF BOOLEAN""")

c.execute("""CREATE TABLE patient_case (case_id INT PRIMARY KEY, patient_id INT, mp_id INT, icd_code VARCHAR(10), icd_sub_code VARCHAR(10), clinical_note TEXT, no_of_visits INT, created_at TIMESTAMP, FOREIGN KEY(patient_id) REFERENCES patient(patient_id), FOREIGN KEY(icd_code) REFERENCES icd_codes(icd_code), FOREIGN KEY(mp_id) REFERENCES medica""")