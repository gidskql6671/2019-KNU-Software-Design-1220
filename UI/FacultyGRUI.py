from UI.UITemplate import *
from UI.LoginUI import *


class FacultyGRUI(UITemplate):
    def __init__(self, window: Tk, font, mainmenu_ui):
        super().__init__(window, font)

        self._status = 0
        self._mainmenu_ui = mainmenu_ui
        self._gr = None  # 졸업요건 클래스가 들어갈거다.

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
                value = "원하는 항목을 선택하세요."
                self.text.configure(state='normal')
                self.text.delete('1.0', END)
                self.text.insert('1.0', value)
                self.text.configure(state='disabled')

        self._listbox.bind("<<ListboxSelect>>", cur_select)

        for index in range(0, 30):
            self._listbox.insert(index, self._gr_list[index][0] + " " + self._gr_list[index][1])

        self._scrollbar["command"] = self._listbox.yview()

        self.frame_list.pack(side="left")
        self.frame_info.pack(side="right", padx=40)

        self.frame_btn = Frame(self.frame_main, bg="gray86")
        Button(self.frame_btn, text="졸업요건 추가", font=("맑은 고딕", 15), bg="gray86", command=self.handler_add).pack(side="left")
        Button(self.frame_btn, text="수정", font=("맑은 고딕", 15), bg="gray86", command=self.handler_edit).pack(side="left", padx=50)
        Button(self.frame_btn, text="삭제", font=("맑은 고딕", 15), bg="gray86", command=self.handler_delete).pack(side="left")

        self.frame_btn.place(relx=0.5, rely=0.9, anchor="center")

        self.frame_add_main = Frame(self.window, borderwidth=2, relief="groove", bg="gray86", padx=10, pady=10)
        Label(self.frame_add_main, text="학생 경력 관리 시스템", font=("맑은 고딕", 30), bg="gray86").pack(side="top")

        frame_add_main_sub1 = Frame(self.frame_add_main, padx=20, pady=20, borderwidth=2, relief="groove", bg="gray81")
        Label(frame_add_main_sub1, text="졸업요건 항목 이름", font=self.font, bg="gray81").grid(column=0, row=0)
        self._entry_add_name = Entry(frame_add_main_sub1, width=15, font=self.font)
        self._entry_add_name.grid(column=0, row=1)
        Label(frame_add_main_sub1, text="달성 기준", font=self.font, bg="gray81").grid(column=1, row=0)
        self._entry_add_des = Entry(frame_add_main_sub1, width=15, font=self.font)
        self._entry_add_des.grid(column=1, row=1)
        Label(frame_add_main_sub1, text="상세 설명", font=self.font, bg="gray81").grid(column=0, row=2)
        self._text_add_des = Text(frame_add_main_sub1, width=50, height=8, font=("맑은 고딕", 12))
        self._text_add_des.insert("1.0", "상세한 설명을 적어주세요.(선택 사항)")
        self._text_add_des.grid(column=0, row=3, columnspan=2)
        Button(frame_add_main_sub1, text="확인", font=("맑은 고딕", 12), command=self.handler_add_ok).grid(column=0, row=4, pady = 5)
        Button(frame_add_main_sub1, text="취소", font=("맑은 고딕", 12), command=self.btn_back_handler).grid(column=1, row=4, pady = 5)

        frame_add_main_sub1.pack(pady=30)

        self.frame_edit_main = Frame(self.window, borderwidth=2, relief="groove", bg="gray86", padx=10, pady=10)
        Label(self.frame_edit_main, text="학생 경력 관리 시스템", font=("맑은 고딕", 30), bg="gray86").pack(side="top")
        Button(self.frame_edit_main, text="취소", font=("맑은 고딕", 12), command=self.btn_back_handler).pack(side="left", anchor="s")

    def btn_back_handler(self):
        if self._status == 0:
            self._erase_main()
            self._mainmenu_ui.start()
        elif self._status == 1:
            self._erase_add_main()
            self.start()
        else:
            self._erase_edit_main()
            self.start()

    def get_gr_list(self):
        # 테스트 용
        for i in range(0, 30):
            self._gr_list.append([])
            self._gr_list[i].append(str(i) + "번째")
            self._gr_list[i].append("달성기준")
            self._gr_list[i].append("자세한 설명?")

    def _draw_add_main(self):
        self.frame_add_main.pack(padx=30, pady=40, ipadx=20, ipady=20, anchor=CENTER, expand=True, fill="both")

    def _erase_add_main(self):
        self.frame_add_main.pack_forget()

    def _draw_edit_main(self):
        self.frame_edit_main.pack(padx=30, pady=40, ipadx=20, ipady=20, anchor=CENTER, expand=True, fill="both")

    def _erase_edit_main(self):
        self.frame_edit_main.pack_forget()

    def handler_add_ok(self):
        if not self._entry_add_name.get() or not self._entry_add_des.get():
            messagebox.showerror(title="졸업요건 추가 에러", message="항목이름과 달성기준을 채워주세요")
            return
        print(self._entry_add_name.get(), self._entry_add_des.get(), self._text_add_des.get("1.0", END))
        self._erase_add_main()
        self.start()

    def handler_add(self):
        self._erase_main()
        self._status = 1
        self._draw_add_main()

    def handler_edit(self):
        self._erase_main()
        self._status = 2
        self._draw_edit_main()

    def handler_delete(self):
        if self._listbox.curselection():
            del self._gr_list[self._listbox.curselection()[0]]
            self._listbox.delete(self._listbox.curselection()[0])

            value = "원하는 항목을 선택하세요."
            self.text.configure(state='normal')
            self.text.delete('1.0', END)
            self.text.insert('1.0', value)
            self.text.configure(state='disabled')

            # GR 클래스에 삭제 요청을 보낸다

    def start(self):
        self._status = 0
        self._draw_main()
