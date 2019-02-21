from collections import OrderedDict
import pandas as pd
import numpy as np
import sqlite3

pd.set_option('display.max_columns', 5)

df = pd.read_csv('icd_codes_final.csv')
#print(df[['icd_code', 'common_name']].head(20))

#generate unique icd codes and the common names associated with them

#convert to lists
icd_codes = df['icd_code'].values.tolist()
common_names = df['common_name'].values.tolist()

#Remove duplicates while preserving order
icd_codes = list(sorted(OrderedDict.fromkeys(icd_codes)))
common_names = list(OrderedDict.fromkeys(common_names))

mapping = list(zip(icd_codes, common_names))
print("{} {}".format(type(mapping[0][0]), type(mapping[0][1])))
#for icd_code, common_name in mapping:
    #print("{} {}".format(icd_code, common_name))

#create offline sqlite3 database
conn = sqlite3.connect('medi_colab.db')

#create a cursor
c = conn.cursor()

#create icd_codes table
c.execute("""CREATE TABLE icd_codes (icd_code VARCHAR(10) PRIMARY KEY, common_name VARCHAR(50) NOT NULL)""")

#commit changes to the database
conn.commit()

#insert mapped list rows one by one
for icd_code, common_name in mapping:
    c.execute("INSERT INTO icd_codes (icd_code, common_name) VALUES (?, ?)", (icd_code, common_name))

conn.commit()

#extract contents for the icd_sub_codes table
df = df[['icd_sub_code', 'scientific_name', 'icd_code']]

#create icd_sub_codes table
c.execute("""CREATE TABLE icd_sub_codes 
            (icd_sub_code VARCHAR(10) PRIMARY KEY, 
            scientific_name TEXT,
            icd_code VARCHAR(50), 
            FOREIGN KEY(icd_code) REFERENCES icd_codes(icd_code))""")

#append the rows to the table
df.to_sql('icd_sub_codes', con = conn, if_exists = 'append', index = False)

conn.commit()

print("TABLE icd_sub_codes has been successfully populated")
#print(icd_codes[:5])
#print(common_names[:5])

