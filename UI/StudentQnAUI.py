from UI.UITemplate import *
from UI import StudentMainUI


class StudentQnAUI(UITemplate):
    def __init__(self, window: Tk, font, student_main):
        super().__init__(window, font)

        self._student_main = student_main

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

    def start(self):
        pass

    def btn_back_handler(self):
        pass
