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



class Faculty(UserAccount):

    def __init__(self, user_id, user_pw, fclt_id, name, department):
        self._user_id = user_id
        self._user_pw = user_pw
        self._fclt_id = fclt_id
        self._name = name
        self._department = department

"""
    def login( self, input_id, input_pwd ):
        user_DB = StudentDB()
        # account exists => return True
        if user_DB.search((input_id, input_pwd)):
            return True
        # account doesn't exist => execute register()
        
        else:
            return user_DB.register((self._user_id, self._user_pw, self._fclt_id, self._name, self._department))
"""
