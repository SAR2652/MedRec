import pandas as pd
import sqlite3
pd.set_option('display.max_columns', 15)


df = pd.read_excel('hospital.xlsx')

print(df.head())

ids = df['UNIQUE HOSPITAL ID'].values.tolist()
names = df['HOSPITAL NAME'].values.tolist()
address = df['ADDRESS'].values.tolist()

pincodes = []
for pincode in df['PIN'].values.tolist():
    temp = int(str(pincode)[:3])
    pincodes.append(temp)

district = df['DISTRICT'].values.tolist()
#contact_nos = df['PHONE NUMBER'].values.tolist()
country = [356] * len(ids)

city = []
#capitalize only the first letter in the string
for item in df['CITY'].values.tolist():
    temp = item.title()
    city.append(temp)

conn = sqlite3.connect('/home/sarvesh/ML_Github/MedRec/databases/medi_colab.db')
c = conn.cursor()

#c.execute("""DROP TABLE hospital""")

#c.execute("""CREATE TABLE hospital (hospital_id INT PRIMARY KEY, name VARCHAR(20), address TEXT, city VARCHAR(15), pincode INT, country_code INT, FOREIGN KEY(pincode) REFERENCES region(pincode), FOREIGN KEY(country_code) REFERENCES country(country_code))""")

mapping = list(zip(ids, names, address, city, pincodes, country))
for id, name, address, city, pincode, country in mapping:
    c.execute("""INSERT INTO hospital VALUES (?, ?, ?, ?, ?, ?)""", (id, name, address, city, pincode, country))

conn.commit()

c.execute("""SELECT * FROM hospital""")
print(c.fetchall())