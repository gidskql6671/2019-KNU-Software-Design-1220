from UI.UITemplate import *
from UI.StudentMainUI import *
from UserAccount.Student import Student
from StudentCareer.StudentCareer import *
from GraduationRequirements.DeepCseMajorAfter12 import DeepCseMajorAfter12
from GraduationRequirements.MultipleMajorTrack import MultipleMajorTrack
from GraduationRequirements.ConvergenceMajor import ConvergenceMajor
from GraduationRequirements.LinkedMajor import LinkedMajor
from GraduationRequirements.MultipleMajor import MultipleMajor


class StudentCareerUI(UITemplate):
    def __init__(self, window: Tk, font, student_main):
        super().__init__(window, font)

        self.window = window
        self.font = font
        self.student_main: StudentMainUI = student_main
        self._status = 0
        self._student_info: Student = None
        self._gr_class = None
        self._gr_list = []  # 졸업 요건
        self._list_index = 0

        self._lecture: lecture = None
        self._non_lecture: nonlecture = None

        self._career_list = []

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

        frame_list = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)
        frame_info = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)

        self._label_list_name = Label(frame_list, text="", font=self.font, bg="gray81")
        self._label_list_name.pack(side="top")

        scrollbar = Scrollbar(frame_list)
        scrollbar.pack(side="left", fill="y")

        self._listbox = Listbox(frame_list, yscrollcommand=scrollbar.set, font=("맑은 고딕", 12), width=30)
        self._listbox.pack(side="left")

        def cur_select(evt):
            if self._listbox.curselection():
                self._list_index = self._listbox.curselection()[0]
                self._entry_name.configure(state="normal")
                self._entry_stand.configure(state="normal")

                self._entry_name.delete(0, END)
                self._entry_stand.delete(0, END)
                self._entry_value.delete(0, END)

                self._entry_name.insert(0, self._gr_list[self._list_index][4])
                self._entry_stand.insert(0, self._gr_list[self._list_index][5])
                self._entry_value.insert(0, self._career_list[self._list_index])

                self._entry_name.configure(state="readonly")
                self._entry_stand.configure(state="readonly")

        self._listbox.bind("<<ListboxSelect>>", cur_select)

        scrollbar["command"] = self._listbox.yview()

        frame_list.pack(side="left")
        frame_info.pack(side="right", padx=40)

        Label(frame_info, text="항목", font=self.font, bg='gray81').grid(row=0, column=0, padx=10)
        Label(frame_info, text="기준", font=self.font, bg='gray81').grid(row=1, column=0, padx=10, pady=10)
        Label(frame_info, text="달성 정도", font=self.font, bg='gray81').grid(row=2, column=0, padx=10)
        self._entry_name = Entry(frame_info, font=("맑은 고딕", 18), width=12, state="readonly")
        self._entry_stand = Entry(frame_info, font=("맑은 고딕", 18), width=12, state="readonly")
        self._entry_value = Entry(frame_info, font=("맑은 고딕", 18), width=12)

        self._entry_name.grid(row=0, column=1, padx=10)
        self._entry_stand.grid(row=1, column=1, padx=10, pady=10)
        self._entry_value.grid(row=2, column=1, padx=10)

        Button(frame_info, text="수정", font=self.font, bg='gray86', command=self._handler_info_ok).grid(row=3, column=0, pady=30)

    def start(self, info):
        self._student_info = info
        self._lecture = lecture(info.get_id())
        self._non_lecture = nonlecture(info.get_id())

        self._entry_name.delete(0, END)
        self._entry_stand.delete(0, END)
        self._entry_value.delete(0, END)
        self._listbox.select_clear(0, END)

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

        self._update_list()

        self._status = 0
        self._draw_main()

    def btn_back_handler(self):
        del self._lecture
        del self._non_lecture
        del self._gr_class
        self._erase_main()
        self.student_main.start(self._student_info)

    def _handler_info_ok(self):
        if not self._entry_value.get() or not self._entry_value.get().isdecimal():
            messagebox.showerror(title="경력 입력 에러", message="경력 값으로 정수를 입력하세요.")
            return

        print(self._gr_list[self._list_index][4], self._entry_value.get())

        self._lecture.update_value(self._gr_list[self._list_index][4], self._entry_value.get())

        self._update_list()

    def get_career(self):
        self._career_list.clear()
        for i in range(0, len(self._gr_list)):
            value_lecture = self._lecture.search_lec_value(self._gr_list[i][4])
            value_non_lecture = self._non_lecture.search_nonlec_value(self._gr_list[i][4])
            if value_lecture:
                self._career_list.append(value_lecture)
            else:
                self._career_list.append(value_non_lecture)

    def get_gr_list(self):
        self._gr_list = self._gr_class.get_GradCondition("1")

    def _update_list(self):
        self.get_gr_list()
        self.get_career()

        self._listbox.delete(0, END)
        for index in range(0, len(self._gr_list)):
            if int(self._career_list[index]) < int(self._gr_list[index][5]):
                self._listbox.insert(index, self._gr_list[index][4] + " : " + str(self._career_list[index])
                                     + "/" + str(self._gr_list[index][5]) + "  (미달성)")
            else:
                self._listbox.insert(index, self._gr_list[index][4] + " : " + str(self._career_list[index])
                                     + "/" + str(self._gr_list[index][5]) + "  (달성)")
