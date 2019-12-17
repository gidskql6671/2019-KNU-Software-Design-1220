from UI.UITemplate import *
from UI.StudentMainUI import StudentMainUI
from UI.FacultyMainUI import FacultyMainUI
from UserAccount.Student import Student
from UserAccount.Faculty import Faculty


class LoginUI(UITemplate):
    def __init__(self, window: Tk, font):
        super().__init__(window, font)

        self._type_user = None
        self._status = 0
        self._student_main_ui = StudentMainUI(window, font, self)
        self._faculty_main_ui = FacultyMainUI(window, font, self)

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

        self.frame_login = Frame(self.window, borderwidth=5, relief="groove", bg="gray81", padx=10, pady=10)
        self.frame_register_student = Frame(self.window, borderwidth=5, relief="groove", bg="gray81", padx=10, pady=10)
        self.frame_register_faculty = Frame(self.window, borderwidth=5, relief="groove", bg="gray81", padx=10, pady=10)
        self.frame_type = Frame(self.window, borderwidth=5, relief="groove", bg="gray81", padx=30, pady=30)

        # 학생, 교직원 선택 UI
        Label(self.frame_type, text="당신의 소속을 선택하세요.", font=self.font, bg="gray81").grid(row=0, column=0, columnspan=4)
        Button(self.frame_type, text="학생", command=self.select_student, font=self.font).grid(row=1, column=0, padx=0.5, pady=10)
        Button(self.frame_type, text="교직원", command=self.select_faculty, font=self.font).grid(row=1, column=2, padx=0.5, pady=10)

        # 로그인 화면의 ID, PWD 입력란과 버튼
        frame_login_sub1 = Frame(self.frame_login, bg="gray81")
        Label(self.frame_login, text="ID", anchor='e', font=self.font, bg="gray81").grid(row=1, column=0)
        Label(self.frame_login, text="Password", font=self.font, bg="gray81").grid(row=2, column=0)
        self._entry_id = Entry(self.frame_login, font=self.font)
        self._entry_pwd = Entry(self.frame_login, show='*', font=self.font)
        self.btn_login = Button(self.frame_login, text="로그인", command=self._click_login, height=2, bg='gray49', font=self.font)

        # 로그인 화면의 회원가입 문구와 버튼
        register_label = Label(frame_login_sub1, text="계정이 없다면 ", bg="gray81")
        register_label.config(font=("맑은 고딕", 12))
        btn_register = Button(frame_login_sub1, text="회원가입", command=self._click_create_account, fg="blue", bg="gray81", relief=FLAT)
        btn_register.config(font=("맑은 고딕", 12))

        # 로그인 화면을 실제 배치하는 구문
        self._entry_id.grid(row=1, column=1)
        self._entry_pwd.grid(row=2, column=1)
        self.btn_login.grid(row=1, column=2, padx=10, rowspan=2)
        frame_login_sub1.grid(row=3, column=1)
        register_label.grid(row=1, column=0)
        btn_register.grid(row=1, column=1)

        # 학생 회원가입란의 id, password, student_id, name, major, is_abeek 입력란과 버튼
        self.radioVar_student = IntVar()
        self.radioVar_student.set(1)

        Label(self.frame_register_student, text="ID", anchor='e', font=self.font, bg="gray81").grid(row=1, column=0)
        Label(self.frame_register_student, text="Password", font=self.font, bg="gray81").grid(row=2, column=0)
        Label(self.frame_register_student, text="학번", font=self.font, bg="gray81").grid(row=3, column=0)
        Label(self.frame_register_student, text="이름", font=self.font, bg="gray81").grid(row=4, column=0)
        Label(self.frame_register_student, text="학과", font=self.font, bg="gray81").grid(row=1, column=2, padx=15)
        Radiobutton(self.frame_register_student, text="심화컴퓨터공학", value=1, variable=self.radioVar_student, font=self.font, bg="gray81").grid(row=1, column=4, sticky="w")
        Radiobutton(self.frame_register_student, text="글로벌소프트웨어", value=2, variable=self.radioVar_student, font=self.font, bg="gray81").grid(row=2,column=4, sticky="w")
        Radiobutton(self.frame_register_student, text="연계전공", value=3, variable=self.radioVar_student, font=self.font, bg="gray81").grid(row=3,column=4, sticky="w")
        Radiobutton(self.frame_register_student, text="융합전공", value=4, variable=self.radioVar_student, font=self.font, bg="gray81").grid(row=4,column=4, sticky="w")
        Radiobutton(self.frame_register_student, text="복수전공", value=5, variable=self.radioVar_student, font=self.font, bg="gray81").grid(row=5,column=4, sticky="w")
        self._entry_register_id = Entry(self.frame_register_student, font=self.font)
        self._entry_register_pwd = Entry(self.frame_register_student, show='*', font=self.font)
        self._entry_student_id = Entry(self.frame_register_student, font=self.font)
        self._entry_student_name = Entry(self.frame_register_student, font=self.font)
        self.btn_register = Button(self.frame_register_student, text="회원가입", command=self._click_register, bg='gray49', font=self.font)

        # 학생 회원가입란을 실제 배치하는 부분
        self._entry_register_id.grid(row=1, column=1)
        self._entry_register_pwd.grid(row=2, column=1)
        self._entry_student_id.grid(row=3, column=1)
        self._entry_student_name.grid(row=4, column=1)
        self.btn_register.grid(row=6, column=1, pady=5, padx=16)

        # 교직원 회원가입란의 (user_id, user_pw, faculty_id, name, department) 입력란과 버튼
        Label(self.frame_register_faculty, text="ID", anchor='e', font=self.font, bg="gray81").grid(row=1, column=0)
        Label(self.frame_register_faculty, text="Password", font=self.font, bg="gray81").grid(row=2, column=0)
        Label(self.frame_register_faculty, text="교직원 번호", font=self.font, bg="gray81").grid(row=3, column=0)
        Label(self.frame_register_faculty, text="이름", font=self.font, bg="gray81").grid(row=4, column=0)
        Label(self.frame_register_faculty, text="부서", font=self.font, bg="gray81").grid(row=5, column=0)
        self._entry_register_faculty_id = Entry(self.frame_register_faculty, font=self.font)
        self._entry_register_faculty_pwd = Entry(self.frame_register_faculty, show='*', font=self.font)
        self._entry_register_faculty_num = Entry(self.frame_register_faculty, font=self.font)
        self._entry_register_faculty_name = Entry(self.frame_register_faculty, font=self.font)
        self._entry_register_faculty_department = Entry(self.frame_register_faculty, font=self.font)
        self.btn_register_faculty = Button(self.frame_register_faculty, text="회원가입", command=self._click_register, height=2, bg='gray49', font=self.font)

        self._entry_register_faculty_id.grid(row=1, column=1, padx=3)
        self._entry_register_faculty_pwd.grid(row=2, column=1, padx=3)
        self._entry_register_faculty_num.grid(row=3, column=1, padx=3)
        self._entry_register_faculty_name.grid(row=4, column=1, padx=3)
        self._entry_register_faculty_department.grid(row=5, column=1, padx=3)
        self.btn_register_faculty.grid(row=2, column=2, padx=3, rowspan=2)

    def start(self):
        self._draw_main()
        self._draw_select_type()

    def btn_back_handler(self):
        if self.btn_back['text'] == "종료":
            self.window.quit()
        else:
            if self._status == 1:  # 로그인 화면
                self._erase_login()
                self._draw_select_type()
            elif self._status == 2:  # 회원가입 화면
                self._erase_register()
                self._draw_login()

    # 학생/교직원 선택 UI
    def _draw_select_type(self):
        self._status = 0
        self.frame_type.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.btn_back.configure(text='종료')

    # 로그인 화면 UI
    def _draw_login(self):
        self._status = 1
        self.frame_login.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.btn_back.configure(text='뒤로가기')

    def _erase_login(self):
        self._entry_id.delete(0, END)
        self._entry_pwd.delete(0, END)
        self.frame_login.place_forget()

    # 회원가입 화면 UI
    def _draw_register(self):
        self._status = 2
        if self._type_user == "student":
            self.frame_register_student.place(relx=0.5, rely=0.55, anchor=CENTER)
        else:
            self.frame_register_faculty.place(relx=0.5, rely=0.55, anchor=CENTER)

    def _erase_register(self):
        if self._type_user == "student":
            self._entry_register_id.delete(0, END)
            self._entry_register_pwd.delete(0, END)
            self._entry_student_name.delete(0, END)
            self._entry_student_id.delete(0, END)
            self.frame_register_student.place_forget()
        else:
            self._entry_register_faculty_id.delete(0, END)
            self._entry_register_faculty_pwd.delete(0, END)
            self._entry_register_faculty_num.delete(0, END)
            self._entry_register_faculty_name.delete(0, END)
            self._entry_register_faculty_department.delete(0, END)
            self.frame_register_faculty.place_forget()

    # 버튼 처리
    def select_student(self):
        self._type_user = "student"
        self.frame_type.place_forget()
        self._draw_login()

    def select_faculty(self):
        self._type_user = "faculty"
        self.frame_type.place_forget()
        self._draw_login()

    def _click_create_account(self):
        self._erase_login()
        self._draw_register()

    def _click_register(self):
        if self._type_user == "student":
            if not self._entry_register_id.get() or not self._entry_register_pwd.get() or not self._entry_student_id.get():
                messagebox.showerror(title="회원가입 에러", message="입력란을 모두 채워주세요")
                return

            if not self._entry_student_id.get().isdecimal():
                messagebox.showerror(title="회원가입 에러", message="학번을 숫자로 입력해주세요")
                return

            student_pd = Student()
            rad_var = self.radioVar_student.get()
            if rad_var == 1:  # 심컴
                student_pd.register_acc(self._entry_register_id.get(), self._entry_register_pwd.get(),
                                        self._entry_student_id.get(), self._entry_student_name.get(), "DeepCseMajor", True)
            elif rad_var == 2:  # 글솦
                student_pd.register_acc(self._entry_register_id.get(), self._entry_register_pwd.get(),
                                        self._entry_student_id.get(), self._entry_student_name.get(), "GlobalSWMajor", False)
            del student_pd
        else:
            if self._entry_register_faculty_department.get() and self._entry_register_faculty_name.get() and \
                    self._entry_register_faculty_pwd.get() and self._entry_register_faculty_id.get() and \
                    self._entry_register_faculty_num.get():

                if not self._entry_register_faculty_id.get().isdecimal():
                    messagebox.showerror(title="회원가입 에러", message="교직원 번호를 숫자로 입력해주세요")
                    return

                faculty_pd = Faculty()
                faculty_pd.register_acc(self._entry_register_faculty_id.get(), self._entry_register_faculty_pwd.get(),
                                        self._entry_register_faculty_num.get(), self._entry_register_faculty_name.get(),
                                        self._entry_register_faculty_department.get())
                del faculty_pd
            else:
                messagebox.showerror(title="회원가입 에러", message="입력란을 모두 채워주세요")
                return

        self._erase_register()
        self._draw_login()

        messagebox.showinfo(title="회원가입 성공", message="회원가입이 성공했습니다.")

    def _click_login(self):
        if not self._entry_id.get() or not self._entry_pwd.get():
            messagebox.showerror(title="로그인 에러", message="입력란을 모두 채워주세요")
            return

        if self._type_user == "student":
            pd_student = Student()
            if pd_student.login(self._entry_id.get(), self._entry_pwd.get()):
                self._erase_main()
                self._erase_login()
                self.erase_title()
                self._student_main_ui.start(pd_student)
            else:
                del pd_student
                messagebox.showerror(title="로그인 에러", message="아이디 및 비밀번호가 틀렸습니다.")
        else:
            pd_faculty = Faculty()
            if pd_faculty.login(self._entry_id.get(), self._entry_pwd.get()):
                self._erase_main()
                self._erase_login()
                self.erase_title()
                self._faculty_main_ui.start(pd_faculty)
            else:
                messagebox.showerror(title="로그인 에러", message="아이디 및 비밀번호가 틀렸습니다.")
