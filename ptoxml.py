# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ptoxml.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PointToXML(object):
    def setupUi(self, PointToXML):
        PointToXML.setObjectName("PointToXML")
        PointToXML.resize(556, 229)
        self.openBT = QtWidgets.QPushButton(PointToXML)
        self.openBT.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.openBT.setObjectName("openBT")
        self.pathLE = QtWidgets.QLineEdit(PointToXML)
        self.pathLE.setGeometry(QtCore.QRect(140, 80, 301, 20))
        self.pathLE.setObjectName("pathLE")

        self.retranslateUi(PointToXML)
        QtCore.QMetaObject.connectSlotsByName(PointToXML)

    def retranslateUi(self, PointToXML):
        _translate = QtCore.QCoreApplication.translate
        PointToXML.setWindowTitle(_translate("PointToXML", "Form"))
        self.openBT.setText(_translate("PointToXML", "打开"))

