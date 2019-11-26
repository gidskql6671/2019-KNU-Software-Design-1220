import sqlite3

conn = sqlite3.connect('db/student.db')

cur = conn.cursor()

### insert
# cur.execute("insert into student values('test', 'test', '2018123123', '홍길동', '컴퓨터학부', 'Y')")

### fetch
user_id = 'test'
user_password = 'test'
cur.execute('SELECT * FROM student WHERE id=? AND password=?', (user_id, user_password))
data = cur.fetchone()
print(type(data))
if cur.fetchone() is not None:
    print("Welcome")
else:
    print("Login failed")

conn.commit()

conn.close()
