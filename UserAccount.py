class UserAccount:

    def __init__(self, user_id, user_pw):
        self._user_id = user_id
        self._user_pw = user_pw

    def get_id(self):
        return self._user_id

    def get_pw(self):
        return self._user_pw

    def del_acc(self):
        pass


class Student(UserAccount):

    def __init__(self, user_id, user_pw, std_id, std_name, std_major, take_ABEEK_course):
        self._user_id = user_id
        self._user_pw = user_pw
        self._std_id = std_id
        self._std_name = std_name
        self._std_major = std_major
        self._take_ABEEK_course = take_ABEEK_course

    def get_std_id(self):
        return self._std_id

    def get_std_name(self):
        return self._std_name

    def get_std_major(self):
        return self._std_major

    def take_abeek(self):
        return self._take_ABEEK_course


class Faculty(UserAccount):

    def __init__(self, user_id, user_pw, fclt_id, fclt_name, fclt_dpt):
        self._user_id = user_id
        self._user_pw = user_pw
        self._fclt_id = fclt_id
        self._fclt_name = fclt_name
        self._fclt_dpt = fclt_dpt

    def get_fclt_id(self):
        return self._fclt_id

    def get_fclt_name(self):
        return self._fclt_name

    def get_fclt_dpt(self):
        return self._fclt_dpt


def login( input_id, input_pwd ):
    # DB search ==> exist
    return True

    return sign_up()


def sign_up(newid, newpw, stdid):
    new_id = newid
    new_pw = newpw
    user_std_id = stdid

    # add to DB