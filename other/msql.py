import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Prime"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM `Sarvesh`")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)