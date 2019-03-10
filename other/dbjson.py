import json
import sqlite3
def tojson(tablename, dbpath):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    temp=c.execute("""SELECT * FROM (?)""", tablename).fetchall()
    json_output=json.dumps(temp)
    return json_output
