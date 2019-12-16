from DBConnection import StudentDB
from UserAccount import UserAccount

class Student(UserAccount):

    def __init__(self):
        self._user_DB = StudentDB()
        self._user_info = None

    def get_info(self):
        return self._user_info

    def login( self, input_id, input_pwd ):

        self._user_info = self._user_DB.search((input_id, input_pwd))
        if None:
            return False
        else:
            return True

    def register_acc(self, user_id, user_pw, student_id, name, major, is_abeek):
        self._user_DB.register((user_id, user_pw, student_id, name, major, is_abeek))

    def del_acc(self, user_id, user_pw):
        self._user_DB.delete((self._user_id, self._user_pw))

    def get_abeek(self):
        return self._is_ABEEK

    def get_major(self):
        return self._major