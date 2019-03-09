from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QComboBox, QTableWidgetItem
from lxml import etree

from props import Ui_PropsWin


class LinkProps(QtWidgets.QWidget, Ui_PropsWin):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # 参考博客中建立的是Widget项目，因此哪里导入的是QWidget
    def __init__(self):
        super(LinkProps, self).__init__()
        self.setupUi(self)
        self.lansmarkTypeList = ["none", "solid", "broken"]
        self.initConfig()
        self.setEvent()
        self.initMarkLineTableComboBox()

    def initConfig(self):
        regx = QRegExp("[0-9]+$")
        validator = QRegExpValidator(regx)
        # self.lansNumLineEdit.setValidator(validator)
        self.sNumLineEdit.setValidator(validator)

    def setEvent(self):
        self.lansLineAddBT.clicked.connect(self.lansLineAddEvent)
        self.lansLineDeleteBT.clicked.connect(self.lansLineDeleteEvent)

        self.markLineAddBT.clicked.connect(self.markLineAddEvent)
        self.markLineDeleteBT.clicked.connect(self.markLineDeleteEvent)

        self.saveProps.clicked.connect(self.savePropsEvent)
        self.createMarkLineTableBT.clicked.connect(self.createMarkLineTableEvent)

    def showWin(self, root, junctionID, fromroad, toroad):
        parser = etree.XMLParser(remove_blank_text=True)
        xml = etree.parse('yf_sample_data.xml', parser)
        self.root = xml.getroot()  # 获取根节点
        # self.root = root
        self.junctionID = junctionID
        self.fromroad = fromroad
        self.toroad = toroad
        self.initWind()
        self.show()

    def initWind(self):
        self.link = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.fromroad + self.toroad + '"]')

        self.type = self.link[0].xpath("@type")[0]
        self.id = self.link[0].xpath("@id")[0]
        self.name = self.link[0].xpath("@name")[0]
        self.lansfrom = self.link[0].xpath("@lansfrom")[0]
        self.lansto = self.link[0].xpath("@lansto")[0]
        self.s = self.link[0].xpath("@s")[0]
        self.lansmark = self.link[0].xpath("@lansmark")[0]
        self.hidepavement = self.link[0].xpath("@hidepavement")[0] if len(
            self.link[0].xpath("@hidepavement")) > 0 else ""
        self.leftCurveStr = self.link[0].xpath("@leftcurve")[0] if len(self.link[0].xpath("@leftcurve")) > 0 else ""
        self.rightCurveStr = self.link[0].xpath("@rightcurve")[0] if len(self.link[0].xpath("@rightcurve")) > 0 else ""
        if self.leftCurveStr != "":
            leftCurveList = self.leftCurveStr.split(",")
            self.leftCurveType = leftCurveList[1]
            self.leftCurveId = leftCurveList[0]
        if self.rightCurveStr != "":
            rightCurveList = self.rightCurveStr.split(",")
            self.rightCurveType = rightCurveList[1]
            self.rightCurveId = rightCurveList[0]

        # 初始化
        self.sNumLineEdit.setText(self.s)
        if self.hidepavement == "1":
            self.hidepavementCBB.setCurrentIndex(1)
        else:
            self.hidepavementCBB.setCurrentIndex(0)

        # 车道线定义初始化
        # self.tableRemoveRow(self.lansLineTable, 0, self.lansLineTable.rowCount())
        # self.tableRemoveRow(self.lansLineTable, 0, 1000)

        # for row in range(0, 10000):
        #     self.lansLineTable.removeRow(row)
        # self.lansLineTable.removeRow(0)
        while self.lansLineTable.rowCount() > 0:
            self.lansLineTable.removeRow(0)
        fromroadList = self.lansfrom.split(";")
        toroadList = self.lansto.split(";")
        rowCount = len(fromroadList)
        # rowCount = self.lansLineTable.rowCount()
        for itemRow in range(0, rowCount):
            self.lansLineTable.insertRow(itemRow)
            self.lansLineTable.setItem(itemRow, 0, QTableWidgetItem(fromroadList[itemRow]))
            self.lansLineTable.setItem(itemRow, 1, QTableWidgetItem(toroadList[itemRow]))

        # 标线定义初始化
        # self.tableRemoveRow(self.markLineTable, 0, self.markLineTable.rowCount())
        # self.tableRemoveRow(self.markLineTable, 0, self.markLineTable.rowCount())
        while self.markLineTable.rowCount() > 0:
            self.markLineTable.removeRow(0)
        self.createMarkLineTableEvent()
        lansmarkRows = self.lansmark.split("|")
        for lansmarkRowsIndex in range(0, len(lansmarkRows)):
            lansmarkItem = lansmarkRows[lansmarkRowsIndex]
            lansmarkItemList = lansmarkItem.split(";")

            self.markLineTable.insertRow(lansmarkRowsIndex)
            _tempZH = lansmarkItemList[0].split(",")
            self.markLineTable.setItem(lansmarkRowsIndex, 0, QTableWidgetItem(_tempZH[0]))

            for addMarkColumn in range(0, len(lansmarkItemList)):
                testCBB = QComboBox()
                testCBB.addItems(self.lansmarkTypeList)
                if addMarkColumn == 0:
                    testCBB.setCurrentText(_tempZH[1])
                    # self.markLineTable.setCellWidget(lansmarkRowsIndex, addMarkColumn + 1, testCBB)
                else:
                    testCBB.setCurrentText(lansmarkItemList[addMarkColumn])
                    # self.markLineTable.setCellWidget(lansmarkRowsIndex, addMarkColumn + 1, testCBB)
                self.markLineTable.setCellWidget(lansmarkRowsIndex, addMarkColumn + 1, testCBB)

        # 左右包围
        if self.leftCurveStr != "":
            if self.leftCurveType == "grass":
                self.leftCurveCBB.setCurrentIndex(1)
            elif self.leftCurveType == "spec_concrete_3d":
                self.leftCurveCBB.setCurrentIndex(2)
            elif self.leftCurveType == "pavement":
                self.leftCurveCBB.setCurrentIndex(3)
            self.leftCurveLE.setText(self.leftCurveId)
        else:
            self.leftCurveCBB.setCurrentIndex(0)

        if self.rightCurveStr != "":
            if self.rightCurveType == "grass":
                self.rightCurveCBB.setCurrentIndex(1)
            elif self.rightCurveType == "spec_concrete_3d":
                self.rightCurveCBB.setCurrentIndex(2)
            elif self.rightCurveType == "pavement":
                self.rightCurveCBB.setCurrentIndex(3)
            self.rightCurveLE.setText(self.rightCurveId)
        else:
            self.rightCurveCBB.setCurrentIndex(0)

    def btn_click(self):  # 定义槽函数btn_click(),也可以理解为重载类Ui_MainWindow中的槽函数btn_click()
        self.textEdit.setText("hi,PyQt5~")

    def savePropsEvent(self):
        print("savePropsEvent...")
        # _roadCount = self.lansNumLineEdit.text()
        _s = self.sNumLineEdit.text().strip()
        # _hidepavement = self.hidepavementLineEdit.text().strip()
        _hidepavement = self.hidepavementCBB.currentIndex()

        # 获取车道连接定义
        model = self.lansLineTable.model()
        rowAllCount = self.lansLineTable.rowCount()
        _lansfrom = ""
        _lansto = ""
        for i in range(0, rowAllCount):
            _lansfromIndex = model.index(i, 0)
            _valfrom = model.data(_lansfromIndex)
            if _valfrom == None:
                QMessageBox.information(self, "温馨提示", "车道连接定义不能为空！", QMessageBox.Yes, QMessageBox.Yes)
                return
            else:
                _lansfrom = _lansfrom + _valfrom.strip() + ";"
            # _lansfrom = _lansfrom + model.data(_lansfromIndex) + ";"

            _lanstoIndex = model.index(i, 1)
            _valto = model.data(_lanstoIndex)
            if _valto == None:
                QMessageBox.information(self, "温馨提示", "车道连接定义不能为空！", QMessageBox.Yes, QMessageBox.Yes)
                return
            else:
                _lansto = _lansto + _valto.strip() + ";"

        _lansfrom = _lansfrom[0:-1]
        _lansto = _lansto[0:-1]

        # 获取标线定义数据
        markLineModel = self.markLineTable.model()
        markRowAllCount = self.markLineTable.rowCount()
        markColumnAllCount = self.markLineTable.columnCount()

        if rowAllCount != (markColumnAllCount - 2):
            QMessageBox.information(self, "温馨提示", "车道连接定义和标线定义不一致！", QMessageBox.Yes, QMessageBox.Yes)
            return

        _lansmark = ""
        for m in range(0, markRowAllCount):
            _markColumn0 = markLineModel.data(markLineModel.index(m, 0))
            if _markColumn0 == None or _markColumn0.strip() == "":
                QMessageBox.information(self, "温馨提示", "标线定义桩号不能为空！", QMessageBox.Yes, QMessageBox.Yes)
                return
            _lansmark = _lansmark + _markColumn0 + ","
            for n in range(1, markColumnAllCount):
                # _val = markLineModel.data(markLineModel.index(m, n))
                _val = self.markLineTable.cellWidget(m, n).currentText()
                if _val == None or _val == "":
                    _lansmark = _lansmark + "none" + ";"
                else:
                    _lansmark = _lansmark + _val.strip() + ";"
            _lansmark = _lansmark[0:-1] + "|"
        _lansmark = _lansmark[0:-1]

        print(_s, _hidepavement)
        print(_lansfrom, _lansto)
        print(_lansmark)
        _leftCurveCBB = self.leftCurveCBB.currentIndex()
        _rightCurveCBB = self.rightCurveCBB.currentIndex()

        # _currentIndex = common.tableWidget.currentIndex().row()
        # _currentIntem = common.list[_currentIndex]
        _currentIntem = {}
        _currentIntem["s"] = _s
        if _hidepavement == 0:
            _currentIntem["hidepavement"] = ""
        else:
            _currentIntem["hidepavement"] = "1"
        _currentIntem["lansfrom"] = _lansfrom
        _currentIntem["lansto"] = _lansto
        _currentIntem["lansmark"] = _lansmark

        _leftCurveLE = self.leftCurveLE.text().strip()
        _rightCurveLE = self.rightCurveLE.text().strip()

        if _leftCurveCBB == 0:
            _leftCurveCBB = ""
        elif _leftCurveCBB == 1:
            _leftCurveCBB = "grass"
        elif _leftCurveCBB == 2:
            _leftCurveCBB = "spec_concrete_3d"
        elif _leftCurveCBB == 3:
            _leftCurveCBB = "pavement"

        if _rightCurveCBB == 0:
            _rightCurveCBB = ""
        elif _rightCurveCBB == 1:
            _rightCurveCBB = "grass"
        elif _rightCurveCBB == 2:
            _rightCurveCBB = "spec_concrete_3d"
        elif _rightCurveCBB == 3:
            _rightCurveCBB = "pavement"

        if _leftCurveCBB != "" and _leftCurveLE == "":
            QMessageBox.information(self, "温馨提示", "左侧包围值不能为空！", QMessageBox.Yes, QMessageBox.Yes)
            return
        if _rightCurveCBB != "" and _rightCurveLE == "":
            QMessageBox.information(self, "温馨提示", "右侧包围值不能为空！", QMessageBox.Yes, QMessageBox.Yes)
            return
        if _leftCurveCBB != "":
            _currentIntem["leftCurve"] = _leftCurveLE + "," + _leftCurveCBB
        if _rightCurveCBB != "":
            _currentIntem["rightCurve"] = _rightCurveLE + "," + _rightCurveCBB

        # common.list[_currentIndex] = _currentIntem

        # junction = etree.SubElement(self.root, 'junction', attrib={"id": self.junctionID})
        # links = etree.SubElement(junction, "links")
        # link = etree.SubElement(links, "link")
        #
        # link.set("type", type)
        # link.set("fromroad", fromroad)
        # link.set("toroad", toroad)
        # link.set("id", id)
        #
        # objects = etree.SubElement(link, "objects")
        # signals = etree.SubElement(link, "signals")
        # links = self.root.xpath('//OpenDriveData/junction[@id="' + self.junctionID + '"]/links')
        # link = etree.SubElement(links, 'link', attrib={"id": self.fromroad + self.toroad})
        link = self.root.xpath(
            '//OpenDriveData/junction[@id="' + self.junctionID + '"]/links/link[@id="' + self.fromroad + self.toroad + '"]')
        attrib = link[0].attrib
        attrib["s"] = _currentIntem["s"]
        attrib["hidepavement"] = _currentIntem["hidepavement"]
        attrib["lansfrom"] = _currentIntem["lansfrom"]
        attrib["lansto"] = _currentIntem["lansto"]
        attrib["lansmark"] = _currentIntem["lansmark"]
        if "leftCurve" in _currentIntem:
            attrib["leftcurve"] = _currentIntem["leftCurve"]
        else:
            if "leftcurve" in attrib:
                del attrib["leftcurve"]
        if "rightCurve" in _currentIntem:
            attrib["rightcurve"] = _currentIntem["rightCurve"]
        else:
            if "rightcurve" in attrib:
                del attrib["rightcurve"]

        try:
            # 节点转为tree对象
            tree = etree.ElementTree(self.root)
            '''
            各个参数含义如下：
            1）第1个参数是xml的完整路径(包括文件名)；
            2）pretty_print参数是否美化代码；
            3）xml_declaration参数是否写入xml声明，就是我们看到xml文档第1行文字；
            4）encoding参数很明显是保存的编码。
            '''
            tree.write('yf_sample_data.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
            print('写入xml OK!')
            QMessageBox.information(self, "温馨提示", "写入xml成功！", QMessageBox.Yes, QMessageBox.Yes)
            self.closeWin()
        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", "写入xml失败！", QMessageBox.Yes, QMessageBox.Yes)

        # self.closeWin()

    def lansLineAddEvent(self):
        rowCount = self.lansLineTable.rowCount()
        self.lansLineTable.insertRow(rowCount)

    def lansLineDeleteEvent(self):
        currentRowIndex = self.lansLineTable.currentIndex().row()
        self.lansLineTable.removeRow(currentRowIndex)

    def markLineAddEvent(self):
        rowCount = self.markLineTable.rowCount()
        self.markLineTable.insertRow(rowCount)
        for addMarkColumn in range(1, self.markLineTable.columnCount()):
            testCBB = QComboBox()
            testCBB.addItems(self.lansmarkTypeList)
            self.markLineTable.setCellWidget(rowCount, addMarkColumn, testCBB)

    def markLineDeleteEvent(self):
        currentRowIndex = self.markLineTable.currentIndex().row()
        self.markLineTable.removeRow(currentRowIndex)

    def createMarkLineTableEvent(self):
        roadNum = self.lansLineTable.rowCount()
        columnList = ["桩号", "1标线", "2标线"]
        markColumnCount = self.markLineTable.columnCount()
        # self.markLineTable.setRowCount(2)
        self.markLineTable.setColumnCount(3)
        if roadNum > 1:
            for column in range(3, roadNum + 2):
                self.markLineTable.insertColumn(column)
                self.markLineTable.setColumnCount(column + 1)
                columnList.append(str(column) + "标线")
            self.markLineTable.setHorizontalHeaderLabels(columnList)

        # testList = ["solid", "broken", "none"]
        # testCBB = QComboBox()
        # testCBB.addItems(testList)
        # self.markLineTable.setCellWidget(1, 2, testCBB)
        self.initMarkLineTableComboBox()

    # 初始化下拉列表
    def initMarkLineTableComboBox(self):
        _currColumn = self.markLineTable.columnCount()
        _currRow = self.markLineTable.rowCount()
        for markLineRow in range(0, _currRow):
            for markLineColumn in range(1, _currColumn):
                self.lansmarkTypeList = ["none", "solid", "broken"]
                testCBB = QComboBox()
                testCBB.addItems(self.lansmarkTypeList)
                self.markLineTable.setCellWidget(markLineRow, markLineColumn, testCBB)

    def closeWin(self):
        self.close()

    def tableRemoveRow(self, table, start, end):
        for row in range(start, end):
            table.removeRow(row)
