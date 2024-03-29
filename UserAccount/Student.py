from DBConnection.StudentDB import StudentDB
from UserAccount.UserAccount import UserAccount


class Student(UserAccount):
    def __init__(self):
        super().__init__()

        self._user_DB = StudentDB()

    def get_major(self):
        return self._user_info[4]

    def get_info(self):
        return self._user_info

    def get_id(self):
        return self._user_info[2]

    def login(self, input_id, input_pwd):
        self._user_info = self._user_DB.search((input_id, input_pwd))

        if not self._user_info:
            return False
        else:
            return True

    def register_acc(self, user_id, user_pw, student_id, name, major, is_abeek):
        print((user_id, user_pw, student_id, name, major, is_abeek))
        self._user_DB.register((user_id, user_pw, student_id, name, major, is_abeek))

    def del_acc(self, user_id, user_pw):
        self._user_DB.delete((user_id, user_pw))
