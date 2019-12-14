from datetime import datetime


class StdCareer:

    def __init__(self):
        _now = datetime.now()


class SbjCareer(StdCareer):
    def __init__(self):
        pass


class subject:
    def __init__(self, category, ID, name, grade):
        self._sub_category = category
        self._sub_ID = ID
        self._sub_name = name
        self._sub_grade = grade


class ABEEK_sub(subject):
    def __init__(self):
        pass


class required_sub(subject):
    def __init__(self):
        pass


class EtcCareer(StdCareer):
    def __init__(self):
        pass


class Document:
    def __init__(self):
        pass
