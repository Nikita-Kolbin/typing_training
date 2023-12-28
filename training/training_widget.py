import datetime
from random import choices, randint
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer

from base_widget import BaseWidget
from .ui_training import Ui_Train
from .exit_dialog.exit_dialog import ExitDialog
from .result.result_dialog import ResultDialog
from storage.storage_sqlite import Storage

class TrainingWidget(BaseWidget):
    def __init__(self, main_window, mode):
        super().__init__()
        self.storage = Storage()
        self.main_window = main_window
        self.mode = mode
        self.started = False
        self.pause = True
        self.second_counter = 0
        self.char_counter = 0
        self.misprint_counter = 0

        self.ui = Ui_Train()
        self.ui.setupUi(self)

        self.words = self.parse_words(mode.language)
        if mode.limit_for == 'words':
            self.sequence = self.gen_seq(self.words, mode.limit, mode.capital_letters)
        else:
            self.sequence = self.gen_seq(self.words, 20, mode.capital_letters)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        if not self.pause:
            self.second_counter += 1
            self.ui.timer.setText(self.format_time())

            if self.mode.limit_for == 'time':
                self.ui.progress_bar.setValue(int(self.second_counter / (self.mode.limit * 60) * 100))
                if self.second_counter / 60 >= self.mode.limit:
                    self.end()

    def update_text(self, char):
        if len(char) == 0:
            return
        if char == self.ui.right.text()[0]:
            self.ui.left.setText(self.ui.left.text() + self.ui.right.text()[0])
            self.ui.right.setText(self.ui.right.text()[1:])
            self.char_counter += 1
        else:
            self.misprint_counter += 1

        if self.mode.limit_for == 'words':
            self.ui.progress_bar.setValue(int((1 - len(self.ui.right.text()) / len(self.sequence)) * 100))
            if len(self.ui.right.text()) == 0:
                self.end()

        if self.mode.limit_for == 'time' and len(self.ui.right.text()) < 50:
            self.ui.right.setText(self.ui.right.text() + self.gen_seq(self.words, 20, self.mode.capital_letters))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.pause = True
            self.open_exit_window()
        elif not self.started and event.key() == QtCore.Qt.Key.Key_Space:
            self.start()
        else:
            self.pause = False
            self.update_text(event.text())

    def open_exit_window(self):
        dlg = ExitDialog(self)
        dlg.exec()

    def open_result_window(self):
        dlg = ResultDialog(self)
        dlg.exec()

    def start(self):
        self.ui.left.setText(' ')
        self.ui.right.setText(self.sequence)
        self.started = True
        self.pause = False

    def end(self):
        self.pause = True
        self.storage.add_train(datetime.date.today(), self.mode.language, self.get_speed(), self.get_accuracy())
        self.open_result_window()

    def restart(self):
        self.main_window.open_training(self.mode)
        self.close()

    def exit(self):
        self.main_window.open_menu()
        self.close()

    def format_time(self) -> str:
        time = str(self.second_counter // 60).rjust(2, '0')
        time += ':'
        time += str(self.second_counter % 60).rjust(2, '0')
        return time

    def get_speed(self):
        return str(int(self.char_counter / self.second_counter * 60) if self.second_counter > 0 else 0) + ' зн/мин'

    def get_accuracy(self):
        char = self.char_counter
        miss = self.misprint_counter
        return str(round(char / (char + miss) * 100, 1) if char > 0 else 0) + '%'

    @staticmethod
    def gen_seq(words: [str], cnt: int, cap: bool) -> str:
        if not cap:
            return ' '.join(choices(words, k=cnt))
        res = choices(words, k=cnt)
        for i in range(cnt):
            if randint(0, 100) < 70:
                res[i] = res[i][0].upper() + res[i][1:]
        return ' '.join(res)

    @staticmethod
    def parse_words(lang: str) -> [str]:
        with open(f'data/{lang}.txt', 'r', encoding='utf-8') as file:
            res = file.read().split('\n')
        return res
