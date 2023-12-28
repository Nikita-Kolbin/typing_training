import sys
from PyQt6.QtWidgets import QApplication

from main_window.main_window import MainWindow

# pyuic6 -o login_form.py main_window.ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

