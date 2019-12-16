from UI.UITemplate import *
from UI.StudentMainUI import *
from UserAccount.Student import Student
from StudentCareer.StudentCareer import *


class StudentCareerUI(UITemplate):
    def __init__(self, window: Tk, font, student_main):
        super().__init__(window, font)

        self.window = window
        self.font = font
        self.student_main: StudentMainUI = student_main
        self._status = 0
        self._student_info: Student = None
        self._gr_list = [] # 졸업 요건
        self._list_index = 0

        self._subject: Subject = None
        self._etc: etc = None

        self._subject_career_list = []
        self._etc_career_list = []

        self.get_gr_list()

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

        frame_list = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)
        frame_info = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)

        scrollbar = Scrollbar(frame_list)
        scrollbar.pack(side="left", fill="y")

        self._listbox = Listbox(frame_list, yscrollcommand=scrollbar.set, font=("맑은 고딕", 12), width=30)
        self._listbox.pack(side="left")

        def cur_select(evt):
            if self._listbox.curselection():
                self._list_index = self._listbox.curselection()[0]
            else:
                value = "원하는 항목을 선택하세요."

        self._listbox.bind("<<ListboxSelect>>", cur_select)

        self._update_list()

        scrollbar["command"] = self._listbox.yview()

        frame_list.pack(side="left")
        frame_info.pack(side="right")

    def start(self, info):
        self._student_info = info
        print(info.get_id())
        self._subject = Subject(info.get_id())
        self._etc = etc(info.get_id())
        self._status = 0
        self._draw_main()

    def btn_back_handler(self):
        del self._subject
        del self._etc
        self._erase_main()
        self.student_main.start(self._student_info)

    def get_gr_list(self):
        # 테스트 용
        self._gr_list.append([])
        self._gr_list[0].append("DeepCseMajor")
        self._gr_list[0].append("DeepCseMajorAfter12")
        self._gr_list[0].append("lecture")
        self._gr_list[0].append("total_credits")
        self._gr_list[0].append("이수 학점")
        self._gr_list[0].append(150)
        self._gr_list[0].append("들어야하는 최소 이수 학점")

        self._gr_list.append([])
        self._gr_list[1].append("DeepCseMajor")
        self._gr_list[1].append("DeepCseMajorAfter12")
        self._gr_list[1].append("lecture")
        self._gr_list[1].append("total_credits")
        self._gr_list[1].append("전공 학점")
        self._gr_list[1].append(42)
        self._gr_list[1].append("들어야하는 최소 전공 학점")

    def _update_list(self):
        self._listbox.delete(0, END)
        for index in range(0, len(self._gr_list)):
            self._listbox.insert(index, self._gr_list[index][4] + "  " + str(self._gr_list[index][5]))
