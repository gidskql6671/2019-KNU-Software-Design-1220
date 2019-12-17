import sqlite3
import os

class DocumentDB(object):
    conn = None
    cur = None
    db_path = os.path.abspath('db/document.db')


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        
    
    # document table : code / submit_date / expire_date / doc_file
    # doc_file은 BLOB형으로, 서류 파일 자체를 DB에 업로드할 일이 생길 경우를 대비해 마련해 둠
    # None 줘도 됨

    # 증빙서류 제출
    # args : (code, submit_date, expire_date, doc_file)
    def new_document(self, args: tuple):
        self.cur.execute('INSERT INTO document VALUES(?, ?, ?, ?)', args)
        self.conn.commit()

    # 증빙서류 조회
    # 인자로 code를 주면 그 행 4개 항목을 튜플로 가져옴
    def search_document(self, code: str):
        self.cur.execute('SELECT * FROM document WHERE code=?', (code))
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 증빙서류 수정
    # args : (code, submit_date, expire_date, doc_file)
    # code로 행을 찾아서 그 행을 주어진 정보로 전체 업데이트함
    def edit_document(self, args: tuple):
        (code, submit_date, expire_date, doc_file) = args
        self.cur.execute(f'UPDATE document SET submit_date={submit_date}, expire_date={expire_date}, doc_file={doc_file} WHERE code=?', (code))
        self.conn.commit()
    
    # 증빙서류 삭제
    # 인자로 code를 주면 그 행 삭제
    def delete_document(self, code: str):
        self.cur.execute('DELETE FROM document WHERE code=?', (code))
        self.conn.commit()

