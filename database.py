# -*- coding: utf-8 -*-
import sqlite3
import os
def get_students():
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    rows = cur.execute('''SELECT rowid, name, age, information FROM STUDENTS''')
    students = {}
    rows = [list(row) for row in rows]
    for row in rows:
        id = row[0]
        other = {
            'name': row[1],
            'age': row[2],
            'information': row[3]
        }
        students[id] = other
    db.commit()
    cur.close()
    db.close()
    return students
def get_student(id):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    row = cur.execute(f'''SELECT name, age, information, rowid FROM STUDENTS WHERE rowid = {id}''')[0]
    res = {
        'name': row[0],
        'age': row[1],
        'information': row[2]
    }
    db.commit()
    cur.close()
    db.close()
    return res
def clear_table():
    os.remove('db.sqlite')
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    cur.execute('''CREATE TABLE STUDENTS (
name string,
age integer,
information string
)''')
    db.commit()
    cur.close()
    db.close()
def edit_student(id,name=None,age=None,information=None):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    for parameter,value in zip(['name','age','information'],[name,age,information]):
        if value:
            cur.execute(f'UPDATE STUDENTS SET {parameter} WHERE rowid = {id}')
    db.commit()
    cur.close()
    db.close()
def remove_student(id):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    cur.execute(f'DELETE FROM STUDENTS WHERE rowid = {id}')
    db.commit()
    cur.close()
    db.close()
def add_student(name, age, information):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()
    cur.execute(f"INSERT INTO STUDENTS (name, age, information) VALUES ('{name}', {age}, '{information}')")
    db.commit()
    cur.close()
    db.close()