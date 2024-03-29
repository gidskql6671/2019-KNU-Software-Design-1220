from UI.UITemplate import *
from UI.StudentMainUI import *
from UserAccount.Student import Student


class StudentQnAUI(UITemplate):
    def __init__(self, window: Tk, font, student_main):
        super().__init__(window, font)

        self._status = 0
        self._mainmenu_ui: StudentMainUI = student_main
        self._list_index = 0
        self._student_info: Student = None

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

        frame_list = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)

        scrollbar = Scrollbar(frame_list)
        scrollbar.pack(side="left", fill="y")
        self._listbox = Listbox(frame_list, yscrollcommand=scrollbar.set, font=("맑은 고딕", 12), width=50)
        self._listbox.pack(side="left")

        def cur_select(evt):
            if self._listbox.curselection():
                self._list_index = self._listbox.curselection()[0]
        self._listbox.bind("<<ListboxSelect>>", cur_select)

        scrollbar["command"] = self._listbox.yview()

        frame_list.place(relx=0.5, rely=0.5, anchor="center")

    def start(self, info):
        self._student_info = info
        self._status = 0
        self._draw_main()

    def btn_back_handler(self):
        if self._status == 0:
            self._erase_main()
            self._mainmenu_ui.start(self._student_info)
        elif self._status == 1:  # 게시물 띄웠을 떄
            pass
