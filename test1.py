import sqlite3
conn = sqlite3.connect (r"D:\Phisit_Python\Work6_1.db")
c = conn.cursor()
c.execute ('''CREATE TABLE students(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(50) NOT NULL,
    lname (50) NOT NULL,
    email varchar(50) NOT NULL,
    sex varchar(10) NOT NULL,
    year varchar(10) NOT NULL,''')
conn.commit()
conn.close()