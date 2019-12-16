from UI.UITemplate import *
from UI.FacultyMainUI import *
from UserAccount.Faculty import Faculty


class FacultyQnAUI(UITemplate):
    def __init__(self, window: Tk, font, mainmenu_ui):
        super().__init__(window, font)

        self._mainmenu_ui = mainmenu_ui

        self._setting_ui()

    def _setting_ui(self):
        super()._setting_ui()

    def start(self):
        pass

    def btn_back_handler(self):
        self._erase_main()
        self._mainmenu_ui.start()
