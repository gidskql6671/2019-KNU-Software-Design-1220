from GraduationRequirements import GlobalSWMajor

class MultipleMajorTrack(GlobalSWMajor):

    def __init__(self, total_credits, if_docsubmit):
        self.total_credits = total_credits
        self.if_docsubmit = if_docsubmit
        self.majorname = 'GlobalSWMajor'
        self.english_score = ''
        self.if_multipleMajors = ''
        self.consultCount = ''
        self.swCredit = ''
        self.liberalCredit = ''
        self.overseaCredit = ''
        self.internCredit = ''
        self.startupCredit = ''
        self.if_startUp = ''
        self.GradConditionTable[0] = ''


    # 디비에 학과 이름 넘겨주고 해당 속성값에 대한 졸업 요건을 받아온다
    # 학점 - 몇|영어성적 -몇 | 에이빅 학점 - 몇 이런식으로 이차원 행렬 만듦
    def set_GradCondition(self):
        self.GradConditionTable[0][0] = '영어성적'
        #self.english_score = DB에서 받아옴(majorname 이용)
        #self.GradConditionTable[0][1] = self.english_score

        self.GradConditionTable[1][0] = '다중전공'
        #self.if_multipleMajors = DB에서 받아옴(majorname 이용)
        #self.GradConditionTable[1][1] = self.if_multipleMajors

        self.GradConditionTable[2][0] = '진로상담수'
        #self.consultCount = DB에서 받아옴
        #self.GradConditionTable[2][1] = self.consultCount

        self.GradConditionTable[3][0] = '전공학점'
        #self.swCredit = DB에서 받아옴
        #self.GradConditionTable[3][1] = self.swCredit

        self.GradConditionTable[4][0] = '교양학점'
        #self.liberalCredit = DB에서 받아옴
        #self.GradConditionTable[4][1] = self.liberalCredit

        self.GradConditionTable[5][0] = '해외대학학점'
        #self.overseaCredit = DB에서 받아옴
        #self.GradConditionTable[5][1] = self.overseaCredit

        self.GradConditionTable[6][0] = '현장실습'
        #self.internCredit = DB에서 받아옴
        #self.GradConditionTable[6][1] = self.internCredit

        self.GradConditionTable[7][0] = '창업교과목'
        #self.startupCredit = DB에서 받아옴
        #self.GradConditionTable[7][1] = self.startupCredit

        self.GradConditionTable[8][0] = '창업여부'
        #self.if_startUp= DB에서 받아옴
        #self.GradConditionTable[8][1] = self.if_startUp

    # 이 이차원 배열을 리턴함 (getter)
    def get_GradCondition(self):
     return self.GradConditionTable


