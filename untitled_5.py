# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(894, 668)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(690, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(670, 50, 171, 161))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 70, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 110, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(670, 230, 171, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(674, 282, 171, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Вид карты"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.radioButton.setText(_translate("Form", "Схема"))
        self.radioButton_2.setText(_translate("Form", "Спутник"))
        self.radioButton_3.setText(_translate("Form", "Гибрид"))
        self.pushButton.setText(_translate("Form", "Искать"))
