from UI.UITemplate import *
from UI.LoginUI import *


class StudentGRUI(UITemplate):
    def __init__(self, window: Tk, font, mainmenu_ui):
        super().__init__(window, font)

        self.mainmenu_ui = mainmenu_ui
        self._gr_class = None  # 졸업요건 클래스가 들어갈거다.
        self._gr_list = []

        self.get_gr_list()

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

        self.frame_info = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)
        self.frame_list = Frame(self.frame_main, borderwidth=2, relief="groove", bg="gray81", padx=10, pady=10)

        self.text = Text(self.frame_info, width=40, height=20)
        self.text.insert(CURRENT, "원하는 항목을 선택하세요.")
        self.text.pack()
        self.text.configure(state='disabled')

        self._scrollbar = Scrollbar(self.frame_list)
        self._scrollbar.pack(side="left", fill="y")

        self._listbox = Listbox(self.frame_list, yscrollcommand=self._scrollbar.set, font=("맑은 고딕", 12), width=30)
        self._listbox.pack(side="left")

        def cur_select(evt):
            if self._listbox.curselection():
                list_index = self._listbox.curselection()[0]
                self.text.configure(state='normal')
                self.text.delete('1.0', END)
                self.text.insert('1.0', self._gr_list[list_index][0] + "  ")
                self.text.insert(CURRENT, self._gr_list[list_index][1] + "\n")
                self.text.insert(CURRENT, self._gr_list[list_index][2])
                self.text.configure(state='disabled')
            else:
                self.text.configure(state='normal')
                self.text.delete('1.0', END)
                self.text.insert('1.0', "원하는 항목을 선택하세요.")
                self.text.configure(state='disabled')

        self._listbox.bind("<<ListboxSelect>>", cur_select)
        for index in range(0, len(self._gr_list)):
            self._listbox.insert(index, self._gr_list[index][0] + " " + self._gr_list[index][1])

        self._scrollbar["command"] = self._listbox.yview()

        self.frame_list.pack(side="left")
        self.frame_info.pack(side="right", padx=40)

    def start(self):
        self.get_gr_list()
        self._listbox.select_clear(0, END)
        self.text.configure(state='normal')
        self.text.delete('1.0', END)
        self.text.insert('1.0', "원하는 항목을 선택하세요.")
        self.text.configure(state='disabled')
        self._draw_main()

    def btn_back_handler(self):
        self._erase_main()
        self.mainmenu_ui.start()

    # 졸업요건 클래스를 통해 졸업요건 리스트를 받아옴.
    def get_gr_list(self):
        self._gr_list.clear()
        # 테스트 용
        for i in range(0, 10):
            self._gr_list.append([])
            self._gr_list[i].append(str(i) + "번째")
            self._gr_list[i].append("간략한 설명")
            self._gr_list[i].append("세부 설명?")
