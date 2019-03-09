# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addname.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddFileName(object):
    def setupUi(self, AddFileName):
        AddFileName.setObjectName("AddFileName")
        AddFileName.resize(413, 149)
        self.selectBT = QtWidgets.QPushButton(AddFileName)
        self.selectBT.setGeometry(QtCore.QRect(320, 60, 75, 23))
        self.selectBT.setObjectName("selectBT")
        self.path = QtWidgets.QLineEdit(AddFileName)
        self.path.setGeometry(QtCore.QRect(20, 60, 281, 20))
        self.path.setObjectName("path")

        self.retranslateUi(AddFileName)
        QtCore.QMetaObject.connectSlotsByName(AddFileName)

    def retranslateUi(self, AddFileName):
        _translate = QtCore.QCoreApplication.translate
        AddFileName.setWindowTitle(_translate("AddFileName", "Form"))
        self.selectBT.setText(_translate("AddFileName", "选择文件夹"))

