from UI.UITemplate import *
from UI import LoginUI
from UI import StudentQnAUI

class StudentMainUI(UITemplate):
    def __init__(self, window: Tk, font, login_ui: LoginUI):
        super().__init__(window, font)

        self._login_ui = login_ui

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

        Button(self.frame_main, text="졸업요건 조회", command=self._start_stand, font=self.font).place(relx=0.25, rely=0.66, anchor="center")
        Button(self.frame_main, text="경력 조회 및 수정", command=self._start_career, font=self.font).place(relx=0.55, rely=0.66, anchor="center")
        Button(self.frame_main, text="게시판", command=self._start_qna, font=self.font).place(relx=0.8, rely=0.66, anchor="center")

        self.btn_back.configure(text='로그아웃')

    def btn_back_handler(self):
        self._erase_main()
        self._login_ui.start()

    def _start_stand(self):
        pass

    def _start_career(self):
        pass

    def _start_qna(self):
        pass

    def start(self):
        print("Student Main UI Start")
        self._draw_main()
