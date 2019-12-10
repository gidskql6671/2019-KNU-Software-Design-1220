from tkinter import *
from UI import LoginUI


class StudentMainUI:
    def __init__(self, window: Tk, font, login_ui: LoginUI):
        self.window = window
        self.font = font
        self._login_ui = login_ui

        self._setting_ui()

    def _setting_ui(self):
        self.frame_main = Frame(self.window, borderwidth=2, relief="groove", bg="gray86", padx=10, pady=10)

        Button(self.frame_main, text="졸업요건 조회", command=self._start_stand, font=self.font).place(relx=0.25, rely=0.66, anchor="center")
        Button(self.frame_main, text="경력 조회 및 수정", command=self._start_career, font=self.font).place(relx=0.55, rely=0.66, anchor="center")
        Button(self.frame_main, text="게시판", command=self._start_qna, font=self.font).place(relx=0.8, rely=0.66, anchor="center")

    def _draw_main(self):
        self._login_ui.draw_title()
        self.frame_main.pack(padx=30, pady=40, ipadx=20, ipady=20, anchor=CENTER, expand=True, fill="both")

    def _start_stand(self):
        pass

    def _start_career(self):
        pass

    def _start_qna(self):
        self._erase_screen()
        self._login_ui.start()

    def _erase_screen(self):
        self._login_ui.erase_title()
        self.frame_main.pack_forget()

    def start(self):
        print("Student Main UI Start")
        self._draw_main()
