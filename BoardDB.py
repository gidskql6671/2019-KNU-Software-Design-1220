import sqlite3

class BoardDB(object):
    conn = None
    cur = None
    db_path = 'db/board.db'


    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
    
    


    def __del__(self):
        self.conn.close()