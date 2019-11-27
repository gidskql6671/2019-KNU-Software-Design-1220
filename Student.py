from StudentDB import StudentDB
from UserAccount import UserAccount

class Student(UserAccount):

    def __init__(self, user_id, user_pw):
        self._user_id = user_id
        self._user_pw = user_pw
        self._std_id = ""
        self._name = ""
        self._major = ""
        self._is_ABEEK = 0

    def get_info(self, user_id, user_pw, std_id, name, major, is_ABEEK):
        self._user_id = user_id
        self._user_pw = user_pw
        self._std_id = std_id
        self._name = name
        self._major = major
        self._is_ABEEK = is_ABEEK

    def login( self, input_id, input_pwd ):
        user_DB = StudentDB()
        # account exists => return True
        if user_DB.search((input_id, input_pwd)):
            return True
        # account doesn't exist => return True
        # login() == F 일 경우 self.get_info( , , , , , , )로 전체 사용자 정보 받아오고 register로 등록
        # user_DB.register((self._user_id, self._user_pw, self._std_id, self._name, self._major, self._is_ABEEK))
        else:
            return False

    def get_abeek(self):
        return self._is_ABEEK

    def get_major(self):
        return self._major