import sqlite3
from datetime import datetime
conn = sqlite3.connect('C:/MedRec/databases/medi_colab.db')

c = conn.cursor()

#c.execute("""CREATE TABLE auth_token_data (id INTEGER PRIMARY KEY AUTOINCREMENT,
                #token VARCHAR(255) NOT NULL, created_at DATE NOT NULL)""")

now = datetime.now()

timestamp = datetime.timestamp(now)

#c.execute("""INSERT INTO auth_token_data(token, created_at) VALUES (?, ?)""", ('xyzabc', timestamp))
c.execute("""TRUNCATE auth_token_data""")

conn.commit()
conn.close()