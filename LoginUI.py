from tkinter import *
from tkinter import messagebox


class LoginUI:
    def __init__(self, window: Tk, font):
        self.window = window
        self.font = font
        self._entry_student_id = None
        self.frame_login = Frame(self.window)
        frame1 = Frame(self.frame_login)
        frame2 = Frame(self.frame_login)
        self.frame_register = Frame(self.window)

        # ID, PWD 입력란과 버튼
        self.radVar_login = IntVar()
        rb_student = Radiobutton(frame1, text="학생", variable=self.radVar_login, value=1, width=4)
        rb_student.select()
        rb_faculty = Radiobutton(frame1, text="교직원", variable=self.radVar_login, value=2, width=4)
        label_id = Label(self.frame_login, text="ID", font=self.font, anchor='e')
        label_pwd = Label(self.frame_login, text="Password", font=self.font)
        self._entry_id = Entry(self.frame_login, font=self.font)
        self._entry_pwd = Entry(self.frame_login, font=self.font, show='*')
        self.btn_login = Button(self.frame_login, text="로그인", command=self._click_login, height=2, bg='gray49', font=self.font)

        # 회원가입 문구와 버튼
        register_label = Label(frame2, text="계정이 없다면 ")
        register_label.config(font=("맑은 고딕", 12))
        btn_register = Button(frame2, text="회원가입", command=self._click_create_account, fg="blue", relief=FLAT)
        btn_register.config(font=("맑은 고딕", 12))

        # 로그인 화면을 실제 배치하는 구문
        rb_student.grid(row=0, column=0)
        rb_faculty.grid(row=0, column=1,  padx=20)
        frame1.grid(row=0, column=1)
        label_id.grid(row=1, column=0)
        label_pwd.grid(row=2, column=0)
        self._entry_id.grid(row=1, column=1)
        self._entry_pwd.grid(row=2, column=1)
        self.btn_login.grid(row=1, column=2, padx=10, rowspan=2)

        frame2.grid(row=3, column=1)
        register_label.grid(row=1, column=0)
        btn_register.grid(row=1, column=1)

        # 회원가입란의 ID, PWD, 학번 입력란과 버튼
        self.radVar_register = IntVar()
        frame2 = Frame(self.frame_register)
        rb_student_r = Radiobutton(frame2, text="학생", variable=self.radVar_register, value=1, width=4)
        rb_student_r.select()
        rb_faculty_r = Radiobutton(frame2, text="교직원", variable=self.radVar_register, value=2, width=4)
        label_id2 = Label(self.frame_register, text="ID", font=self.font, anchor='e')
        label_pwd2 = Label(self.frame_register, text="Password", font=self.font)
        label_student_id = Label(self.frame_register, text="학번", font=self.font)
        self._entry_register_id = Entry(self.frame_register, font=self.font)
        self._entry_register_pwd = Entry(self.frame_register, font=self.font, show='*')
        self._entry_student_id = Entry(self.frame_register, font=self.font)

        self.btn_login = Button(self.frame_register, text="회원가입", command=self._click_register, height=2, bg='gray49', font=self.font)

        rb_student_r.grid(row=0, column=0)
        rb_faculty_r.grid(row=0, column=1,  padx=20)
        frame2.grid(row=0, column=1)
        label_id2.grid(row=1, column=0)
        label_pwd2.grid(row=2, column=0)
        label_student_id.grid(row=3, column=0)
        self._entry_register_id.grid(row=1, column=1)
        self._entry_register_pwd.grid(row=2, column=1)
        self._entry_student_id.grid(row=3, column=1)
        self.btn_login.grid(row=1, column=2, padx=10, rowspan=3)

    def start(self):
        self._draw_login()

    def _draw_login(self):
        self.frame_login.place(relx=0.5, rely=0.45, anchor=CENTER)

    def _draw_register(self):
        self.frame_register.place(relx=0.5, rely=0.45, anchor=CENTER)

    def _click_create_account(self):
        self._erase_login()
        self._draw_register()

    def _erase_login(self):
        self.frame_login.place_forget()

    def _erase_register(self):
        self.frame_register.place_forget()

    def _click_register(self):
        if not self._entry_register_id.get() or not self._entry_register_pwd.get() or not self._entry_student_id.get():
            messagebox.showerror(title="회원가입 에러", message="입력란을 모두 채워주세요")
            return

        if self.radVar_register.get() == 1:
            print(self._entry_register_id.get(), self._entry_register_pwd.get(), self._entry_student_id.get(), "학생임")
        else:
            print(self._entry_register_id.get(), self._entry_register_pwd.get(), self._entry_student_id.get(), "교직원임")

        self._erase_register()
        self._draw_login()

    def _click_login(self):
        if not self._entry_id.get() or not self._entry_pwd.get():
            messagebox.showerror(title="로그인 에러", message="입력란을 모두 채워주세요")
            return

        if self.radVar_login.get() == 1: # 학생
            print(self._entry_id.get(), self._entry_pwd.get(), "학생임")
        else:
            print(self._entry_id.get(), self._entry_pwd.get(), "교직원임")
