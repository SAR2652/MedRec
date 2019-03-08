import pandas as pd
import sqlite3
read=pd.read_csv("pincodes1.csv")
read.dropna(axis = 0, subset = ['City'], inplace = True)
print(read['City'].isna().sum())
#print(read.head())
#print(read['Pincode'].isna().sum())
pincodes=read['Pincode'].values.tolist()
city=read['City'].values.tolist()
print(len(city))
print(type(city[-1]))
state=read['State'].values.tolist()
mapping=list(zip(city, state))
new_mapping = []
for city, state in mapping:
    try:
        region = city + ', ' + state
    except Exception as e:
        import sys
        print(e,type(city),state)
        sys.exit(0)
    new_mapping.append(region)
#print(new_mapping)
comma_mapping = []
for x in new_mapping:
    if x not in comma_mapping:
        comma_mapping.append(x)

p=[]
for pin in pincodes:
    x=int(pin)
    x=x//1000
    if x not in p:
        p.append(x)

city, state = zip(*mapping)

final = list(zip(p, comma_mapping))

conn = sqlite3.connect('D:\Practice\MedRec\other\medi_colab.db')
c = conn.cursor()

c.execute("""CREATE TABLE region (pincode INT PRIMARY KEY, region VARCHAR(75))""")
for pin, region in final:
    c.execute("""INSERT INTO region VALUES (?, ?)""", (pin, region))
conn.commit()
print("Region table successfully created")
