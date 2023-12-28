from PyQt6.QtCore import Qt

from .ui_statistics import Ui_Statistics
from .row.row_widget import RowWidget
from storage.storage_sqlite import Storage
from base_widget import BaseWidget


class StatisticsWidget(BaseWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_Statistics()
        self.ui.setupUi(self)

        self.ui.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)

        self.storage = Storage()
        self.fill_table()

    def fill_table(self):
        rows = self.storage.get_trains()
        for row in rows[::-1]:
            widget = RowWidget(self, row[0], row[1], row[2], row[3], row[4])
            self.ui.scrollAreaWidgetContents.layout().addWidget(widget)

    def remove_train(self, w):
        self.storage.del_train(w.id)
        self.ui.scrollAreaWidgetContents.layout().removeWidget(w)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.exit()

    def exit(self):
        self.main_window.open_menu()
        self.close()
