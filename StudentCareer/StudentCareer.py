from DBConnection.StudentCareerDB import StudentCareerDB
from datetime import datetime
import random


class StdCareer:

    def __init__(self):
        self._career_DB = StudentCareerDB()


class lecture(StdCareer):
    # 학번에 맞는 강의 리스트를 받아서 _career에 저장
    def __init__(self, id):
        super().__init__()

        self._id = id
        self._career = self._career_DB.list_lecture_career(id)  # 커리어 리스트를 받아옴

    # update value. _career가 존재하면 value, date 수정, 없으면 새로 만든다.
    # data = (student_id, career_code, type_name, value, date) 학생 번호, 식별 번호, category, value, 등록일
    def update_value(self, name, value):
        for i in range(0, len(self._career)):
            if self._career[i][2] == name:
                _temp = list(self._career[i])
                _temp[3] = value
                _temp[4] = datetime.now()
                self._career[i] = tuple(_temp)
                print(_temp)
                self._career_DB.edit_lecture_career(self._career[i])
                return

        _temp = (self._id, name, name, value, datetime.now())
        self._career_DB.new_lecture_career(_temp)

    # category : ABEEK 기본, ABEEK 전공, ABEEK 공학, 영어 성적, 현장 실습 등...
    def search_lec_value(self, category):
        for i in range(0, len(self._career)):
            if self._career[i][2] == category:
                data = self._career[i][3]
                return data

        # 여기까지오면 데이터가 없는 거다
        return 0

    def del_lec(self, code):
        self._career_DB.delete_lecture_career(code)


class nonlecture(StdCareer):
    def __init__(self, id):
        super().__init__()

        self._id = id
        self._career = self._career_DB.list_nonlecture_career(id)

    # make new document -> submit
    # data = (student_id, career_code, expire_date, field, value, date) 식별번호, 등록일, 만료일, 파일
    # file parameter NULL..
    def update_document(self, code, expire_date, field, value):
        for i in range(0, len(self._career)):
            if self._career[i][1] == code:
                _temp = list(self._career[i])
                _temp[2] = expire_date
                _temp[3] = field
                _temp[4] = value
                _temp[5] = datetime.now()
                self._career[i] = tuple(_temp)
                self._career_DB.edit_nonlecture_career(self._career[i])
                return
        _temp = (self._id, code, expire_date, field, value, datetime.now())
        self._career_DB.new_nonlecture_career(_temp)

    def del_document(self, code):
        self._career_DB.delete_nonlecture_career(code)

    def search_nonlec_value(self, category: str):
        for i in range(0, len(self._career)):
            if self._career[i][3] == category:
                data = self._career[i][4]
                return data

        # 여기까지 오면 데이터가 없는거다
        return 0
    