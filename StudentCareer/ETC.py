from StudentCareer.StudentCareer import StdCareer
from datetime import datetime

class etc(StdCareer):
    def __init__(self):
        super().__init__()

    # code, 만료일, 파일만 받으면 내부에서 등록 날짜 받아서 DB 함수로 넘겨줌
    def add_etc(self, code, expire_date, doc_file):
        self._lecture_DB.new_document((code, datetime.now(), expire_date, doc_file))

    def search(self):
        pass

    # 차례로  식별 번호, 타입:교양전공, 추가 일
    # 필드:토익 인턴,,

