import sqlite3

conn = sqlite3.connect('db/student.db')
cur = conn.cursor()

print('받아야 할 것 : id, password')
user_id = input('id: ')
user_pw = input('password: ')

# fetch
cur.execute('SELECT * FROM student WHERE id=? AND password=?', (user_id, user_pw))
data = cur.fetchone()
if data:
    print('login succeed')
    for it in data:
        print(it)
else:
    print('login failed')

print('completed')
conn.commit()
conn.close()

