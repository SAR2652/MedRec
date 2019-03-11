import pandas as pd
import sqlite3
from dbjson import tojson

df = pd.read_csv('all.csv')

print(df.head())

country = df['name'].values.tolist()
code = df['country-code'].values.tolist()

conn = sqlite3.connect('/home/sarvesh/ML_Github/MedRec/databases/medi_colab.db')

c = conn.cursor()
json_op= tojson('country', '/home/sarvesh/ML_Github/MedRec/databases/medi_colab.db')
#c.execute("""CREATE TABLE country (country_code INT PRIMARY KEY, country_name VARCHAR(50))""")

#mapping = list(zip(code, country))

#for code, country in mapping:
    #c.execute("""INSERT into country (country_code, country_name) VALUES (?, ?)""", (code, country))

c.execute("""SELECT * FROM country""")
print(c.fetchall())
print("\n \n", json_op)
