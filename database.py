import sqlite3
bd = sqlite3.connect('db.sqlite')
cur = bd.cursor()
cur.execute('''create table STUDENTS (
name text,
age integer,
information text)
''')
cur.close()