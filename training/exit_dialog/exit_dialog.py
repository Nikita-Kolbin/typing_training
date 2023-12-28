from PyQt6.QtWidgets import QDialog

from .ui_exit import Ui_Exit


class ExitDialog(QDialog):
    def __init__(self, train_widget):
        super().__init__()
        self.train_widget = train_widget

        self.ui = Ui_Exit()
        self.ui.setupUi(self)

        char = train_widget.char_counter

        self.ui.time.setText("Время: " + train_widget.format_time())
        self.ui.count.setText("Символы: " + str(char))
        self.ui.speed.setText("Скорость: " + train_widget.get_speed())
        self.ui.accuracy.setText("Точность: " + train_widget.get_accuracy())

        self.ui.exit.pressed.connect(self.close)
        self.ui.restart.pressed.connect(self.restart)
        self.ui.cancel.pressed.connect(self.cancel)

    def close(self):
        self.train_widget.exit()
        self.deleteLater()

    def restart(self):
        self.train_widget.restart()
        self.deleteLater()

    def cancel(self):
        self.deleteLater()
