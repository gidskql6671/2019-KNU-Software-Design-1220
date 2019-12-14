from GraduationRequirements import GradRequirement

class LinkedMajor(GradRequirement):

    def __init__(self, total_credits, if_docsubmit):
        self.total_credits = total_credits
        self.if_docsubmit = if_docsubmit
        self.majorname = 'LinkedMajor'
        self.linkedName = ''
        self.linkedCredit = ''
        self.GradConditionTable[0] = ''


    # 디비에 학과 이름 넘겨주고 해당 속성값에 대한 졸업 요건을 받아온다
    # 학점 - 몇|영어성적 -몇 | 에이빅 학점 - 몇 이런식으로 이차원 행렬 만듦
    def set_GradCondition(self):
        self.GradConditionTable[0][0] = '연계전공명'
        # self.linkedName = DB에서 받아옴
        # self.GradConditionTable[0][1] = self.linkedName

        self.GradConditionTable[1][0] = '연계이수학점'
        # self.linkedCredit=DB에서 받아옴
        #self.GradConditionTable[1][1] = self.linkedCredit

    # 이 이차원 배열을 리턴함 (getter)
    def get_GradCondition(self):
     return self.GradConditionTable


