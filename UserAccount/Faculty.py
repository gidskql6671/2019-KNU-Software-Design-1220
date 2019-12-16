from DBConnection import FacultyDB
from UserAccount import UserAccount


class Faculty(UserAccount):

    def __init__(self, user_id, user_pw, faculty_id, name, department):
        self._user_id = user_id
        self._user_pw = user_pw
        self._faculty_id = ""
        self._name = ""
        self._department = ""

    def get_info(self, user_id, user_pw, faculty_id, name, department):
        self._user_id = user_id
        self._user_pw = user_pw
        self._faculty_id = faculty_id
        self._name = name
        self._department = department

    def login( self, user_id, user_pw ):
        user_DB = FacultyDB()
        # account exists => return True
        if user_DB.search((user_id, user_pw)):
            return True
        # account doesn't exist => return True
        # login() == F 일 경우 self.get_info( , , , , , )로 전체 사용자 정보 받아오고 register로 등록
        # user_DB.register((self._user_id, self._user_pw, self._faculty_id, self._name, self._department))
        else:
            return False