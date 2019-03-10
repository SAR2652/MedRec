import pandas as pd
import sqlite3
read=pd.read_csv("pincodes2.csv")
dname=read['DistrictsName'].values.tolist()
city=read['City'].values.isna()
