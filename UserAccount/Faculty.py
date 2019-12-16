from DBConnection.FacultyDB import FacultyDB
from UserAccount.UserAccount import UserAccount


class Faculty(UserAccount):

    def __init__(self):
        self._user_DB = FacultyDB()
        self._user_info = None

    def get_info(self):
        return self._user_info

    def login(self, input_id, input_pwd):

        self._user_info = self._user_DB.search((input_id, input_pwd))
        if None:
            return False
        else:
            return True

    def register_acc(self, user_id, user_pw, Faculty_id, name, department):
        self._user_DB.register((user_id, user_pw, Faculty_id, name, department))

    def del_acc(self, user_id, user_pw):
        self._user_DB.delete((self._user_id, self._user_pw))