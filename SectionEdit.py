from PyQt5.QtCore import QRegExp, QRectF, QLineF
from PyQt5.QtGui import QRegExpValidator, QColor
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QCompleter, QGraphicsView, QGraphicsScene, \
    QGraphicsLineItem
from lxml import etree

from DrawSection import MainWindow
from sectionwin import Ui_SectionWind


class SectionEdit(QWidget, Ui_SectionWind):
    # class SectionEdit(QGraphicsView, Ui_SectionWind):

    def __init__(self):
        super(SectionEdit, self).__init__()
        self.setupUi(self)
        parser = etree.XMLParser(remove_blank_text=True)
        xml = etree.parse('yf_sample_data.xml', parser)
        self.root = xml.getroot()  # 获取根节点
        self.list = []
        self.roadidlist = []
        self.initConfig()
        self.initEvent()
        # 画图板
        self.gv = MainWindow(self)
        self.gv.drawSection(self.list)

    def initConfig(self):
        regx = QRegExp("[0-9]+$")
        validator = QRegExpValidator(regx)
        self.sLE.setValidator(validator)
        self.sLE.setPlaceholderText("请输入数字")

        roadList = self.root.xpath('//OpenDriveData/road')
        for rindex in range(0, len(roadList)):
            roadid = roadList[rindex].xpath("@id")[0]
            self.roadidlist.append(roadid)
        self.roadidlist.sort()
        self.roadidCBB.addItems(self.roadidlist)
        self.roadidCBB.setEditable(True)
        self.completerRoadidCBB = QCompleter(self.roadidlist)
        self.roadidCBB.setCompleter(self.completerRoadidCBB)

        self.saveBT.clicked.connect(self.saveEvent)


    def initEvent(self):
        self.readBT.clicked.connect(self.readByRoadId)
        self.addBT.clicked.connect(self.addSectionEvent)
        self.deleteBT.clicked.connect(self.deleteSectionEvent)
        self.rightlansLE.editingFinished.connect(self.rightlansLEEFAction)
        # self.roadidLE.editingFinished.connect(self.readByRoadId)
        self.calculateBT.clicked.connect(self.calculateEvent)

    def showWin(self):
        self.show()

    def readByRoadId(self):
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            xml = etree.parse('yf_sample_data.xml', parser)
            self.root = xml.getroot()  # 获取根节点
            self.list = []
            # self.roadid = self.roadidLE.text().strip() if self.roadidLE.text() != None else ""
            self.roadid = self.roadidCBB.currentText().strip()
            self.sectionList = self.root.xpath(
                '//OpenDriveData/road[@id="' + self.roadid + '"]/lanes/section')

            # 清空表格行
            while self.sectionTable.rowCount() > 0:
                self.sectionTable.removeRow(0)

            for sectionIndex in range(0, len(self.sectionList)):
                # self.sectionTable.insertRow(sectionIndex)
                section = self.sectionList[sectionIndex]
                s = section.xpath("@s")[0]
                leftlans = section.xpath("@leftlans")[0]
                rightlans = section.xpath("@rightlans")[0]
                centermark = section.xpath("@centermark")[0]
                leftmark = section.xpath("@leftmark")[0]
                rightmark = section.xpath("@rightmark")[0]
                leftpre = section.xpath("@leftpre")[0]
                rightpre = section.xpath("@rightpre")[0]
                leftsuc = section.xpath("@leftsuc")[0]
                rightsuc = section.xpath("@rightsuc")[0]

                self.list.append({"s": s, "leftlans": leftlans, "rightlans": rightlans, "centermark": centermark,
                                  "leftmark": leftmark,
                                  "rightmark": rightmark, "leftpre": leftpre, "rightpre": rightpre, "leftsuc": leftsuc,
                                  "rightsuc": rightsuc})

            self.listSort()
            self.initTable()  # 初始化table数据

            # self.sectionTable.setItem(sectionIndex, 0, QTableWidgetItem(s))
            # self.sectionTable.setItem(sectionIndex, 1, QTableWidgetItem(leftlans))
            # self.sectionTable.setItem(sectionIndex, 2, QTableWidgetItem(rightlans))
            # self.sectionTable.setItem(sectionIndex, 3, QTableWidgetItem(centermark))
            # self.sectionTable.setItem(sectionIndex, 4, QTableWidgetItem(leftmark))
            # self.sectionTable.setItem(sectionIndex, 5, QTableWidgetItem(rightmark))
            # self.sectionTable.setItem(sectionIndex, 6, QTableWidgetItem(leftpre))
            # self.sectionTable.setItem(sectionIndex, 7, QTableWidgetItem(rightpre))
            # self.sectionTable.setItem(sectionIndex, 8, QTableWidgetItem(leftsuc))
            # self.sectionTable.setItem(sectionIndex, 9, QTableWidgetItem(rightsuc))

        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", '错误信息：{0}'.format(err), QMessageBox.Yes, QMessageBox.Yes)

    def initTable(self):
        # 清空表格行
        while self.sectionTable.rowCount() > 0:
            self.sectionTable.removeRow(0)
        for index in range(0, len(self.list)):
            self.sectionTable.insertRow(index)
            section = self.list[index]
            s = section.get("s")
            leftlans = section.get("leftlans")
            rightlans = section.get("rightlans")
            centermark = section.get("centermark")
            leftmark = section.get("leftmark")
            rightmark = section.get("rightmark")
            leftpre = section.get("leftpre")
            rightpre = section.get("rightpre")
            leftsuc = section.get("leftsuc")
            rightsuc = section.get("rightsuc")

            self.sectionTable.setItem(index, 0, QTableWidgetItem(str(s)))
            self.sectionTable.setItem(index, 1, QTableWidgetItem(leftlans))
            self.sectionTable.setItem(index, 2, QTableWidgetItem(rightlans))
            self.sectionTable.setItem(index, 3, QTableWidgetItem(centermark))
            self.sectionTable.setItem(index, 4, QTableWidgetItem(leftmark))
            self.sectionTable.setItem(index, 5, QTableWidgetItem(rightmark))
            self.sectionTable.setItem(index, 6, QTableWidgetItem(leftpre))
            self.sectionTable.setItem(index, 7, QTableWidgetItem(rightpre))
            self.sectionTable.setItem(index, 8, QTableWidgetItem(leftsuc))
            self.sectionTable.setItem(index, 9, QTableWidgetItem(rightsuc))

    def getListByTable(self):
        self.list = []
        rows = self.sectionTable.rowCount()
        column = self.sectionTable.columnCount()
        model = self.sectionTable.model()
        for rowIndex in range(0, rows):
            s = model.data(model.index(rowIndex, 0))
            leftlans = model.data(model.index(rowIndex, 1))
            rightlans = model.data(model.index(rowIndex, 2))
            centermark = model.data(model.index(rowIndex, 3))
            leftmark = model.data(model.index(rowIndex, 4))
            rightmark = model.data(model.index(rowIndex, 5))
            leftpre = model.data(model.index(rowIndex, 6))
            rightpre = model.data(model.index(rowIndex, 7))
            leftsuc = model.data(model.index(rowIndex, 8))
            rightsuc = model.data(model.index(rowIndex, 9))
            self.list.append({"s": s, "leftlans": leftlans, "rightlans": rightlans, "centermark": centermark,
                              "leftmark": leftmark,
                              "rightmark": rightmark, "leftpre": leftpre, "rightpre": rightpre, "leftsuc": leftsuc,
                              "rightsuc": rightsuc})

    def listSort(self):
        self.list.sort(key=lambda k: (int(k.get('s', 0))), reverse=False)

    def addSectionEvent(self):
        s = self.sLE.text().strip()
        rightlans = self.rightlansLE.text().strip()
        rightmark = self.rightmarkLE.text().strip()
        centermark = self.centermarkLE.text().strip()

        leftlans = self.leftlansLE.text().strip()
        leftmark = self.leftmarkLE.text().strip()

        if s != "":
            self.list.append(
                {"s": s, "rightlans": rightlans, "rightmark": rightmark, "centermark": centermark, "leftlans": leftlans,
                 "leftmark": leftmark})
            self.listSort()
            self.initTable()

    def deleteSectionEvent(self):
        currentRowIndex = self.sectionTable.currentIndex().row()
        if currentRowIndex == -1:
            QMessageBox.information(self, "温馨提示", "请选择删除记录！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            self.sectionTable.removeRow(currentRowIndex)
            self.list.pop(currentRowIndex)

    def rightlansLEEFAction(self):
        print(self.rightlansLE.text())
        rightlansStr = self.rightlansLE.text()
        rightlansList = rightlansStr.split(";")
        rightmark = ""
        for rindex in range(0, len(rightlansList)):
            rightmark = rightmark + "solid;"
        rightmark = rightmark[0:-1]
        self.rightmarkLE.setText(rightmark)

    def calculateEvent(self):
        self.getListByTable()
        _len = len(self.list)
        if _len > 1:
            self.getRightPreAndSuc()

            # # pre
            # # 处理第一个pre
            # rightlansStr = self.list[0].get("rightlans")
            # rightlansList = rightlansStr.split(";")
            # rightpre = ""
            # _count = 0
            # for ri in range(0, len(rightlansList)):
            #     _count = _count + 1
            #     rightpre = rightpre + "-" + str(_count) + ";"
            # rightpre = rightpre[0:-1]
            # self.list[0]["rightpre"] = rightpre
            #
            # for index in range(1, _len):
            #     preRightlansStr = self.list[index - 1].get("rightlans")
            #     currentRightlansStr = self.list[index].get("rightlans")
            #     rightpre = self.getPre(currentRightlansStr, preRightlansStr, "right")
            #     self.list[index]["rightpre"] = rightpre
            #
            # # suc
            # rightsuc = ""
            # for index in range(1, _len - 1):
            #     sucRightlansStr = self.list[index + 1].get("rightlans")
            #     currentRightlansStr = self.list[index].get("rightlans")
            #     rightsuc = self.getSuc(currentRightlansStr, sucRightlansStr, "right")
            #     self.list[index]["rightsuc"] = rightsuc
            #
            # # 处理第后一个suc
            # rightlansStr = self.list[_len - 1].get("rightlans")
            # rightlansList = rightlansStr.split(";")
            # _count = 0
            # rightsuc = ""
            # for ri in range(0, len(rightlansList)):
            #     _count = _count + 1
            #     rightsuc = rightsuc + "-" + str(_count) + ";"
            # rightsuc = rightsuc[0:-1]
            # self.list[_len - 1]["rightsuc"] = rightsuc

        self.initTable()
        self.gv.drawSection(self.list)

    def getRightPreAndSuc(self):
        _len = len(self.list)
        # pre
        # 处理第一个pre
        rightlansStr = self.list[0].get("rightlans")
        rightlansList = rightlansStr.split(";")
        rightpre = ""
        _count = 0
        for ri in range(0, len(rightlansList)):
            _count = _count + 1
            rightpre = rightpre + "-" + str(_count) + ";"
        rightpre = rightpre[0:-1]
        self.list[0]["rightpre"] = rightpre

        for index in range(1, _len):
            preRightlansStr = self.list[index - 1].get("rightlans")
            currentRightlansStr = self.list[index].get("rightlans")
            rightpre = self.getPre(currentRightlansStr, preRightlansStr, "right")
            self.list[index]["rightpre"] = rightpre

        # suc
        rightsuc = ""
        for index in range(1, _len - 1):
            sucRightlansStr = self.list[index + 1].get("rightlans")
            currentRightlansStr = self.list[index].get("rightlans")
            rightsuc = self.getSuc(currentRightlansStr, sucRightlansStr, "right")
            self.list[index]["rightsuc"] = rightsuc

        # 处理第后一个suc
        rightlansStr = self.list[_len - 1].get("rightlans")
        rightlansList = rightlansStr.split(";")
        _count = 0
        rightsuc = ""
        for ri in range(0, len(rightlansList)):
            _count = _count + 1
            rightsuc = rightsuc + "-" + str(_count) + ";"
        rightsuc = rightsuc[0:-1]
        self.list[_len - 1]["rightsuc"] = rightsuc

    def getPre(self, currentLansStr, preLansStr, type):
        _signType = ""
        if type == "right":
            _signType = "-"

        currentLansList = currentLansStr.split(";")
        preLansList = preLansStr.split(";")
        currentLansLenght = len(currentLansList)
        preLansLenght = len(preLansList)
        templateStr = ""

        for index in range(0, currentLansLenght):
            if currentLansList[index] == "0":
                templateStr = templateStr + "0;"
            else:
                templateStr = templateStr + "#;"

        templateStr = templateStr[0:-1]
        if currentLansLenght > preLansLenght:
            for pindex in range(0, preLansLenght):
                templateStr = templateStr.replace("#", _signType + str(pindex + 1), 1)

            templateStr = templateStr.replace("0", "")
        elif currentLansLenght == preLansLenght:
            templateStr = "";
            for pindex in range(0, preLansLenght):
                templateStr = templateStr + _signType + str(pindex + 1) + ";"
            templateStr = templateStr[0:-1]
        elif currentLansLenght < preLansLenght:
            for pindex in range(0, preLansLenght):
                preLan = preLansList[pindex]
                if preLan == "0":
                    pass
                else:
                    templateStr = templateStr.replace("#", _signType + str(pindex + 1), 1)

        return templateStr

    def getSuc(self, currentLansStr, sucLansStr, type):
        _signType = ""
        if type == "right":
            _signType = "-"
        currentLansList = currentLansStr.split(";")
        sucLansList = sucLansStr.split(";")
        currentLansLenght = len(currentLansList)
        sucLansLenght = len(sucLansList)
        templateStr = ""

        for index in range(0, currentLansLenght):
            if currentLansList[index] == "0":
                templateStr = templateStr + "0;"
            else:
                templateStr = templateStr + "#;"

        templateStr = templateStr[0:-1]

        if currentLansLenght > sucLansLenght:
            for pindex in range(0, sucLansLenght):
                templateStr = templateStr.replace("#", _signType + str(pindex + 1), 1)

            templateStr = templateStr.replace("0", "")
        elif currentLansLenght == sucLansLenght:
            templateStr = "";
            for pindex in range(0, sucLansLenght):
                templateStr = templateStr + _signType + str(pindex + 1) + ";"
            templateStr = templateStr[0:-1]
        elif currentLansLenght < sucLansLenght:
            for pindex in range(0, sucLansLenght):
                preLan = sucLansList[pindex]
                if preLan == "0":
                    pass
                else:
                    templateStr = templateStr.replace("#", _signType + str(pindex + 1), 1)

        return templateStr

    def saveEvent(self):
        self.getListByTable()
        road = self.root.xpath('//OpenDriveData/road[@id="' + self.roadid + '"]')
        lanes = self.root.xpath('//OpenDriveData/road[@id="' + self.roadid + '"]/lanes')

        # 删除lanes节点
        if len(road) > 0 and len(lanes) > 0:
            road[0].remove(lanes[0])

        lanes = etree.SubElement(road[0], 'lanes')
        for index in range(0, len(self.list)):
            item = self.list[index]
            section = etree.SubElement(lanes, 'section')
            s = item.get("s")
            leftlans = item.get("leftlans")
            rightlans = item.get("rightlans")
            centermark = item.get("centermark")
            leftmark = item.get("leftmark")
            rightmark = item.get("rightmark")
            leftpre = item.get("leftpre")
            rightpre = item.get("rightpre")
            leftsuc = item.get("leftsuc")
            rightsuc = item.get("rightsuc")
            section.set("s", str(s))
            section.set("leftlans", leftlans)
            section.set("rightlans", rightlans)
            section.set("centermark", centermark)
            section.set("leftmark", leftmark)
            section.set("rightmark", rightmark)
            section.set("leftpre", leftpre)
            section.set("rightpre", rightpre)
            section.set("leftsuc", leftsuc)
            section.set("rightsuc", rightsuc)

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
            # self.closeWin()
        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", "写入xml失败！错误信息：{0}".format(err), QMessageBox.Yes, QMessageBox.Yes)

