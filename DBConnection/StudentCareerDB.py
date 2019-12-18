import sqlite3
import os

class StudentCareerDB(object):
    conn = None
    cur = None
    db_path = os.path.abspath('db/student_career.db')


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
    

    ## 교과경력 : lecture_career 테이블
    # student_id / career_code / type_name / value / date

    # 교과경력 추가
    # args : (student_id, career_code, type_name, value, date)
    def new_lecture_career(self, args: tuple):
        self.cur.execute('INSERT INTO lecture_career VALUES(?, ?, ?, ?, ?)', args)
        self.conn.commit()

    # 교과경력 조회
    # 인자로 career_code를 주면 그 행 5개 항목을 튜플로 가져옴
    def search_lecture_career(self, career_code: str):
        self.cur.execute('SELECT * FROM lecture_career WHERE career_code=?', (career_code,))
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 학번으로 교과경력 전체 조회
    # 인자로 student_id를 주면 그 학생의 교과경력을 튜플의 리스트로 모두 가져옴
    def list_lecture_career(self, student_id: str):
        self.cur.execute('SELECT * FROM lecture_career WHERE student_id=?', (student_id,))
        data = self.cur.fetchall()
        self.conn.commit()
        return data

    # 교과경력 수정
    # args : (student_id, career_code, type_name, value, date)
    # career_code로 행을 찾아서 그 행을 주어진 정보로 전체 업데이트함
    def edit_lecture_career(self, args: tuple):
        (student_id, career_code, type_name, value, date) = args
        self.cur.execute(f"UPDATE lecture_career SET student_id='{student_id}', type_name='{type_name}', value='{value}', date='{date}' WHERE career_code=?", (career_code,))
        self.conn.commit()
    
    # 교과경력 삭제
    # 인자로 career_code를 주면 그 행 삭제
    def delete_lecture_career(self, career_code: str):
        self.cur.execute('DELETE FROM lecture_career WHERE career_code=?', (career_code,))
        self.conn.commit()

    #############################################################

    ## 비교과경력 : nonlecture_career 테이블
    # student_id / career_code / expire_date / field / value / date
    # field : 졸업요건의 field (필드 코드)와 대응

    # 비교과경력 추가
    # args : (student_id, career_code, expire_date, field, value, date)
    def new_nonlecture_career(self, args: tuple):
        self.cur.execute('INSERT INTO nonlecture_career VALUES(?, ?, ?, ?, ?, ?)', args)
        self.conn.commit()

    # 비교과경력 조회
    # 인자로 career_code를 주면 그 행 6개 항목을 튜플로 가져옴
    def search_nonlecture_career(self, career_code: str):
        self.cur.execute('SELECT * FROM nonlecture_career WHERE career_code=?', (career_code,))
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 학번으로 비교과경력 전체 조회
    # 인자로 student_id를 주면 그 학생의 교과경력을 튜플의 리스트로 모두 가져옴
    def list_nonlecture_career(self, student_id: str):
        self.cur.execute('SELECT * FROM nonlecture_career WHERE student_id=?', (student_id,))
        data = self.cur.fetchall()
        self.conn.commit()
        return data

    # 학번과 알고 싶은 필드를 주면, 그 정보 가져오기
    # args : (student_id, field)
    def get_nonlecture_career_value(self, args: tuple):
        self.cur.execute('SELECT * FROM nonlecture_career WHERE student_id=? AND field=?', args)
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 비교과경력 수정
    # args : (student_id, career_code, expire_date, field, value, date)
    # career_code로 행을 찾아서 그 행을 주어진 정보로 전체 업데이트함
    def edit_nonlecture_career(self, args: tuple):
        (student_id, career_code, expire_date, field, value, date) = args
        self.cur.execute(f'UPDATE nonlecture_career SET student_id={student_id}, expire_date={expire_date}, field={field}, value={value}, date={date} WHERE career_code=?', (career_code,))
        self.conn.commit()
    
    # 비교과경력 삭제
    # 인자로 career_code를 주면 그 행 삭제
    def delete_nonlecture_career(self, career_code: str):
        self.cur.execute('DELETE FROM nonlecture_career WHERE career_code=?', (career_code,))
        self.conn.commit()

