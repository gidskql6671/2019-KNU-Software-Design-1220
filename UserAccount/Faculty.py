from DBConnection.FacultyDB import FacultyDB
from UserAccount.UserAccount import UserAccount


class Faculty(UserAccount):

    def __init__(self):
        super().__init__()

        self._user_DB = FacultyDB()

    def get_info(self):
        return self._user_info

    def login(self, input_id, input_pwd):
        self._user_info = self._user_DB.search((input_id, input_pwd))

        if not self._user_info:
            return False
        else:
            return True

    def register_acc(self, user_id, user_pw, faculty_id, name, department):
        self._user_DB.register((user_id, user_pw, faculty_id, name, department))

    def del_acc(self):
        self._user_DB.delete((self._user_id, self._user_pw))
