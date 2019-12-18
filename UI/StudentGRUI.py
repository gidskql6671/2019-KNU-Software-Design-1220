from UI.UITemplate import *
from UI.StudentMainUI import *
from UserAccount.Student import Student
from GraduationRequirements.DeepCseMajorAfter12 import DeepCseMajorAfter12
from GraduationRequirements.MultipleMajorTrack import MultipleMajorTrack
from GraduationRequirements.ConvergenceMajor import ConvergenceMajor
from GraduationRequirements.LinkedMajor import LinkedMajor
from GraduationRequirements.MultipleMajor import MultipleMajor


class StudentGRUI(UITemplate):
    def __init__(self, window: Tk, font, mainmenu_ui):
        super().__init__(window, font)

        self.mainmenu_ui = mainmenu_ui
        self._gr_class = None  # 졸업요건 클래스가 들어갈거다.
        self._gr_list = []
        self._student_info: Student = None
        self.list_index = -1

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

        frame_info = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)
        self.frame_list = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)

        Label(frame_info, text="항목", font=self.font, bg='gray81').grid(row=0, column=0, padx=10)
        Label(frame_info, text="기준", font=self.font, bg='gray81').grid(row=1, column=0, padx=10, pady=10)
        Label(frame_info, text="상세 설명", font=self.font, bg='gray81').grid(row=2, column=0, padx=10)
        self._entry_name = Entry(frame_info, font=("맑은 고딕", 18), width=12, state="readonly")
        self._text_des = Text(frame_info, font=("맑은 고딕", 16), height=7, width=16, state="disabled")
        self._entry_value = Entry(frame_info, font=("맑은 고딕", 18), width=12, state="readonly")

        self._entry_name.grid(row=0, column=1, padx=10)
        self._text_des.grid(row=2, column=1, padx=10, pady=10, rowspan=4)
        self._entry_value.grid(row=1, column=1, padx=10)

        self._label_list_name = Label(self.frame_list, text="", font=self.font, bg="gray81")
        self._label_list_name.pack(side="top")
        self._scrollbar = Scrollbar(self.frame_list)
        self._scrollbar.pack(side="left", fill="y")

        self._listbox = Listbox(self.frame_list, yscrollcommand=self._scrollbar.set, font=("맑은 고딕", 12), width=30)
        self._listbox.pack(side="left")

        def cur_select(evt):
            if self._listbox.curselection():
                self.list_index = self._listbox.curselection()[0]
                self._entry_name.configure(state='normal')
                self._entry_value.configure(state='normal')
                self._text_des.configure(state='normal')

                self._entry_name.delete(0, END)
                self._entry_value.delete(0, END)
                self._text_des.delete('1.0', END)
                self._entry_name.insert(0, self._gr_list[self.list_index][4])
                self._entry_value.insert(0, self._gr_list[self.list_index][5])
                self._text_des.insert('1.0', self._gr_list[self.list_index][6])

                self._entry_name.configure(state='readonly')
                self._entry_value.configure(state='readonly')
                self._text_des.configure(state='disabled')
            else:
                value = "원하는 항목을 선택하세요."
                self._entry_name.configure(state='normal')
                self._entry_value.configure(state='normal')
                self._text_des.configure(state='normal')
                self._entry_name.delete(0, END)
                self._entry_value.delete(0, END)
                self._text_des.delete('1.0', END)
                self._text_des.insert('1.0', value)
                self._entry_name.configure(state='readonly')
                self._entry_value.configure(state='readonly')
                self._text_des.configure(state='disabled')

        self._listbox.bind("<<ListboxSelect>>", cur_select)

        self._scrollbar["command"] = self._listbox.yview()

        self.frame_list.pack(side="left")
        frame_info.pack(side="right", padx=40, pady=40, anchor="s")

    def start(self, info):
        self._student_info = info

        major = info.get_major()

        if major == "DeepCseMajorAfter12":
            self._label_list_name.configure(text="심화컴퓨터")
            self._gr_class = DeepCseMajorAfter12()
        elif major == "MultipleMajorTrack":
            self._label_list_name.configure(text="글로벌소프트웨어")
            self._gr_class = MultipleMajorTrack()
        elif major == "LinkedMajor":
            self._label_list_name.configure(text="연계 전공")
            self._gr_class = LinkedMajor()
        elif major == "ConvergenceMajor":
            self._label_list_name.configure(text="융합 전공")
            self._gr_class = ConvergenceMajor()
        elif major == "MultipleMajor":
            self._label_list_name.configure(text="복수 전공")
            self._gr_class = MultipleMajor()

        self.update_list()

        del self._gr_class

        self._listbox.select_clear(0, END)

        value = "원하는 항목을 선택하세요."
        self._entry_name.configure(state='normal')
        self._entry_value.configure(state='normal')
        self._text_des.configure(state='normal')

        self._entry_name.delete(0, END)
        self._entry_value.delete(0, END)
        self._text_des.delete('1.0', END)
        self._text_des.insert('1.0', value)

        self._entry_name.configure(state='readonly')
        self._entry_value.configure(state='readonly')
        self._text_des.configure(state='disabled')

        self._draw_main()

    def btn_back_handler(self):
        self._erase_main()
        self.mainmenu_ui.start(self._student_info)

    # 졸업요건 클래스를 통해 졸업요건 리스트를 받아옴.
    def get_gr_list(self):
        self._gr_list = self._gr_class.get_GradCondition("1")

    def update_list(self):
        self.get_gr_list()
        for index in range(0, len(self._gr_list)):
            self._listbox.insert(index, self._gr_list[index][4] + " : " + self._gr_list[index][5])

    def _draw_main(self):
        self.label_title.place(relx=0.5, rely=0.15, anchor=CENTER)
        self.frame_main.pack(padx=30, pady=40, ipadx=20, ipady=20, anchor=CENTER, expand=True, fill="both")
