import sqlite3
import os
def get_students():
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    rows = cur.execute('''SELECT name, age, information, ROWID FROM STUDENTS''')
    cur.close()
    students = {}
    for row in rows:
        id = row[-1]
        other = {
            'name': row[0],
            'age': row[1],
            'information': row[2]
        }
        students[id] = other
    return students
def get_student(id):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    row = cur.execute(f'''SELECT name, age, information, ROWID FROM STUDENTS WHERE ROWID = {id}''')[0]
    cur.close()
    return {
        'name': row[0],
        'age': row[1],
        'information': row[2]
    }
def clear_table():
    os.remove('db.sqlite')
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    cur.execute('''CREATE TABLE STUDENTS (
name string,
age integer,
information string
)''')
def edit_student(id,name,age,information):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    for parameter,value in zip(['name','age','information'],[name,age,information]):
        if value:
            cur.execute(f'UPDATE STUDENTS SET {parameter} WHERE ROWID = {id}')
    cur.close()
def remove_student(id):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    cur.execute(f'DELETE FROM STUDENTS WHERE ROWID = {id}')
    cur.close()
def add_student(name, age, information):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    cur.execute(f"INSERT INTO STUDENTS (name, age, information) VALUES ('{name}', {age}, '{information}')"")
    cur.close()