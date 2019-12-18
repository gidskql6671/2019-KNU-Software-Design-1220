import sqlite3
import os

class GradRequirementsDB(object):
    conn = None
    cur = None
    db_path = os.path.abspath('db/grad_requirements.db')

    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    # grad_requirements table 구성 설명:
    # major : 전공 (DeepCseMajor / GlobalSWMajor / LinkedMajor / 융합전공 / 복수전공 / 부전공)
    # sub_major : 2번째 전공 필드 
    #             (심컴의 경우 여기에 DeepCseMajorBefore12 / DeepCseMajorAfter12 중 하나를 넣으면 됨.)
    #             (글솝의 경우 여기에 MultipleMajorTrack / OverseaDualTrack / BachelorMasterTrack 중 하나를 넣으면 됨.)
    #             (연계, 융합, 복수, 부전공의 경우 각 전공명을 입력)
    # type : 교과경력 / 비교과경력 (lecture / nonlecture)
    # field : 필드 코드 (total_credits, if_docsubmit, ...)
    # field_name : 필드 한글 이름 (이수 학점, 문서 제출 여부)
    # value : 해당하는 필드값
    # description : 필드에 대한 설명글

    # 졸업요건 항목 추가하기
    # 졸업요건 타입 type-->lecture/nonlecture, 텍스트로 구분
    # args : (major, sub_major, type, field, field_name, value, description)
    def new_requirement(self, args: tuple):
        self.cur.execute('INSERT INTO grad_requirements VALUES(?, ?, ?, ?, ?, ?, ?)', args)
        self.conn.commit()

    # 졸업요건 항목 조회하기
    # args : (major, sub_major, type, field)
    # 해당하는 행이 튜플로 반환됨. 마지막 값이 value이니 참조해서 사용
    def search_requirement(self, args: tuple):
        self.cur.execute('SELECT * FROM grad_requirements WHERE major=? AND sub_major=? AND type=? AND field=?', args)
        data = self.cur.fetchone()
        self.conn.commit()
        return data

    # 전공, 전공2, 타입 주면 해당하는 졸업요건 리스트 전체 가져오기
    # args : (major, sub_major, type)
    # 6개 정보를 담은 튜플의 리스트로 반환됨
    def list_requirement(self, args: tuple):
        self.cur.execute('SELECT * FROM grad_requirements WHERE major=? AND sub_major=? AND type=?', args)
        data = self.cur.fetchall()
        self.conn.commit()
        return data

    # 졸업요건 항목 수정하기
    # args : (major, sub_major, type, field, field_name, value, description)
    # 해당하는 (major, sub_major, type, field)의 값을 새 값들로 모두 바꿈
    def edit_requirement(self, args: tuple):
        (major, sub_major, type, field, field_name, value, description) = args
        self.cur.execute(f"UPDATE grad_requirements SET field_name='{field_name}', value='{value}', description='{description}' WHERE major=? AND sub_major=? AND type=? AND field=?", (major, sub_major, type, field))
        self.conn.commit()

    # 졸업요건 항목 삭제하기
    # args : (major, sub_major, type, field)
    def delete_requirement(self, args: tuple):
        self.cur.execute('DELETE FROM grad_requirements WHERE major=? AND sub_major=? AND type=? AND field=?', args)
        self.conn.commit()

    