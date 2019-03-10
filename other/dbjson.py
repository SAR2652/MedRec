import json
import sqlite3
conn = sqlite3.connect('D:\Practice\MedRec\other\medi_colab.db')
c = conn.cursor()
def tojson():
    temp=c.execute("""SELECT * FROM REGION""").fetchall()
    json_output=json.dumps(temp)
    print(json_output)
