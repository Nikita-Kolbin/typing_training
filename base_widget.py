from PyQt6.QtWidgets import QWidget


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        pass