import pandas as pd
import sqlite3
import dbjson

df = pd.read_csv('all.csv')

print(df.head())

#country = df['name'].values.tolist()
#code = df['country-code'].values.tolist()

conn = sqlite3.connect('D:\Practice\MedRec\databases\medi_colab.db')

c = conn.cursor()
json_op=dbjson.tojson(tablename='country',path='D:\Practice\MedRec\databases\medi_colab.db')
#c.execute("""CREATE TABLE country (country_code INT PRIMARY KEY, country_name VARCHAR(50))""")

#mapping = list(zip(code, country))

#for code, country in mapping:
    #c.execute("""INSERT into country (country_code, country_name) VALUES (?, ?)""", (code, country))

c.execute("""SELECT * FROM country""")
print(c.fetchall())
print("/n /n",json_op)
