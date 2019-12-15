import sqlite3

class StudentCareerDB(object):
    conn = None
    cur = None
    db_path = 'db/student_career.db'


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        
    