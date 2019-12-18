from GraduationRequirements.GradRequirement import GradRequirement


class LinkedMajor(GradRequirement):
    def __init__(self):
        super().__init__()

    # gr_type은 교과인지 비교과인지. 교과면 1, 비교과면 0
    # code는 항목당 고유한 코드, name은 항목의 이름, value는 값, des는 설명
    def edit_GradCondition(self, gr_type, code, name, value, des):
        self.GradRequirementDB.edit_requirement(("LinkedMajor", "LinkedMajor", gr_type, code, name, value, des))

    def create_GradCondition(self, gr_type, code, name, value, des):
        if self.GradRequirementDB.search_requirement(("LinkedMajor", "LinkedMajor", gr_type, code)):
            return -1
        self.GradRequirementDB.new_requirement(("LinkedMajor", "LinkedMajor", gr_type, code, name, value, des))
        return 0

    def delete_GradCondition(self, gr_type, code):
        # args : (major, sub_major, type, field)
        self.GradRequirementDB.delete_requirement(("LinkedMajor", "LinkedMajor", gr_type, code))

    # 이 이차원 배열을 리턴함 (getter)
    def get_GradCondition(self, gr_type):
        self._gr_list = self.GradRequirementDB.list_requirement(("LinkedMajor", "LinkedMajor", gr_type))
        return self._gr_list



