import sqlite3
import os

class StudentCareerDB(object):
    conn = None
    cur = None
    db_path = os.path.abspath('../db/student_career.db')


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        
    
    ## 교과경력 : lecture_career 테이블
    # student_id / career_code / lecture_code / date

    # 교과경력 추가
    # args : (student_id, career_code, lecture_code, date)
    def new_lecture_career(self, args: tuple):
        self.cur.execute('INSERT INTO lecture_career VALUES(?, ?, ?, ?)', args)
        self.conn.commit()

    # 교과경력 조회
    # 인자로 career_code를 주면 그 행 4개 항목을 튜플로 가져옴
    def search_lecture_career(self, career_code: str):
        self.cur.execute('SELECT * FROM lecture_career WHERE career_code=?', (career_code))
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 교과경력 수정
    # args : (student_id, career_code, lecture_code, date)
    # career_code로 행을 찾아서 그 행을 주어진 정보로 전체 업데이트함
    def edit_lecture_career(self, args: tuple):
        (student_id, career_code, lecture_code, date) = args
        self.cur.execute(f'UPDATE lecture_career SET student_id={student_id}, lecture_code={lecture_code}, date={date} WHERE career_code=?', (career_code))
        self.conn.commit()
    
    # 교과경력 삭제
    # 인자로 career_code를 주면 그 행 삭제
    def delete_lecture_career(self, career_code: str):
        self.cur.execute('DELETE * FROM lecture_career WHERE career_code=?', (career_code))
        self.conn.commit()

    #############################################################

    ## 비교과경력 : nonlecture_career 테이블
    # student_id / career_code / expire_date / doc_code / date

    # 비교과경력 추가
    # args : (student_id, career_code, expire_date, doc_code, date)
    def new_nonlecture_career(self, args: tuple):
        self.cur.execute('INSERT INTO nonlecture_career VALUES(?, ?, ?, ?, ?)', args)
        self.conn.commit()

    # 비교과경력 조회
    # 인자로 career_code를 주면 그 행 5개 항목을 튜플로 가져옴
    def search_nonlecture_career(self, career_code: str):
        self.cur.execute('SELECT * FROM nonlecture_career WHERE career_code=?', (career_code))
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 비교과경력 수정
    # args : (student_id, career_code, expire_date, doc_code, date)
    # career_code로 행을 찾아서 그 행을 주어진 정보로 전체 업데이트함
    def edit_nonlecture_career(self, args: tuple):
        (student_id, career_code, expire_date, doc_code, date) = args
        self.cur.execute(f'UPDATE nonlecture_career SET student_id={student_id}, expire_date={expire_date}, doc_code={doc_code}, date={date} WHERE career_code=?', (career_code))
        self.conn.commit()
    
    # 비교과경력 삭제
    # 인자로 career_code를 주면 그 행 삭제
    def delete_nonlecture_career(self, career_code: str):
        self.cur.execute('DELETE * FROM nonlecture_career WHERE career_code=?', (career_code))
        self.conn.commit()

