import pandas as pd
import sqlite3
read=pd.read_csv("pincodes2.csv")
dname=read['DistrictsName'].values.tolist()
city=read['City'].values.tolist()
l=len(city)
x=0
for c in city:
    if c=='NaN':
        if(x!=(l-1)):
            city[x]=dname[x]
            x=x+1
            print(dname, city)
