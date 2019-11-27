from tkinter import *

class LoginUI:
    def __init__(self, window, font):
        self.window = window
        self.font = font

        frame1 = Frame(window)
        frame1.pack()

        self.entry_id = Entry(frame1, font=font)
        self.entry_pwd = Entry(frame1, font=font)

        btn_login = Button(frame1, text="로그인", command=self.login, height=2, font=font)

        self.entry_id.grid(row=0, column=0)
        self.entry_pwd.grid(row=1, column=0)
        btn_login.grid(row=0, column=1, rowspan=2)

    def login(self):
        print(self.entry_id.get(), self.entry_pwd.get(), sep="\n")
        pass