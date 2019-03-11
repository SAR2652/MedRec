import sqlite3 

conn = sqlite3.connect('/home/sarvesh/ML_Github/MedRec/databases/medi_colab.db')
c = conn.cursor()

#c.execute("""CREATE TABLE medical_practitioner (mp_id INT PRIMARY KEY, last_name VARCHAR(20), first_name VARCHAR(20), middle_name VARCHAR(20), password TEXT, dob DATE, sex BOOLEAN, address TEXT, clinic_address TEXT, degree VARCHAR(10), field TEXT, email VARCHAR(30), hospital_id INT, pincode INT, country_code INT, registered_at TIMESTAMP, FOREIGN KEY(hospital_id) REFERENCES hospital(hospital_id), FOREIGN KEY(pincode) REFERENCES region(pincode), FOREIGN KEY(country_code) REFERENCES country(country_code))""")

#c.execute("""CREATE TABLE patient (patient_id INT PRIMARY KEY, last_name VARCHAR(20), first_name VARCHAR(20), middle_name VARCHAR(20), dob DATE, sex BOOLEAN, blood_type VARCHAR(5), address TEXT, pincode INT, country_code INT, occupation TEXT, contact_no_1 INT, contact_no_2 INT, email VARCHAR(20), allergies TEXT, DHx TEXT, Ca BOOLEAN, IDDM BOOLEAN, NIDDM BOOLEAN, MI BOOLEAN, AF BOOLEAN, registered_at TIMESTAMP, FOREIGN KEY(pincode) REFERENCES region(pincode), FOREIGN KEY(country_code) REFERENCES country(country_code))""")

#c.execute("""CREATE TABLE patient_case (case_id INT PRIMARY KEY, patient_id INT, mp_id INT, icd_sub_code VARCHAR(10), icd_code VARCHAR(10), HPC TEXT, MoI TEXT, D_and_V TEXT, clinical_note TEXT, no_of_visits INT, created_at TIMESTAMP, FOREIGN KEY(patient_id) REFERENCES patient(patient_id), FOREIGN KEY(icd_code) REFERENCES icd_codes(icd_code), FOREIGN KEY(icd_sub_code) REFERENCES icd_sub_codes(icd_sub_code), FOREIGN KEY(mp_id) REFERENCES medical_practitioner(mp_id)) """)

c.execute("""CREATE TABLE patient_record (record_id INT PRIMARY KEY, visit_no INT, on_arrival TEXT, diagnosis TEXT, Tx TEXT, report_suggestions TEXT, medication TEXT, advice TEXT, query TEXT, case_id INT, created_at TIMESTAMP, FOREIGN KEY(case_id) REFERENCES patient_case(case_id))""")

conn.commit()
conn.close()