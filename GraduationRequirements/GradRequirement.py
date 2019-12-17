from DBConnection import GradRequirementsDB
from DBConnection.GradRequirementsDB import GradRequirementsDB

class GradRequirement:

    def __init__(self, major,sub_major):
        self.GradRequirmentDB = GradRequirementsDB()
        self.total_credits
        self.if_docsubmit
        self.major =major
        self.sub_major = sub_major
        self.field
        self.field_name
        self.value
        self.description


    #디비에 해당 학과의 졸업 요건 추가
    def new_requirement(self):
        GradRequirementsDB.new_requirement(self.major,self.sub_major,self.field,self.field_name,self.value,self.description)

    #디비에 해당 학과의 졸업요건 변경
    def edit_requirement(self):
        GradRequirementsDB.edit_requirement(self.major,self.sub_major,self.field,self.field_name,self.value,self.description)

    #디비에 해당 학과의 졸업요건 삭제
    def del_requirment(self):
        GradRequirementsDB.delete_requirement(self.major,self.sub_major,self.field)


