# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diffs.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_diffs(object):
    def setupUi(self, diffs):
        diffs.setObjectName("diffs")
        diffs.resize(1853, 808)
        self.retainRadioButton = QtWidgets.QRadioButton(diffs)
        self.retainRadioButton.setGeometry(QtCore.QRect(50, 20, 141, 16))
        self.retainRadioButton.setObjectName("retainRadioButton")
        self.replaceRadioButton = QtWidgets.QRadioButton(diffs)
        self.replaceRadioButton.setGeometry(QtCore.QRect(360, 20, 141, 16))
        self.replaceRadioButton.setObjectName("replaceRadioButton")
        self.leftOpenBT = QtWidgets.QPushButton(diffs)
        self.leftOpenBT.setGeometry(QtCore.QRect(480, 60, 75, 23))
        self.leftOpenBT.setObjectName("leftOpenBT")
        self.leftPathLE = QtWidgets.QLineEdit(diffs)
        self.leftPathLE.setGeometry(QtCore.QRect(90, 60, 381, 20))
        self.leftPathLE.setObjectName("leftPathLE")
        self.label = QtWidgets.QLabel(diffs)
        self.label.setGeometry(QtCore.QRect(30, 60, 51, 16))
        self.label.setObjectName("label")
        self.rightPathLE = QtWidgets.QLineEdit(diffs)
        self.rightPathLE.setGeometry(QtCore.QRect(1030, 50, 381, 21))
        self.rightPathLE.setObjectName("rightPathLE")
        self.rightOpenBT = QtWidgets.QPushButton(diffs)
        self.rightOpenBT.setGeometry(QtCore.QRect(1420, 50, 75, 23))
        self.rightOpenBT.setObjectName("rightOpenBT")
        self.label_2 = QtWidgets.QLabel(diffs)
        self.label_2.setGeometry(QtCore.QRect(980, 50, 51, 21))
        self.label_2.setObjectName("label_2")
        self.leftTreeWidget = QtWidgets.QTreeWidget(diffs)
        self.leftTreeWidget.setGeometry(QtCore.QRect(20, 160, 851, 501))
        self.leftTreeWidget.setObjectName("leftTreeWidget")
        self.leftSelectAllBT = QtWidgets.QPushButton(diffs)
        self.leftSelectAllBT.setGeometry(QtCore.QRect(20, 120, 75, 23))
        self.leftSelectAllBT.setObjectName("leftSelectAllBT")
        self.leftClearBT = QtWidgets.QPushButton(diffs)
        self.leftClearBT.setGeometry(QtCore.QRect(110, 120, 75, 23))
        self.leftClearBT.setObjectName("leftClearBT")
        self.rightTreeWidget = QtWidgets.QTreeWidget(diffs)
        self.rightTreeWidget.setGeometry(QtCore.QRect(950, 160, 851, 501))
        self.rightTreeWidget.setObjectName("rightTreeWidget")
        self.runBT = QtWidgets.QPushButton(diffs)
        self.runBT.setGeometry(QtCore.QRect(210, 120, 75, 23))
        self.runBT.setObjectName("runBT")
        self.rightClearBT = QtWidgets.QPushButton(diffs)
        self.rightClearBT.setGeometry(QtCore.QRect(1040, 120, 75, 23))
        self.rightClearBT.setObjectName("rightClearBT")
        self.rightSelectAllBT = QtWidgets.QPushButton(diffs)
        self.rightSelectAllBT.setGeometry(QtCore.QRect(950, 120, 75, 23))
        self.rightSelectAllBT.setObjectName("rightSelectAllBT")
        self.rightRemoveBT = QtWidgets.QPushButton(diffs)
        self.rightRemoveBT.setGeometry(QtCore.QRect(1140, 120, 75, 23))
        self.rightRemoveBT.setObjectName("rightRemoveBT")
        self.replaceAddRadioButton = QtWidgets.QRadioButton(diffs)
        self.replaceAddRadioButton.setGeometry(QtCore.QRect(210, 20, 141, 16))
        self.replaceAddRadioButton.setObjectName("replaceAddRadioButton")
        self.readRightBT = QtWidgets.QPushButton(diffs)
        self.readRightBT.setGeometry(QtCore.QRect(1510, 50, 75, 23))
        self.readRightBT.setObjectName("readRightBT")
        self.leftRoadidLE = QtWidgets.QLineEdit(diffs)
        self.leftRoadidLE.setGeometry(QtCore.QRect(340, 120, 181, 20))
        self.leftRoadidLE.setObjectName("leftRoadidLE")
        self.leftFilterBT = QtWidgets.QPushButton(diffs)
        self.leftFilterBT.setGeometry(QtCore.QRect(530, 120, 75, 23))
        self.leftFilterBT.setObjectName("leftFilterBT")
        self.rightFilterBT = QtWidgets.QPushButton(diffs)
        self.rightFilterBT.setGeometry(QtCore.QRect(1450, 120, 75, 23))
        self.rightFilterBT.setObjectName("rightFilterBT")
        self.rightRoadidLE = QtWidgets.QLineEdit(diffs)
        self.rightRoadidLE.setGeometry(QtCore.QRect(1260, 120, 181, 20))
        self.rightRoadidLE.setObjectName("rightRoadidLE")

        self.retranslateUi(diffs)
        QtCore.QMetaObject.connectSlotsByName(diffs)

    def retranslateUi(self, diffs):
        _translate = QtCore.QCoreApplication.translate
        diffs.setWindowTitle(_translate("diffs", "Form"))
        self.retainRadioButton.setText(_translate("diffs", "保留原有数据和新增"))
        self.replaceRadioButton.setText(_translate("diffs", "替换全部数据"))
        self.leftOpenBT.setText(_translate("diffs", "打开"))
        self.label.setText(_translate("diffs", "xodr文件："))
        self.rightOpenBT.setText(_translate("diffs", "打开"))
        self.label_2.setText(_translate("diffs", "xml文件："))
        self.leftTreeWidget.headerItem().setText(0, _translate("diffs", "id"))
        self.leftTreeWidget.headerItem().setText(1, _translate("diffs", "type"))
        self.leftTreeWidget.headerItem().setText(2, _translate("diffs", "name"))
        self.leftTreeWidget.headerItem().setText(3, _translate("diffs", "s"))
        self.leftTreeWidget.headerItem().setText(4, _translate("diffs", "t"))
        self.leftTreeWidget.headerItem().setText(5, _translate("diffs", "zOffset"))
        self.leftSelectAllBT.setText(_translate("diffs", "全选"))
        self.leftClearBT.setText(_translate("diffs", "取消"))
        self.rightTreeWidget.headerItem().setText(0, _translate("diffs", "id"))
        self.rightTreeWidget.headerItem().setText(1, _translate("diffs", "type"))
        self.rightTreeWidget.headerItem().setText(2, _translate("diffs", "name"))
        self.rightTreeWidget.headerItem().setText(3, _translate("diffs", "s"))
        self.rightTreeWidget.headerItem().setText(4, _translate("diffs", "t"))
        self.rightTreeWidget.headerItem().setText(5, _translate("diffs", "zOffset"))
        self.runBT.setText(_translate("diffs", "执行"))
        self.rightClearBT.setText(_translate("diffs", "取消"))
        self.rightSelectAllBT.setText(_translate("diffs", "全选"))
        self.rightRemoveBT.setText(_translate("diffs", "删除"))
        self.replaceAddRadioButton.setText(_translate("diffs", "替换和新增"))
        self.readRightBT.setText(_translate("diffs", "重新读取"))
        self.leftFilterBT.setText(_translate("diffs", "筛选"))
        self.rightFilterBT.setText(_translate("diffs", "筛选"))

