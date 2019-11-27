import tkinter
import tkinter.font
from LoginUI import *

def main():
    # window 생성
    window = tkinter.Tk()

    # window 기본 설정
    window.title("학생 경력 관리 시스템")
    window.geometry("940x600+300+100")
    window.resizable(False, False)

    font = tkinter.font.Font(family="맑은 고딕", size=20)

    loginUI = LoginUI(window, font)


    window.mainloop()


if __name__ == '__main__':
    main()