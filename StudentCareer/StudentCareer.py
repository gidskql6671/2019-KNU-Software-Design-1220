from DBConnection.StudentCareerDB import StudentCareerDB
from DBConnection.DocumentDB import DocumentDB
from datetime import datetime
import random

class StdCareer:

    def __init__(self):
        self._career_DB = StudentCareerDB()
        self._doc_DB = DocumentDB()


class Subject(StdCareer):
    # id에 맞는 강의 리스트를 받아서 _career에 저장
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._career = self._career_DB.list_lecture_career(id)

    # update value. _career가 존재하면 value, date 수정, 없으면 새로 만든다.
    def update_value(self, name, value):
        if self._career:
            for i in range(0, len(self._career)):
                if self._career[i][2] == name:
                    self._temp = list(self._career[i])
                    self._temp[3] = value
                    self._temp[4] = datetime.now()
                    self._career[i] = tuple(self._temp)
                    self._career_DB.edit_lecture_career(self._career[i])
                    return
        else:
            self._temp = (self._id, random.randint(0, 10000), name, value, datetime.now())
            self._career_DB.new_lecture_career(self._temp)

    # category : ABEEK 기본, ABEEK 전공, ABEEK 공학, 영어 성적, 현장 실습 등...
    def search_value(self, category):
        for i in range(0, len(self._career)):
            if self._career[i][2] == category:
                _data = self._career[i][3]
        return _data


class etc(StdCareer):
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._career = self._doc_DB.list_lecture_career(id)

    # update value. _career가 존재하면 value, date 수정, 없으면 새로 만든다.
    def new_document(self, name, value):
        self._temp = (self._id, random.randint(0, 10000), name, value, datetime.now())
        self._career_DB.new_lecture_career(self._temp)

    # category : ABEEK 기본, ABEEK 전공, ABEEK 공학, 영어 성적, 현장 실습 등...
    def search_value(self, category):
        for i in range(0, len(self._career)):
            if self._career[i][2] == category:
                _data = self._career[i][3]

        return _data

