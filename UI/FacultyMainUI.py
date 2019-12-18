from UI.UITemplate import *
from UI.FacultyGRUI import FacultyGRUI
from UI.FacultyQnAUI import FacultyQnAUI
from UI.LoginUI import *
from UserAccount.Faculty import Faculty


class FacultyMainUI(UITemplate):
    def __init__(self, window: Tk, font, login_ui):
        super().__init__(window, font)

        self._login_ui: LoginUI = login_ui
        self._gr_ui = FacultyGRUI(window, font, self)
        self._qna_ui = FacultyQnAUI(window, font, self)
        self._faculty_info: Faculty = None

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

        Button(self.frame_main, text="졸업요건 조회 및 수정", command=self._start_stand, font=self.font).place(relx=0.25, rely=0.66, anchor="center")
        Button(self.frame_main, text="Q&A 게시판", command=self._start_qna, font=self.font).place(relx=0.8, rely=0.66, anchor="center")

        self.btn_back.configure(text='로그아웃')

    def start(self, info):
        self._faculty_info = info
        self._draw_main()

    def btn_back_handler(self):
        self._erase_main()
        del self._faculty_info
        self._login_ui.start()

    def _start_stand(self):
        self._erase_main()
        self._gr_ui.start(self)

    def _start_qna(self):
        self._erase_main()
        self._qna_ui.start(self)
        pass
