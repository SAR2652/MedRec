import pandas as pd
import sqlite3

df = pd.read_csv('all.csv')

print(df.head())

#country = df['name'].values.tolist()
#code = df['country-code'].values.tolist()

conn = sqlite3.connect('/home/sarvesh/ML_Github/MedRec/databases/medi_colab.db')

c = conn.cursor()

#c.execute("""CREATE TABLE country (country_code INT PRIMARY KEY, country_name VARCHAR(50))""")

#mapping = list(zip(code, country))

#for code, country in mapping:
    #c.execute("""INSERT into country (country_code, country_name) VALUES (?, ?)""", (code, country))

c.execute("""SELECT * FROM country""")
print(c.fetchall())