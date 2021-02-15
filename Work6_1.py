import sqlite3 
from os import name,system
conn = sqlite3.connect (r"D:\Phisit_Python\Work6_1.db")
c = conn.cursor()
"""c.execute ('''CREATE TABLE students(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(50) NOT NULL,
    lname varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    sex varchar(10) NOT NULL,
    year varchar(10) NOT NULL)''')
conn.commit()
conn.close()"""

def menu():
    global choice
    print('*******ระบบทะเบียนเรียน*******\n'+'='*25+'\n เพิ่มข้อมูลนักเรียนกด [a]\n แสดงข้อมูลนักเรียน [b]\n แก้ไขข้อมูลนักเรียน [c]\n ลบข้อมูลนักเรียน [d]\n ออกจากโปรแกรม [x]\n')
    choice = input('กรุณาเลือกรายการ : ')

def add(fname,lname,email,sex,year):
    try:
        conn = sqlite3.connect(r'D:\Phisit_Python\Work6_1.db')
        c = conn.cursor()
        sql = '''INSERT INTO students (fname,lname,email,sex,year) VALUES (?,?,?,?,?)'''
        data = (fname,lname,email,sex,year)
        c.execute(sql,data)
        conn.commit()
        c.close()
        print('เพิ่มข้อมูลเรียบร้อย')
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()
def show():
    print('\n\t\t\t*** แสดงข้อมูลนักเรียน ***\n')
    print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<10}{5}\n'.format('No','fname','lname','email','sex','year'))
    with sqlite3.connect(r"D:\Phisit_Python\Work6_1.db") as con:
        con.row_factory = sqlite3.Row
        show1="SELECT * FROM students "
        for row in con.execute(show1):
            print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<10}{5}'.format(row["id"],row["fname"],row["lname"],row["email"],row["sex"],row["year"]))

def edit(fname,lname,email,sex,year,iid):
    conn = sqlite3.connect(r'D:\Phisit_Python\Work6_1.db')
    c = conn.cursor()
    try :
        data = (fname,lname,email,sex,year,'{}'.format(iid))
        c.execute('''UPDATE students SET fname =?, lname =?, email =?, sex =?, year =? WHERE id = ?''',data)
        conn.commit()
        c.close()
        print('แก้ไขข้อมูลเรียบร้อย\n')
        
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()
    
def delete():
    shoose1 = input('ลำดับที่ต้องการลบ : ')
    conn = sqlite3.connect(r"D:\Phisit_Python\Work6_1.db")
    c = conn.cursor()
    c.execute('''DELETE FROM students WHERE id = ?''',shoose1)
    conn.commit()
    conn.close()
    print('แก้ไขข้อมูลเรียบร้อยแล้ว ')

def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
    
while True:
    menu()       
    if choice == 'a':
        fn,ln,em,s,a = input('ชื่อ-สกุล-อีเมล-เพศ-อายุ-ชั้นปี : ').split()
        add(fn,ln,em,s,a)
    elif choice == 'b':
        show()
    elif choice == 'c':
        iid = input('ลำดับที่ต้องการแก้ไข : ')
        fname,lname,email,sex,year = input('fname,lname,email,sex,year').split()
        edit(fname,lname,email,sex,year,iid)
    elif choice == 'd':
        delete()
    elif choice == 'x':
        m = str(input('ออกจากโปรแกรมหรือไม่ yes or no :'))
        if m == 'yes':
            clear()
            break
    else:
        print('กรุณากรอกตัวเลือกให้ถูกต้อง')

