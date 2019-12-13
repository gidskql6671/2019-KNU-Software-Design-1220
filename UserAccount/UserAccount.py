from StudentDB import StudentDB

class UserAccount:

    def __init__(self, user_id, user_pw):
        self._user_id = user_id
        self._user_pw = user_pw

    def register_acc(self):
        pass

    def del_acc(self, user_id, user_pw):
        user_DB = StudentDB()
        user_DB.delete((self._user_id, self._user_pw))