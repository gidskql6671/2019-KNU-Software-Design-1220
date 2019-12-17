from GraduationRequirements.DeepCseMajor import DeepCseMajor


class DeepCseMajorAfter12(DeepCseMajor):
    def __init__(self):
        super().__init__()

    # 디비에 학과 이름 넘겨주고 해당 속성값에 대한 졸업 요건을 받아온다
    # 학점 - 몇|영어성적 -몇 | 에이빅 학점 - 몇 이런식으로 이차원 행렬 만듦
    def set_GradCondition(self):
        self.GradRequirementDB.edit_requirement(self.major,self.submajor,self.field,self.field_name,self.value,self.description)


    # 이 이차원 배열을 리턴함 (getter)
    def get_GradCondition(self):
        data = self.GradRequirementDB.list_requirment(self.major, self.sub_major)
        return data



