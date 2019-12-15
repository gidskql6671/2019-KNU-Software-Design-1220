import sqlite3
import os

class BoardDB(object):
    conn = None
    cur = None
    db_path = os.path.abspath('../db/board.db')


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    
    # 자신이 올린 질문 리스트 보기
    # 인자로 작성자 이름 입력 (학생 한정)
    # 결과값은 튜플의 리스트로 리턴됨 [(id, author, title, content), (id, author, title, content), ...]
    def question_list(self, author: str):
        self.cur.execute('SELECT * FROM question WHERE author=?', (author))
        data = self.cur.fetchall()
        self.conn.commit()
        return data

    # 질문 작성하기
    # args로 (author, title, content) tuple
    # 생성된 질문의 id가 리턴됨
    def new_question(self, args: tuple):
        self.cur.execute('INSERT INTO question(author, title, content) VALUES(?, ?, ?)', args)
        self.conn.commit()
        return self.cur.lastrowid

    # 질문 수정하기
    # args로 (id, title, content)
    # id는 수정할 질문 id
    def edit_question(self, args: tuple):
        (id, title, content) = args
        self.cur.execute(f'UPDATE question SET title={title}, content={content} WHERE id=?', (id))
        self.conn.commit()

    # 질문 삭제하기
    # 인자로 삭제할 질문 id 입력
    def delete_question(self, id: int):
        self.cur.execute('DELETE * FROM question WHERE id=?', (id))
        self.conn.commit()


    #################################################################################

    # 자신이 올린 답변 리스트 보기
    # 인자로 작성자 이름 입력 (교직원 한정)
    # 결과값은 튜플의 리스트로 리턴됨 [(id, question_id, author, content), (id, question_id, author, content), ...]
    def answer_list(self, author: str):
        self.cur.execute('SELECT * FROM answer WHERE author=?', (author))
        data = self.cur.fetchall()
        self.conn.commit()
        return data

    # 해당하는 질문에 달린 답변 리스트 보기
    # 인자로 question_id 입력
    # 결과값은 answer_list와 마찬가지로 튜플의 리스트로 리턴됨
    def answer_list_by_question(self, question_id: int):
        self.cur.execute('SELECT * FROM answer WHERE question_id=?', (question_id))
        data = self.cur.fetchall()
        self.conn.commit()
        return data

    # 답변 작성하기
    # args로 (question_id, author, content) tuple
    # 해당하는 question_id의 질문에 답변 작성
    # 생성된 답변의 id가 리턴됨
    def new_answer(self, args: tuple):
        self.cur.execute('INSERT INTO answer(question_id, author, content) VALUES(?, ?, ?)', args)
        self.conn.commit()
        return self.cur.lastrowid

    # 답변 수정하기
    # args로 (id, content)
    # id는 수정할 답변 id
    def edit_answer(self, args: tuple):
        (id, content) = args
        self.cur.execute(f'UPDATE answer SET content={content} WHERE id=?', (id))
        self.conn.commit()

    # 질문 삭제하기
    # 인자로 삭제할 질문 id 입력
    def delete_answer(self, id: int):
        self.cur.execute('DELETE * FROM answer WHERE id=?', (id))
        self.conn.commit()
