import StudentCareer


class Subject(StudentCareer):
    def __init__(self):
        #list_lecture로 값 받아옴
        self._data = None

    def add_lecture(self, code, type, name, point, is_necessary, is_abeek):
        self._lecture_DB.new_lecture((code, type, name, point, is_necessary, is_abeek))

    def search(self, code):
        self._data = self._lecture_DB.search_lecture(code)
        return self._data

    # update value
    # for i in range(0, len(career))
       # if(carreer[i][2] == name)
    # 이름 같으면

    # return category value