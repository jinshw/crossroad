# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'props.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PropsWin(object):
    def setupUi(self, PropsWin):
        PropsWin.setObjectName("PropsWin")
        PropsWin.setEnabled(True)
        PropsWin.resize(1382, 897)
        PropsWin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2 = QtWidgets.QLabel(PropsWin)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.lansLineTable = QtWidgets.QTableWidget(PropsWin)
        self.lansLineTable.setEnabled(True)
        self.lansLineTable.setGeometry(QtCore.QRect(40, 130, 231, 171))
        self.lansLineTable.setObjectName("lansLineTable")
        self.lansLineTable.setColumnCount(2)
        self.lansLineTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lansLineTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lansLineTable.setHorizontalHeaderItem(1, item)
        self.label_3 = QtWidgets.QLabel(PropsWin)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 31, 21))
        self.label_3.setObjectName("label_3")
        self.sNumLineEdit = QtWidgets.QLineEdit(PropsWin)
        self.sNumLineEdit.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.sNumLineEdit.setObjectName("sNumLineEdit")
        self.lanswidthstatCheckBox = QtWidgets.QCheckBox(PropsWin)
        self.lanswidthstatCheckBox.setGeometry(QtCore.QRect(40, 340, 91, 21))
        self.lanswidthstatCheckBox.setObjectName("lanswidthstatCheckBox")
        self.closeborderComboBox = QtWidgets.QComboBox(PropsWin)
        self.closeborderComboBox.setEnabled(True)
        self.closeborderComboBox.setGeometry(QtCore.QRect(130, 380, 171, 22))
        self.closeborderComboBox.setObjectName("closeborderComboBox")
        self.closeborderComboBox.addItem("")
        self.closeborderComboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(PropsWin)
        self.label_4.setGeometry(QtCore.QRect(40, 380, 71, 21))
        self.label_4.setObjectName("label_4")
        self.markLineTable = QtWidgets.QTableWidget(PropsWin)
        self.markLineTable.setEnabled(True)
        self.markLineTable.setGeometry(QtCore.QRect(310, 130, 511, 171))
        self.markLineTable.setObjectName("markLineTable")
        self.markLineTable.setColumnCount(3)
        self.markLineTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.markLineTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.markLineTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.markLineTable.setHorizontalHeaderItem(2, item)
        self.label_5 = QtWidgets.QLabel(PropsWin)
        self.label_5.setGeometry(QtCore.QRect(310, 70, 71, 21))
        self.label_5.setObjectName("label_5")
        self.closeborderTable = QtWidgets.QTableWidget(PropsWin)
        self.closeborderTable.setEnabled(True)
        self.closeborderTable.setGeometry(QtCore.QRect(40, 450, 421, 161))
        self.closeborderTable.setObjectName("closeborderTable")
        self.closeborderTable.setColumnCount(4)
        self.closeborderTable.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.closeborderTable.setItem(2, 3, item)
        self.label_6 = QtWidgets.QLabel(PropsWin)
        self.label_6.setGeometry(QtCore.QRect(40, 650, 61, 21))
        self.label_6.setObjectName("label_6")
        self.leftCurveLE = QtWidgets.QLineEdit(PropsWin)
        self.leftCurveLE.setGeometry(QtCore.QRect(200, 650, 91, 20))
        self.leftCurveLE.setObjectName("leftCurveLE")
        self.leftCurveCBB = QtWidgets.QComboBox(PropsWin)
        self.leftCurveCBB.setEnabled(True)
        self.leftCurveCBB.setGeometry(QtCore.QRect(100, 650, 91, 22))
        self.leftCurveCBB.setObjectName("leftCurveCBB")
        self.leftCurveCBB.addItem("")
        self.leftCurveCBB.addItem("")
        self.leftCurveCBB.addItem("")
        self.leftCurveCBB.addItem("")
        self.rightCurveLE = QtWidgets.QLineEdit(PropsWin)
        self.rightCurveLE.setGeometry(QtCore.QRect(200, 690, 91, 20))
        self.rightCurveLE.setText("")
        self.rightCurveLE.setObjectName("rightCurveLE")
        self.label_7 = QtWidgets.QLabel(PropsWin)
        self.label_7.setGeometry(QtCore.QRect(40, 690, 61, 21))
        self.label_7.setObjectName("label_7")
        self.rightCurveCBB = QtWidgets.QComboBox(PropsWin)
        self.rightCurveCBB.setEnabled(True)
        self.rightCurveCBB.setGeometry(QtCore.QRect(100, 690, 91, 22))
        self.rightCurveCBB.setObjectName("rightCurveCBB")
        self.rightCurveCBB.addItem("")
        self.rightCurveCBB.addItem("")
        self.rightCurveCBB.addItem("")
        self.rightCurveCBB.addItem("")
        self.saveProps = QtWidgets.QPushButton(PropsWin)
        self.saveProps.setGeometry(QtCore.QRect(740, 30, 75, 23))
        self.saveProps.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveProps.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saveProps.setObjectName("saveProps")
        self.lansLineAddBT = QtWidgets.QPushButton(PropsWin)
        self.lansLineAddBT.setGeometry(QtCore.QRect(40, 100, 51, 23))
        self.lansLineAddBT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lansLineAddBT.setObjectName("lansLineAddBT")
        self.lansLineDeleteBT = QtWidgets.QPushButton(PropsWin)
        self.lansLineDeleteBT.setGeometry(QtCore.QRect(100, 100, 51, 23))
        self.lansLineDeleteBT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lansLineDeleteBT.setObjectName("lansLineDeleteBT")
        self.markLineAddBT = QtWidgets.QPushButton(PropsWin)
        self.markLineAddBT.setGeometry(QtCore.QRect(310, 100, 51, 23))
        self.markLineAddBT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.markLineAddBT.setObjectName("markLineAddBT")
        self.markLineDeleteBT = QtWidgets.QPushButton(PropsWin)
        self.markLineDeleteBT.setGeometry(QtCore.QRect(370, 100, 51, 23))
        self.markLineDeleteBT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.markLineDeleteBT.setObjectName("markLineDeleteBT")
        self.closeborderAddBT = QtWidgets.QPushButton(PropsWin)
        self.closeborderAddBT.setGeometry(QtCore.QRect(40, 420, 51, 23))
        self.closeborderAddBT.setObjectName("closeborderAddBT")
        self.closeborderDeleteBT = QtWidgets.QPushButton(PropsWin)
        self.closeborderDeleteBT.setGeometry(QtCore.QRect(100, 420, 51, 23))
        self.closeborderDeleteBT.setObjectName("closeborderDeleteBT")
        self.label_8 = QtWidgets.QLabel(PropsWin)
        self.label_8.setGeometry(QtCore.QRect(230, 30, 81, 21))
        self.label_8.setObjectName("label_8")
        self.createMarkLineTableBT = QtWidgets.QPushButton(PropsWin)
        self.createMarkLineTableBT.setGeometry(QtCore.QRect(280, 210, 21, 21))
        self.createMarkLineTableBT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createMarkLineTableBT.setObjectName("createMarkLineTableBT")
        self.hidepavementCBB = QtWidgets.QComboBox(PropsWin)
        self.hidepavementCBB.setEnabled(True)
        self.hidepavementCBB.setGeometry(QtCore.QRect(320, 30, 91, 22))
        self.hidepavementCBB.setObjectName("hidepavementCBB")
        self.hidepavementCBB.addItem("")
        self.hidepavementCBB.addItem("")

        self.retranslateUi(PropsWin)
        QtCore.QMetaObject.connectSlotsByName(PropsWin)

    def retranslateUi(self, PropsWin):
        _translate = QtCore.QCoreApplication.translate
        PropsWin.setWindowTitle(_translate("PropsWin", "属性编辑"))
        self.label_2.setText(_translate("PropsWin", "车道连接定义："))
        item = self.lansLineTable.horizontalHeaderItem(0)
        item.setText(_translate("PropsWin", "开始车道"))
        item = self.lansLineTable.horizontalHeaderItem(1)
        item.setText(_translate("PropsWin", "到达车道"))
        self.label_3.setText(_translate("PropsWin", "S值："))
        self.lanswidthstatCheckBox.setText(_translate("PropsWin", "宽度是否有变化"))
        self.closeborderComboBox.setItemText(0, _translate("PropsWin", "右侧边线 rightcloseborder"))
        self.closeborderComboBox.setItemText(1, _translate("PropsWin", "左侧边线 leftcloseborder"))
        self.label_4.setText(_translate("PropsWin", "道路哪一侧："))
        item = self.markLineTable.horizontalHeaderItem(0)
        item.setText(_translate("PropsWin", "桩号"))
        item = self.markLineTable.horizontalHeaderItem(1)
        item.setText(_translate("PropsWin", "1标线"))
        item = self.markLineTable.horizontalHeaderItem(2)
        item.setText(_translate("PropsWin", "2标线"))
        self.label_5.setText(_translate("PropsWin", "标线定义："))
        item = self.closeborderTable.verticalHeaderItem(0)
        item.setText(_translate("PropsWin", "1"))
        item = self.closeborderTable.verticalHeaderItem(1)
        item.setText(_translate("PropsWin", "2"))
        item = self.closeborderTable.verticalHeaderItem(2)
        item.setText(_translate("PropsWin", "3"))
        item = self.closeborderTable.horizontalHeaderItem(0)
        item.setText(_translate("PropsWin", "桩号"))
        item = self.closeborderTable.horizontalHeaderItem(1)
        item.setText(_translate("PropsWin", "包围类型"))
        item = self.closeborderTable.horizontalHeaderItem(2)
        item.setText(_translate("PropsWin", "包围ID"))
        item = self.closeborderTable.horizontalHeaderItem(3)
        item.setText(_translate("PropsWin", "是否变化宽度"))
        __sortingEnabled = self.closeborderTable.isSortingEnabled()
        self.closeborderTable.setSortingEnabled(False)
        item = self.closeborderTable.item(0, 0)
        item.setText(_translate("PropsWin", "0"))
        item = self.closeborderTable.item(0, 1)
        item.setText(_translate("PropsWin", "无"))
        item = self.closeborderTable.item(0, 2)
        item.setText(_translate("PropsWin", "无"))
        item = self.closeborderTable.item(0, 3)
        item.setText(_translate("PropsWin", "0"))
        item = self.closeborderTable.item(1, 0)
        item.setText(_translate("PropsWin", "8"))
        item = self.closeborderTable.item(1, 1)
        item.setText(_translate("PropsWin", "草地"))
        item = self.closeborderTable.item(1, 2)
        item.setText(_translate("PropsWin", "666"))
        item = self.closeborderTable.item(1, 3)
        item.setText(_translate("PropsWin", "1"))
        item = self.closeborderTable.item(2, 0)
        item.setText(_translate("PropsWin", "20"))
        item = self.closeborderTable.item(2, 1)
        item.setText(_translate("PropsWin", "无"))
        item = self.closeborderTable.item(2, 2)
        item.setText(_translate("PropsWin", "无"))
        item = self.closeborderTable.item(2, 3)
        item.setText(_translate("PropsWin", "0"))
        self.closeborderTable.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("PropsWin", "左侧包围："))
        self.leftCurveCBB.setItemText(0, _translate("PropsWin", "无"))
        self.leftCurveCBB.setItemText(1, _translate("PropsWin", "草地"))
        self.leftCurveCBB.setItemText(2, _translate("PropsWin", "混凝土"))
        self.leftCurveCBB.setItemText(3, _translate("PropsWin", "人行道"))
        self.label_7.setText(_translate("PropsWin", "右侧包围："))
        self.rightCurveCBB.setItemText(0, _translate("PropsWin", "无"))
        self.rightCurveCBB.setItemText(1, _translate("PropsWin", "草地"))
        self.rightCurveCBB.setItemText(2, _translate("PropsWin", "混凝土"))
        self.rightCurveCBB.setItemText(3, _translate("PropsWin", "人行道"))
        self.saveProps.setText(_translate("PropsWin", "保存"))
        self.lansLineAddBT.setText(_translate("PropsWin", "增加行"))
        self.lansLineDeleteBT.setText(_translate("PropsWin", "删除行"))
        self.markLineAddBT.setText(_translate("PropsWin", "增加行"))
        self.markLineDeleteBT.setText(_translate("PropsWin", "删除行"))
        self.closeborderAddBT.setText(_translate("PropsWin", "增加行"))
        self.closeborderDeleteBT.setText(_translate("PropsWin", "删除行"))
        self.label_8.setText(_translate("PropsWin", "是否隐藏道路："))
        self.createMarkLineTableBT.setText(_translate("PropsWin", ">>"))
        self.hidepavementCBB.setItemText(0, _translate("PropsWin", "否"))
        self.hidepavementCBB.setItemText(1, _translate("PropsWin", "是"))
