# Form implementation generated from reading ui file '.\menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(667, 485)
        Menu.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Menu)
        self.frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.start = QtWidgets.QPushButton(parent=self.frame)
        self.start.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.start.setFont(font)
        self.start.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.start.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"")
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 0, 0, 1, 1)
        self.statistics = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.statistics.setFont(font)
        self.statistics.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"\n"
"")
        self.statistics.setObjectName("statistics")
        self.gridLayout.addWidget(self.statistics, 1, 0, 1, 1)
        self.settings = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.settings.setFont(font)
        self.settings.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"")
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 2, 0, 1, 1)
        self.exit = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"")
        self.exit.setObjectName("exit")
        self.gridLayout.addWidget(self.exit, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Form"))
        self.start.setText(_translate("Menu", "Начать"))
        self.statistics.setText(_translate("Menu", "Статистика"))
        self.settings.setText(_translate("Menu", "Настройки"))
        self.exit.setText(_translate("Menu", "Выход"))
