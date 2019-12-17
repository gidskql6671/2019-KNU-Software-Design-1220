import sqlite3
import os


class StudentDB(object):
    conn = None
    cur = None
    db_path = os.path.abspath('db/student.db')


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        

    # 학생 계정 생성
    # args로 (user_id, user_pw, student_id, name, major, is_abeek) 6개 항목 tuple을 줘야 함
    def register(self, args: tuple):
        self.cur.execute('INSERT INTO student VALUES(?, ?, ?, ?, ?, ?)', args)
        self.conn.commit()

    # 학생 계정 정보 검색 (로그인)
    # args로 (user_id, user_pw) tuple을 주면, 그 row의 정보 6개를 tuple로 리턴 (결과가 없으면 None을 리턴)
    def search(self, args: tuple):
        self.cur.execute('SELECT * FROM student WHERE id=? AND password=?', args)
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 학생 계정 정보 수정
    # args로 (user_id, user_pw, student_id, name, major, is_abeek) 6개 항목 tuple을 주면, user_id, user_pw로 검색한 행을 넘겨준 전체 정보로 갱신
    def update(self, args: tuple):
        (user_id, user_pw, student_id, name, major, is_abeek) = args
        self.cur.execute(f'UPDATE student SET id={user_id}, password={user_pw}, student_id={student_id}, name={name}, major={major}, is_abeek={is_abeek} WHERE id=? AND password=?', args)
        self.conn.commit()
    
    # 학생 계정 탈퇴 (계정 정보만 삭제)
    # args로 (user_id, user_pw) tuple을 주면, 해당 행을 삭제
    def delete(self, args: tuple):
        self.cur.execute('DELETE FROM student WHERE id=? AND password=?', args)
        self.conn.commit()
