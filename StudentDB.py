import sqlite3

class StudentDB(object):
    conn = None
    cur = None
    db_path = 'db/student.db'


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        

    # args로 (user_id, user_pw, student_id, name, major, is_abeek) 6개 항목 tuple을 줘야 함
    def register(self, args: tuple):
        self.cur.execute('INSERT INTO student VALUES(?, ?, ?, ?, ?, ?)', args)
        self.conn.commit()

    # args로 (user_id, user_pw) tuple을 주면, 그 row의 정보 6개를 tuple로 리턴 (결과가 없으면 None을 리턴)
    def search(self, args: tuple):
        self.cur.execute('SELECT * FROM student WHERE id=? AND password=?', args)
        data = self.cur.fetchone()
        self.conn.commit()
        return data
    
    # args로 (user_id, user_pw) tuple을 주면, 해당 행을 삭제
    def delete(self, args: tuple):
        self.cur.execute('DELETE * FROM student WHERE id=? AND password=?', args)
        self.conn.commit()


    def __del__(self):
        self.conn.close()