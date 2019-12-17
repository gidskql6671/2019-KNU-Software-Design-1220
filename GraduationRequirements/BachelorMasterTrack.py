from GraduationRequirements import GlobalSWMajor
from DBConnection.GradRequirementsDB import GradRequirementsDB

class BachelorMasterTrack(GlobalSWMajor):

    def __init__(self, total_credits, if_docsubmit):
        self.GradRequirmentDB = GradRequirementsDB()
        self.total_credits
        self.if_docsubmit
        self.major = 'GlobalSWMajor'
        self.sub_major = 'BachelorMasterTrack'
        self.field
        self.field_name
        self.value
        self.description = ''
        self.english_score = ''
        self.if_multipleMajors = ''
        self.consultCount = ''
        self.swCredit = ''
        self.liberalCredit = ''
        self.overseaCredit = ''
        self.internCredit = ''


    # 디비에 학과 이름 넘겨주고 해당 속성값에 대한 졸업 요건을 받아온다
    # 학점 - 몇|영어성적 -몇 | 에이빅 학점 - 몇 이런식으로 이차원 행렬 만듦
    def set_GradCondition(self):
        GradRequirementsDB.edit_requirement(self.major,self.submajor,self.field,self.field_name,self.value,self.description)

    def get_GradCondition(self):
        tuple = GradRequirementsDB.list_requirment(self.major, self.sub_major)
        return tuple


