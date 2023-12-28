from PyQt6.QtWidgets import QMainWindow

from .ui_main_window import Ui_MainWindow
from training.training_widget import TrainingWidget
from menu.menu_widget import MenuWidget
from stats.statistics_widget import StatisticsWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Слепая печать")

        self.open_menu()

    def open_menu(self):
        self.setCentralWidget(MenuWidget(self))

    def open_training(self, mode):
        self.setCentralWidget(TrainingWidget(self, mode))

    def open_statistics(self):
        self.setCentralWidget(StatisticsWidget(self))

    def keyPressEvent(self, event):
        return self.centralWidget().keyPressEvent(event)
