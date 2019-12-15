import sqlite3

class LectureDB(object):
    conn = None
    cur = None
    db_path = 'db/lecture.db'


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        

    # 교과목 추가하기
    # args : (code, type, name, point, is_necessary, is_abeek)
    #        (과목코드:TEXT, 교과구분:INT, 교과목명:TEXT, 학점:INT, 필수?:TEXT, ABEEK?:TEXT)
    # 과목코드는 모든 과목마다 다르다고 가정 (중복 허용 안 됨)
    # TODO: 교과구분 정의
    def new_lecture(self, args: tuple):
        self.cur.execute('INSERT INTO lecture VALUES(?, ?, ?, ?, ?, ?)', args)
        self.conn.commit()

    # 과목코드로 교과목 가져오기
    # 인자로 과목코드를 주면 해당 과목의 정보 6개 튜플로 리턴
    def search_lecture(self, code: str):
        self.cur.execute('SELECT * FROM lecture WHERE code=?', (code))
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 교과목 수정하기
    # new_lecture와 같이 6개 tuple을 주면, code에 해당하는 과목코드의 과목의 정보를 모두 주어진 정보로 수정
    def edit_lecture(self, args: tuple):
        (code, type, name, point, is_necessary, is_abeek) = args
        self.cur.execute(f'UPDATE lecture SET code={code}, type={type}, name={name}, point={point}, is_necessary={is_necessary}, is_abeek={is_abeek} WHERE code=?', (code))
        self.conn.commit()
    
    # 교과목 삭제하기
    # 인자로 과목코드를 주면 해당 과목 삭제
    def delete(self, code: str):
        self.cur.execute('DELETE * FROM lecture WHERE code=?', (code))
        self.conn.commit()
