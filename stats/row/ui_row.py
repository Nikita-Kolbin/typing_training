# Form implementation generated from reading ui file '.\row.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Row(object):
    def setupUi(self, Row):
        Row.setObjectName("Row")
        Row.resize(563, 43)
        Row.setMaximumSize(QtCore.QSize(16777215, 50))
        Row.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Row)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.date = QtWidgets.QLabel(parent=Row)
        self.date.setStyleSheet("color: rgb(255, 255, 255);")
        self.date.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date.setObjectName("date")
        self.horizontalLayout.addWidget(self.date)
        self.lang = QtWidgets.QLabel(parent=Row)
        self.lang.setStyleSheet("color: rgb(255, 255, 255);")
        self.lang.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lang.setObjectName("lang")
        self.horizontalLayout.addWidget(self.lang)
        self.speed = QtWidgets.QLabel(parent=Row)
        self.speed.setStyleSheet("color: rgb(255, 255, 255);")
        self.speed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.speed.setObjectName("speed")
        self.horizontalLayout.addWidget(self.speed)
        self.accuracy = QtWidgets.QLabel(parent=Row)
        self.accuracy.setStyleSheet("color: rgb(255, 255, 255);")
        self.accuracy.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.accuracy.setObjectName("accuracy")
        self.horizontalLayout.addWidget(self.accuracy)
        self.remove = QtWidgets.QPushButton(parent=Row)
        self.remove.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.remove.setObjectName("remove")
        self.horizontalLayout.addWidget(self.remove)

        self.retranslateUi(Row)
        QtCore.QMetaObject.connectSlotsByName(Row)

    def retranslateUi(self, Row):
        _translate = QtCore.QCoreApplication.translate
        Row.setWindowTitle(_translate("Row", "Form"))
        self.date.setText(_translate("Row", "11.11.2011"))
        self.lang.setText(_translate("Row", "rus"))
        self.speed.setText(_translate("Row", "100 зн/мин"))
        self.accuracy.setText(_translate("Row", "69%"))
        self.remove.setText(_translate("Row", "Удалить"))
