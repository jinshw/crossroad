# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sectionwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SectionWind(object):
    def setupUi(self, SectionWind):
        SectionWind.setObjectName("SectionWind")
        SectionWind.setEnabled(True)
        SectionWind.resize(1369, 797)
        self.sectionTable = QtWidgets.QTableWidget(SectionWind)
        self.sectionTable.setGeometry(QtCore.QRect(40, 310, 1211, 261))
        self.sectionTable.setObjectName("sectionTable")
        self.sectionTable.setColumnCount(10)
        self.sectionTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionTable.setHorizontalHeaderItem(9, item)
        self.label = QtWidgets.QLabel(SectionWind)
        self.label.setGeometry(QtCore.QRect(60, 50, 21, 16))
        self.label.setObjectName("label")
        self.sLE = QtWidgets.QLineEdit(SectionWind)
        self.sLE.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.sLE.setObjectName("sLE")
        self.leftlansLE = QtWidgets.QLineEdit(SectionWind)
        self.leftlansLE.setGeometry(QtCore.QRect(300, 50, 251, 20))
        self.leftlansLE.setText("")
        self.leftlansLE.setObjectName("leftlansLE")
        self.label_2 = QtWidgets.QLabel(SectionWind)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SectionWind)
        self.label_3.setGeometry(QtCore.QRect(570, 50, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SectionWind)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 71, 20))
        self.label_4.setObjectName("label_4")
        self.centermarkLE = QtWidgets.QLineEdit(SectionWind)
        self.centermarkLE.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.centermarkLE.setObjectName("centermarkLE")
        self.leftmarkLE = QtWidgets.QLineEdit(SectionWind)
        self.leftmarkLE.setGeometry(QtCore.QRect(300, 100, 421, 20))
        self.leftmarkLE.setObjectName("leftmarkLE")
        self.label_5 = QtWidgets.QLabel(SectionWind)
        self.label_5.setGeometry(QtCore.QRect(230, 100, 61, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(SectionWind)
        self.label_6.setGeometry(QtCore.QRect(750, 100, 61, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(SectionWind)
        self.label_7.setGeometry(QtCore.QRect(20, 150, 61, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(SectionWind)
        self.label_8.setGeometry(QtCore.QRect(370, 150, 61, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(SectionWind)
        self.label_9.setGeometry(QtCore.QRect(20, 190, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(SectionWind)
        self.label_10.setGeometry(QtCore.QRect(370, 190, 61, 20))
        self.label_10.setObjectName("label_10")
        self.rightlansLE = QtWidgets.QLineEdit(SectionWind)
        self.rightlansLE.setGeometry(QtCore.QRect(640, 50, 251, 20))
        self.rightlansLE.setObjectName("rightlansLE")
        self.lineEdit_3 = QtWidgets.QLineEdit(SectionWind)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 150, 251, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(SectionWind)
        self.lineEdit_7.setGeometry(QtCore.QRect(440, 150, 251, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(SectionWind)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 190, 251, 20))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(SectionWind)
        self.lineEdit_9.setGeometry(QtCore.QRect(440, 190, 251, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.rightmarkLE = QtWidgets.QLineEdit(SectionWind)
        self.rightmarkLE.setGeometry(QtCore.QRect(820, 100, 421, 20))
        self.rightmarkLE.setObjectName("rightmarkLE")
        self.addBT = QtWidgets.QPushButton(SectionWind)
        self.addBT.setGeometry(QtCore.QRect(330, 270, 75, 23))
        self.addBT.setObjectName("addBT")
        self.deleteBT = QtWidgets.QPushButton(SectionWind)
        self.deleteBT.setGeometry(QtCore.QRect(420, 270, 75, 23))
        self.deleteBT.setObjectName("deleteBT")
        self.calculateBT = QtWidgets.QPushButton(SectionWind)
        self.calculateBT.setGeometry(QtCore.QRect(520, 270, 75, 23))
        self.calculateBT.setObjectName("calculateBT")
        self.saveBT = QtWidgets.QPushButton(SectionWind)
        self.saveBT.setGeometry(QtCore.QRect(610, 270, 75, 23))
        self.saveBT.setObjectName("saveBT")
        self.label_11 = QtWidgets.QLabel(SectionWind)
        self.label_11.setGeometry(QtCore.QRect(40, 270, 41, 20))
        self.label_11.setObjectName("label_11")
        self.readBT = QtWidgets.QPushButton(SectionWind)
        self.readBT.setGeometry(QtCore.QRect(220, 270, 75, 23))
        self.readBT.setObjectName("readBT")
        self.roadidCBB = QtWidgets.QComboBox(SectionWind)
        self.roadidCBB.setGeometry(QtCore.QRect(90, 270, 111, 22))
        self.roadidCBB.setObjectName("roadidCBB")

        self.retranslateUi(SectionWind)
        QtCore.QMetaObject.connectSlotsByName(SectionWind)

    def retranslateUi(self, SectionWind):
        _translate = QtCore.QCoreApplication.translate
        SectionWind.setWindowTitle(_translate("SectionWind", "Section"))
        item = self.sectionTable.horizontalHeaderItem(0)
        item.setText(_translate("SectionWind", "s"))
        item = self.sectionTable.horizontalHeaderItem(1)
        item.setText(_translate("SectionWind", "leftlans"))
        item = self.sectionTable.horizontalHeaderItem(2)
        item.setText(_translate("SectionWind", "rightlans"))
        item = self.sectionTable.horizontalHeaderItem(3)
        item.setText(_translate("SectionWind", "centermark"))
        item = self.sectionTable.horizontalHeaderItem(4)
        item.setText(_translate("SectionWind", "leftmark"))
        item = self.sectionTable.horizontalHeaderItem(5)
        item.setText(_translate("SectionWind", "rightmark"))
        item = self.sectionTable.horizontalHeaderItem(6)
        item.setText(_translate("SectionWind", "leftpre"))
        item = self.sectionTable.horizontalHeaderItem(7)
        item.setText(_translate("SectionWind", "rightpre"))
        item = self.sectionTable.horizontalHeaderItem(8)
        item.setText(_translate("SectionWind", "leftsuc"))
        item = self.sectionTable.horizontalHeaderItem(9)
        item.setText(_translate("SectionWind", "rightsuc"))
        self.label.setText(_translate("SectionWind", "s："))
        self.label_2.setText(_translate("SectionWind", "leftlans："))
        self.label_3.setText(_translate("SectionWind", "rightlans："))
        self.label_4.setText(_translate("SectionWind", "centermark："))
        self.centermarkLE.setText(_translate("SectionWind", "solid"))
        self.leftmarkLE.setText(_translate("SectionWind", "solid"))
        self.label_5.setText(_translate("SectionWind", "leftmark："))
        self.label_6.setText(_translate("SectionWind", "rightmark："))
        self.label_7.setText(_translate("SectionWind", "leftpre："))
        self.label_8.setText(_translate("SectionWind", "rightpre："))
        self.label_9.setText(_translate("SectionWind", "leftsuc："))
        self.label_10.setText(_translate("SectionWind", "rightsuc："))
        self.rightlansLE.setText(_translate("SectionWind", "3.75;3.75;3.75;3.5"))
        self.lineEdit_7.setText(_translate("SectionWind", "-1;-2;-3;-4;-5;-6;-7;-8;-9;-10;-11;-12"))
        self.lineEdit_9.setText(_translate("SectionWind", "-1;-2;-3;-4;-5;-6;-7;-8;-9;-10;-11;-12"))
        self.rightmarkLE.setText(_translate("SectionWind", "broken;broken;broken;solid;broken;broken;broken;solid;broken;solid"))
        self.addBT.setText(_translate("SectionWind", "添加行"))
        self.deleteBT.setText(_translate("SectionWind", "删除行"))
        self.calculateBT.setText(_translate("SectionWind", "计算"))
        self.saveBT.setText(_translate("SectionWind", "保存"))
        self.label_11.setText(_translate("SectionWind", "道路ID："))
        self.readBT.setText(_translate("SectionWind", "读取"))

