import sqlite3

conn = sqlite3.connect('db/student.db')
cur = conn.cursor()

print('받아야 할 것 : id, password, student_id, name, major, is_abeek')
user_id = input('id: ')
user_pw = input('password: ')
student_id = input('student_id: ')
name = input('name: ')
major = input('major: ')
is_abeek = input('is_abeek: ')

# insert new row
cur.execute('INSERT INTO student VALUES(?, ?, ?, ?, ?, ?)', (user_id, user_pw, student_id, name, major, is_abeek))

print('completed')
conn.commit()
conn.close()

