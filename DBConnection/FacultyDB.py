import sqlite3
import os

class FacultyDB(object):
    conn = None
    cur = None
    db_path = os.path.abspath('../db/faculty.db')


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        

    # 교직원 계정 생성
    # args로 (user_id, user_pw, faculty_id, name, department) 5개 항목 tuple을 줘야 함
    def register(self, args: tuple):
        self.cur.execute('INSERT INTO faculty VALUES(?, ?, ?, ?, ?)', args)
        self.conn.commit()

    # 교직원 계정 정보 검색 (로그인)
    # args로 (user_id, user_pw) tuple을 주면, 그 row의 정보 5개를 tuple로 리턴 (결과가 없으면 None을 리턴)
    def search(self, args: tuple):
        self.cur.execute('SELECT * FROM faculty WHERE id=? AND password=?', args)
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 교직원 계정 정보 수정
    # args로 (user_id, user_pw, faculty_id, name, department) 5개 항목 tuple을 주면, user_id, user_pw로 검색한 행을 넘겨준 전체 정보로 갱신
    def update(self, args: tuple):
        (user_id, user_pw, faculty_id, name, department) = args
        self.cur.execute(f'UPDATE faculty SET id={user_id}, password={user_pw}, faculty_id={faculty_id}, name={name}, department={department} WHERE id=? AND password=?', args)
        self.conn.commit()
    
    # 교직원 계정 탈퇴 (계정 정보만 삭제)
    # args로 (user_id, user_pw) tuple을 주면, 해당 행을 삭제
    def delete(self, args: tuple):
        self.cur.execute('DELETE * FROM faculty WHERE id=? AND password=?', args)
        self.conn.commit()
