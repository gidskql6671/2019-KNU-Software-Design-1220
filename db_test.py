import sqlite3

conn = sqlite3.connect('db/student.db')

cur = conn.cursor()
cur.execute("insert into student values('test', 'test', '2018123123', '홍길동', '컴퓨터학부', 'Y')")

conn.commit()

conn.close()
