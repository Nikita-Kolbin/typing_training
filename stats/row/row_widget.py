from PyQt6.QtWidgets import QWidget

from .ui_row  import Ui_Row


class RowWidget(QWidget):
    def __init__(self, stats, id, date, lang, speed, accuracy):
        super().__init__()

        self.ui = Ui_Row()
        self.ui.setupUi(self)

        self.stats = stats
        self.id = id
        self.ui.date.setText(date)
        self.ui.lang.setText(lang)
        self.ui.speed.setText(speed)
        self.ui.accuracy.setText(accuracy)

        self.ui.remove.clicked.connect(self.remove)

    def remove(self):
        self.stats.remove_train(self)


