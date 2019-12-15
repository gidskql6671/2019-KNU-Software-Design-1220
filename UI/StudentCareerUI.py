from UI.UITemplate import *
from UI.StudentMainUI import *


class StudentCareerUI(UITemplate):
    def __init__(self, window: Tk, font, student_main):
        super().__init__(window, font)

        self.window = window
        self.font = font
        self.student_main: StudentMainUI = student_main

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

    def start(self):
        self._draw_main()

    def btn_back_handler(self):
        self._erase_main()
        self.student_main.start()
