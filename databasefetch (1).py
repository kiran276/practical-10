import sqlite3

con = sqlite3.connect('Registration Form.db')

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM STUDENT')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
        
sql_fetch(con)