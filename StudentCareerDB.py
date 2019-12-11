import sqlite3

class FacultyDB(object):
    conn = None
    cur = None
    # TODO: HERE (학생경력, 졸업요건 DB설계, 커넥션 작성)
    db_path = 'db/asdf.db'


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        