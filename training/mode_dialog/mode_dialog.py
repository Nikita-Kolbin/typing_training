from PyQt6.QtWidgets import QDialog

from .ui_mode import Ui_Mode


class Mode:
    def __init__(self, lang='rus', lim_for='words', lim=10, cap=False):
        self.language = lang
        self.limit_for = lim_for
        self.limit = lim
        self.capital_letters = cap


class ModeDialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_Mode()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.start)
        self.ui.buttonBox.rejected.connect(self.cancel)

        self.ui.time_limit.hide()
        self.ui.choose_time_limit.hide()

        self.ui.choose_limit.currentIndexChanged.connect(self.change_limit)

    def change_limit(self):
        if self.ui.choose_limit.currentIndex() == 0:
            self.ui.time_limit.hide()
            self.ui.choose_time_limit.hide()
            self.ui.words_limit.show()
            self.ui.choose_words_limit.show()
        else:
            self.ui.time_limit.show()
            self.ui.choose_time_limit.show()
            self.ui.words_limit.hide()
            self.ui.choose_words_limit.hide()

    def start(self):
        mode = Mode()
        mode.language = 'rus' if self.ui.choose_language.currentIndex() == 0 else 'eng'
        mode.limit_for = 'words' if self.ui.choose_limit.currentIndex() == 0 else 'time'

        if self.ui.choose_limit.currentIndex() == 0:
            mode.limit = int(self.ui.choose_words_limit.text())
        else:
            mode.limit = int(self.ui.choose_time_limit.text())

        mode.capital_letters = self.ui.choose_capital_letter.isChecked()

        self.main_window.open_training(mode)
        self.deleteLater()

    def cancel(self):
        self.deleteLater()
