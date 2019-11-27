class UserAccount:
    user_id = ""
    user_pw = ""

    def __init__(self, user_id, user_pw):
        self.user_id = user_id
        self.user_pw = user_pw

    def get_id(self):
        return self.user_id

    def get_pw(self):
        return self.user_pw

    def del_acc(self):
        pass


class Student(UserAccount):
    std_id = 0
    std_name = ""
    std_major = ""
    take_ABEEK_course = True

    def __init__(self, user_id, user_pw, std_id, std_name, std_major, take_ABEEK_course):
        self.user_id = user_id
        self.user_pw = user_pw
        self.std_id = std_id
        self.std_name = std_name
        self.std_major = std_major
        self.take_ABEEK_course = take_ABEEK_course

    def get_std_id(self):
        return self.std_id

    def get_std_name(self):
        return self.std_name

    def get_std_major(self):
        return self.std_major

    def take_abeek(self):
        return self.take_ABEEK_course


class Faculty(UserAccount):
    fclt_id = 0
    fclt_name = ""
    fclt_dpt = ""

    def __init__(self, user_id, user_pw, fclt_id, fclt_name, fclt_dpt):
        self.user_id = user_id
        self.user_pw = user_pw
        self.fclt_id = fclt_id
        self.fclt_name = fclt_name
        self.fclt_dpt = fclt_dpt

    def get_fclt_id(self):
        return self.fclt_id

    def get_fclt_name(self):
        return self.fclt_name

    def get_fclt_dpt(self):
        return self.fclt_dpt
