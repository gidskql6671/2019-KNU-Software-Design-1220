from tkinter import *
from tkinter import messagebox
import abc


class UITemplate:
    def __init__(self, window: Tk, font):
        self.window = window
        self.font = font

    def _setting_ui(self):
        self.frame_main = Frame(self.window, borderwidth=2, relief="groove", bg="gray86", padx=10, pady=10)

        self.label_title = Label(self.window, text="학생 경력 관리 시스템", font=("맑은 고딕", 30), bg="gray86")
        self.btn_back = Button(self.frame_main, text="뒤로가기", font=("맑은 고딕", 12), command=self.btn_back_handler)

        self.draw_btn_back()

    def draw_title(self):
        self.label_title.place(relx=0.5, rely=0.2, anchor=CENTER)

    def erase_title(self):
        self.label_title.place_forget()

    def draw_btn_back(self):
        self.btn_back.pack(side="left", anchor="s")

    def erase_btn_back(self):
        self.btn_back.pack_forget()

    @ abc.abstractmethod
    def btn_back_handler(self):
        pass

    def _draw_main(self):
        self.draw_title()
        self.frame_main.pack(padx=30, pady=40, ipadx=20, ipady=20, anchor=CENTER, expand=True, fill="both")

    def _erase_main(self):
        self.erase_title()
        self.frame_main.pack_forget()
