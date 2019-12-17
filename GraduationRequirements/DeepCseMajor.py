from GraduationRequirements import GradRequirement
from DBConnection import GradRequirementsDB

class DeepCseMajor(GradRequirement):

    def __init__(self,sub_major):
        self.GradRequirmentDB = GradRequirementsDB
        self.total_credits
        self.if_docsubmit
        self.major ='DeepCseMajor'
        self.sub_major = sub_major
        self.field
        self.field_name
        self.value
        self.description = ''


    # 디비에 학과 이름 넘겨주고 해당 속성값에 대한 졸업 요건을 받아온다
    def edit_requirement(self):
        GradRequirementsDB.edit_requirement(self.major,self.submajor,self.field,self.field_name,self.value,self.description)


    def get_GradCondition(self):
        tuple = GradRequirementsDB.list_requirment(self.major, self.sub_major)
        return tuple


