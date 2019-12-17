from GraduationRequirements import GlobalSWMajor
from DBConnection.GradRequirementsDB import GradRequirementsDB

class OverseaDualTrack(GlobalSWMajor):
    def __init__(self):
        self.GradRequirmentDB = GradRequirementsDB()
        self.total_credits
        self.if_docsubmit
        self.majorname = 'GlobalSWMajor'
        self.sub_major = 'OveseaDualTrack'
        self.field
        self.field_name
        self.value
        self.description = ''
        self.english_score = ''
        self.if_multipleMajors = ''
        self.consultCount = ''
        self.swCredit = ''
        self.liberalCredit = ''
        self.if_dualComplete = ''
        self.startupCredit =''


    def set_GradCondition(self):
        GradRequirementsDB.edit_requirement(self.major, self.submajor, self.field, self.field_name, self.value,self.description)

    def get_GradCondition(self):
        tuple = GradRequirementsDB.list_requirment(self.major, self.sub_major)
        return tuple

