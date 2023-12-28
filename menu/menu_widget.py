from .ui_menu import Ui_Menu
from training.mode_dialog.mode_dialog import ModeDialog

from base_widget import BaseWidget


class MenuWidget(BaseWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_Menu()
        self.ui.setupUi(self)

        self.ui.start.clicked.connect(self.open_start_dialog)
        self.ui.statistics.clicked.connect(self.open_statistics)

        self.ui.exit.clicked.connect(self.exit)

    def open_start_dialog(self):
        dlg = ModeDialog(self.main_window)
        dlg.exec()

    def open_statistics(self):
        self.main_window.open_statistics()

    def exit(self):
        self.exit()
