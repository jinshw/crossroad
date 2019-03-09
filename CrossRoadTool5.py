import sys
import uuid
import xml.dom.minidom

from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QMessageBox, QLabel, QCompleter, QColorDialog, \
    QTableWidget, QTableWidgetItem, QPushButton, QRadioButton, \
    QButtonGroup, QLineEdit, QGroupBox, QFormLayout, QVBoxLayout, QHBoxLayout, QAbstractItemView
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QCursor, QPixmap, QColor
from PyQt5.QtCore import Qt, QSize, QPoint
from lxml import etree

from SectionEdit import SectionEdit
from SignalEdit import SignalEdit
from CrossPaintBoard import CrossPaintBoard
from LinkProps import LinkProps
import common


class CrossRoadTool(QWidget):
    def __init__(self):
        super().__init__()
        self.items_list = []
        self.road_list = {}
        common.list = common.list
        self.linkPropsWin = LinkProps()
        self.signalEditWin = SignalEdit()
        self.sectionWin = SectionEdit()
        self.readXML()
        self.initUI()
        # self.initTableDatas()

    def initUI(self):
        self.setGeometry(50, 50, 1500, 800)
        self.__paintBoard = CrossPaintBoard(self)
        self.__paintBoard.move(300, 50)
        # self.showMaximized()
        self.setWindowTitle("交通路口处理工具")
        self.initComboBox()
        self.initTableWidget()
        self.initButton()
        self.initQRadioButton()
        self.initRoadLine()

        self.show()

    # 初始化下拉选择框
    def initComboBox(self):
        self.comboLeftOne = QComboBox(self)
        self.comboLeftTwo = QComboBox(self)
        self.comboRightOne = QComboBox(self)
        self.comboRightTwo = QComboBox(self)
        self.comboTopOne = QComboBox(self)
        self.comboTopTwo = QComboBox(self)
        self.comboBottomOne = QComboBox(self)
        self.comboBottomTwo = QComboBox(self)

        self.comboLeftOne.setEditable(True)
        self.comboLeftTwo.setEditable(True)
        self.comboRightOne.setEditable(True)
        self.comboRightTwo.setEditable(True)
        self.comboTopOne.setEditable(True)
        self.comboTopTwo.setEditable(True)
        self.comboBottomOne.setEditable(True)
        self.comboBottomTwo.setEditable(True)

        self.comboLeftOne.addItems(self.items_list)
        self.comboLeftTwo.addItems(self.items_list)
        self.comboRightOne.addItems(self.items_list)
        self.comboRightTwo.addItems(self.items_list)
        self.comboTopOne.addItems(self.items_list)
        self.comboTopTwo.addItems(self.items_list)
        self.comboBottomOne.addItems(self.items_list)
        self.comboBottomTwo.addItems(self.items_list)

        # 增加自动补全
        self.completerLeftOne = QCompleter(self.items_list)
        self.completerLeftTwo = QCompleter(self.items_list)
        self.completerRightOne = QCompleter(self.items_list)
        self.completerRightTwo = QCompleter(self.items_list)
        self.completerTopOne = QCompleter(self.items_list)
        self.completerTopTwo = QCompleter(self.items_list)
        self.completerBottomOne = QCompleter(self.items_list)
        self.completerBottomTwo = QCompleter(self.items_list)

        self.comboLeftOne.setCompleter(self.completerLeftOne)
        self.comboLeftTwo.setCompleter(self.completerLeftTwo)
        self.comboRightOne.setCompleter(self.completerRightOne)
        self.comboRightTwo.setCompleter(self.completerRightTwo)
        self.comboTopOne.setCompleter(self.completerTopOne)
        self.comboTopTwo.setCompleter(self.completerTopTwo)
        self.comboBottomOne.setCompleter(self.completerBottomOne)
        self.comboBottomTwo.setCompleter(self.completerBottomTwo)

        # ComboBox 设置的位置
        self.comboLeftOne.move(200, 190)
        self.comboLeftTwo.move(200, 290)
        self.comboRightOne.move(730, 190)
        self.comboRightTwo.move(730, 290)
        self.comboTopOne.move(420, 20)
        self.comboTopTwo.move(520, 20)
        self.comboBottomOne.move(420, 500)
        self.comboBottomTwo.move(520, 500)

    def initButton(self):
        self.createButton = QPushButton(self)
        self.createButton.setText("生成")
        self.createButton.clicked.connect(self.createContent)
        self.createButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createButton.move(900, 650)

        self.saveButton = QPushButton(self)
        self.saveButton.setText("保存")
        self.saveButton.setShortcut('Ctrl+S')  # shortcut key
        self.saveButton.clicked.connect(self.saveContextToXML)
        self.saveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveButton.move(1000, 650)

        self.clearButton = QPushButton(self)
        self.clearButton.setText("清除")
        self.clearButton.clicked.connect(self.clearEvent)
        self.clearButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearButton.move(1100, 650)

        self.readProsBT = QPushButton(self)
        self.readProsBT.setText("读取列表")
        self.readProsBT.move(1200, 650)
        self.readProsBT.clicked.connect(self.readPropsListEvent)
        self.readProsBT.setCursor(QCursor(Qt.PointingHandCursor))

        self.editProsBT = QPushButton(self)
        self.editProsBT.setText("编辑属性")
        self.editProsBT.move(1300, 650)
        self.editProsBT.clicked.connect(self.openPropsWinEvent)
        self.editProsBT.setCursor(QCursor(Qt.PointingHandCursor))

        self.openSignalBT = QPushButton(self)
        self.openSignalBT.setText("信号灯编辑")
        self.openSignalBT.clicked.connect(self.openSignalEditEvent)
        self.openSignalBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.openSignalBT.move(900, 700)

        self.sectionEditBT = QPushButton(self)
        self.sectionEditBT.setText("Section编辑")
        self.sectionEditBT.move(1000, 700)
        self.sectionEditBT.clicked.connect(self.openSectionWinEvent)
        self.sectionEditBT.setCursor(QCursor(Qt.PointingHandCursor))

    def initQRadioButton(self):
        self.rbCrossType = QRadioButton("十字型路口", self)
        self.rbTType = QRadioButton("T字型路口", self)
        self.rbStraightType = QRadioButton("直型路口", self)
        self.rbTurnType = QRadioButton("拐字型路口", self)
        self.rbStraightType.setChecked(True)  # 默认选中

        self.lbID = QLabel("ID:", self)
        self.inputID = QLineEdit(self)
        self.lbID.move(680, 605)
        self.inputID.move(700, 600)

        self.bg = QButtonGroup(self)
        self.bg.addButton(self.rbCrossType, 1)
        self.bg.addButton(self.rbTType, 2)
        self.bg.addButton(self.rbStraightType, 3)
        self.bg.addButton(self.rbTurnType, 4)
        self.bg.buttonClicked.connect(self.rbclicked)
        self.rbCrossType.move(500, 650)
        self.rbTType.move(600, 650)
        self.rbStraightType.move(700, 650)
        self.rbTurnType.move(800, 650)

    def rbclicked(self):
        if self.bg.checkedId() == 1:  # 十字路口
            print("十字路口...")
            self.comboLeftOne.setVisible(True)
            self.comboLeftTwo.setVisible(True)
            self.comboRightOne.setVisible(True)
            self.comboRightTwo.setVisible(True)
            self.comboTopOne.setVisible(True)
            self.comboTopTwo.setVisible(True)
            self.comboBottomOne.setVisible(True)
            self.comboBottomTwo.setVisible(True)
        elif self.bg.checkedId() == 2:  # 丁字路口
            print("丁字路口...")
            self.comboLeftOne.setVisible(True)
            self.comboLeftTwo.setVisible(True)
            self.comboRightOne.setVisible(True)
            self.comboRightTwo.setVisible(True)
            self.comboTopOne.setVisible(True)
            self.comboTopTwo.setVisible(True)
            self.comboBottomOne.setVisible(False)
            self.comboBottomTwo.setVisible(False)
        elif self.bg.checkedId() == 3:  # 直型路口
            self.comboLeftOne.setVisible(True)
            self.comboLeftTwo.setVisible(True)
            self.comboRightOne.setVisible(True)
            self.comboRightTwo.setVisible(True)
            self.comboTopOne.setVisible(False)
            self.comboTopTwo.setVisible(False)
            self.comboBottomOne.setVisible(False)
            self.comboBottomTwo.setVisible(False)
        elif self.bg.checkedId() == 4:  # 拐字型路口
            self.comboLeftOne.setVisible(False)
            self.comboLeftTwo.setVisible(False)
            self.comboRightOne.setVisible(True)
            self.comboRightTwo.setVisible(True)
            self.comboTopOne.setVisible(True)
            self.comboTopTwo.setVisible(True)
            self.comboBottomOne.setVisible(False)
            self.comboBottomTwo.setVisible(False)

    # Override
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        # self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        # 左
        qp.drawLine(300, 200, 400, 200)
        qp.drawLine(300, 300, 400, 300)
        # 右
        qp.drawLine(600, 200, 700, 200)
        qp.drawLine(600, 300, 700, 300)
        # 上
        qp.drawLine(450, 150, 450, 50)
        qp.drawLine(550, 150, 550, 50)
        # 下
        qp.drawLine(450, 350, 450, 450)
        qp.drawLine(550, 350, 550, 450)

        # qp.drawArc(400, 200, 450, 350, 30 * 16, 120 * 16)

        path = QPainterPath()
        path.moveTo(400, 200)
        # 使用cubicTo() 方法生成，分别需要三个点：起始点，控制点和终止点

        # qp.setPen(Qt.red)
        # # self.area.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        # self.update()

        # 直行
        qp.setPen(Qt.green)
        qp.drawLine(600, 200, 400, 200)  # 右1--左1
        qp.drawLine(400, 300, 600, 300)  # 左2--右2
        qp.drawLine(450, 150, 450, 350)  # 上1 -- 下1
        qp.drawLine(550, 350, 550, 150)  # 下2 -- 上2

        # 左行
        qp.setPen(Qt.blue)
        qp.drawLine(400, 300, 550, 150)  # 左2 -- 上2
        qp.drawLine(600, 200, 450, 350)  # 右1 -- 下1
        qp.drawLine(450, 150, 600, 300)  # 上1 -- 右1
        qp.drawLine(550, 350, 400, 200)  # 下2 -- 左1

        # 右行
        qp.setPen(Qt.red)
        qp.drawLine(400, 300, 450, 350)  # 左2 -- 下1
        qp.drawLine(600, 200, 550, 150)  # 右1 -- 上2
        qp.drawLine(450, 150, 400, 200)  # 上1 -- 左1
        qp.drawLine(550, 350, 600, 300)  # 下2 -- 右2

        # 贝塞尔曲线
        # qp.setPen(Qt.red)
        # path.cubicTo(400, 200, 450, 250, 450, 350)

        qp.drawPath(path)
        # pen.setStyle(Qt.DashLine)
        # qp.setPen(pen)
        # qp.drawLine(20, 80, 250, 80)

        # pen.setStyle(Qt.DashDotLine)
        # qp.setPen(pen)
        # qp.drawLine(20, 120, 250, 120)
        #
        # pen.setStyle(Qt.DotLine)
        # qp.setPen(pen)
        # qp.drawLine(20, 160, 250, 160)
        #
        # pen.setStyle(Qt.DashDotDotLine)
        # qp.setPen(pen)
        # qp.drawLine(20, 200, 250, 200)
        #
        # pen.setStyle(Qt.CustomDashLine)
        # pen.setDashPattern([1, 4, 5, 4])
        # qp.setPen(pen)
        # qp.drawLine(20, 240, 250, 240)

    def initTableWidget(self):
        common.tableWidget = QTableWidget(self)
        common.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        common.tableWidget.setColumnCount(3)
        common.tableWidget.setRowCount(18)
        common.tableWidget.move(900, 100)
        common.tableWidget.setFixedHeight(500)
        common.tableWidget.setFixedWidth(500)
        common.tableWidget.setHorizontalHeaderLabels(["从ID路", "到ID路", "类型"])

    def initTableDatas(self):
        common.tableWidget.clearContents()
        for i in range(len(common.list)):
            common.tableWidget.setItem(i, 0, QTableWidgetItem(common.list[i].get("fromroad")))
            common.tableWidget.setItem(i, 1, QTableWidgetItem(common.list[i].get("toroad")))
            if common.list[i].get("type") == "st":
                common.tableWidget.setItem(i, 2, QTableWidgetItem("直行"))
            elif common.list[i].get("type") == "lt":
                common.tableWidget.setItem(i, 2, QTableWidgetItem("左行"))
            elif common.list[i].get("type") == "rt":
                common.tableWidget.setItem(i, 2, QTableWidgetItem("右行"))
            elif common.list[i].get("type") == "ut":
                common.tableWidget.setItem(i, 2, QTableWidgetItem("掉头"))

    def readXML(self):
        print("start read xml...")
        # 打开xml文档
        '''
        必须在解析的时候添加
        remove_blank_text=True
        这样的话 pretty_print=True 才会真正有效
        '''
        parser = etree.XMLParser(remove_blank_text=True)
        xml = etree.parse('yf_sample_data.xml', parser)
        self.root = xml.getroot()  # 获取根节点
        # self.removeNodes("junction")  # 清除所有junction节点
        itemlist = self.root.xpath('//OpenDriveData/road/@id')
        for id in itemlist:
            # id = item.getAttribute("id")
            if not id:
                print("id is null")
            else:
                self.items_list.append(id)
                # roadSections = self.root.xpath('//OpenDriveData/road[@id="' + id + '"]/lanes/section')
                #
                # self.road_list[id] = {"id": id, "roadNum": 6}
        self.items_list.sort()

    # 保存数据到XML
    def saveContextToXML(self):
        print("saveContextToXML start...")

        if len(common.list) == 0:
            QMessageBox.information(self, "温馨提示", "请先生成数据！", QMessageBox.Yes, QMessageBox.Yes)
            return
        print("junction id:" + self.inputID.text().strip())

        junctionID = self.inputID.text().strip()

        if junctionID == "":
            print("junction id is null")
            QMessageBox.information(self, "温馨提示", "ID不能为空，请输入！", QMessageBox.Yes, QMessageBox.Yes)
            return

        currentJunctionIds = self.root.xpath('//OpenDriveData/junction[@id="' + junctionID + '"]')
        if len(currentJunctionIds) > 0:
            print("当前的ID已经存在，请更换一个ID！")
            reply = QMessageBox.information(self, "温馨提示", "当前的ID已经存在，是否替换！", QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.removeNodes("junction", junctionID)
            else:
                return

        # 用DOM对象创建元素子节点
        # junction = etree.SubElement(self.root, 'junction', attrib={'id': '222', "name": "333"})
        junction = etree.SubElement(self.root, 'junction', attrib={"id": junctionID})
        links = etree.SubElement(junction, "links")

        for i in range(len(common.list)):
            id = common.list[i].get("fromroad") + common.list[i].get("toroad")
            type = common.list[i].get("type")
            fromroad = common.list[i].get("fromroad")
            toroad = common.list[i].get("toroad")

            roadNums = self.getRoadNum(common.list[i])
            lansfrom = ""
            lansto = ""
            if type == "st":
                _fromRoadNum = roadNums["fromRoadNum"]
                _toRoadNum = roadNums["toRoadNum"]
                _roadNumMin = min(_fromRoadNum, _toRoadNum)
                if _roadNumMin <= 2:
                    lansfrom = "-1;-2"
                    lansto = "-1;-2"
                else:
                    for _indexNum in range(2, _roadNumMin):
                        lansfrom = lansfrom + "-" + str(_indexNum) + ";"
                        lansto = lansto + "-" + str(_indexNum) + ";"
                    lansfrom = lansfrom[0:-1]
                    lansto = lansto[0:-1]
            elif type == "lt":
                lansfrom = "-1"
                lansto = "-1"
            elif type == 'rt':
                lansfrom = "-" + str(roadNums["fromRoadNum"])
                lansto = "-" + str(roadNums["toRoadNum"])
            elif type == 'ut':
                lansfrom = "-1"
                lansto = "-1"

            # link = etree.SubElement(links, "link",
            #                         attrib={"type": type, "fromroad": fromroad, "toroad": toroad, "id": id,
            #                                 "name": "", "lansfrom": "-1", "lansto": "-1", "s": "0",
            #                                 "lansmark": "0,solid;solid", "hidepavement": ""
            #                                 })
            link = etree.SubElement(links, "link")
            # 使用set方法添加属性，属性值不排序，而etree.SubElement(links, "link", attrib={})设置，属性值导出时是有序的
            link.set("type", type)
            link.set("fromroad", fromroad)
            link.set("toroad", toroad)
            link.set("id", id)

            fromroadName = self.root.xpath('//OpenDriveData/road[@id="' + fromroad + '"]/@name')[0]
            toroadName = self.root.xpath('//OpenDriveData/road[@id="' + fromroad + '"]/@name')[0]
            _name = type + "_" + fromroadName + "_" + toroadName
            link.set("name", _name)
            link.set("lansfrom", lansfrom)
            link.set("lansto", lansto)
            link.set("s", "0")

            _lansmark = "0,"
            for k in range(0, len(lansfrom.split(";")) + 1):
                _lansmark = _lansmark + "solid;"
            _lansmark = _lansmark[0:-1]
            link.set("lansmark", _lansmark)

            link.set("hidepavement", "")

            # 判断是否编辑了属性
            if "lansfrom" in common.list[i]:
                link.set("lansfrom", common.list[i]["lansfrom"])
            if "lansto" in common.list[i]:
                link.set("lansto", common.list[i]["lansto"])
            if "lansmark" in common.list[i]:
                link.set("lansmark", common.list[i]["lansmark"])
            if "hidepavement" in common.list[i]:
                link.set("hidepavement", common.list[i]["hidepavement"])
            if "s" in common.list[i]:
                link.set("s", common.list[i]["s"])

            if "leftCurve" in common.list[i]:
                link.set("leftCurve", common.list[i]["leftCurve"])
            if "rightCurve" in common.list[i]:
                link.set("rightCurve", common.list[i]["rightCurve"])

            objects = etree.SubElement(link, "objects")
            signals = etree.SubElement(link, "signals")
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
            self.clearEvent()

        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", "写入xml失败！", QMessageBox.Yes, QMessageBox.Yes)

    # 删除指定节点
    def removeNodes(self, nodeName, id=""):
        if id == "":
            junctionOlds = self.root.xpath("//OpenDriveData/" + nodeName)
        else:
            junctionOlds = self.root.xpath("//OpenDriveData/" + nodeName + "[@id='" + id + "']")
        for node in junctionOlds:
            self.root.remove(node)

    # 清除数据
    def clearEvent(self):
        print("clear ...")
        common.list = []
        common.tableWidget.clearContents()

        self.__paintBoard.clearBoard()
        self.initRoadLine()

    def getComboBoxIds(self):
        self.leftOneId = self.comboLeftOne.currentText()
        self.leftTwoId = self.comboLeftTwo.currentText()
        self.rightOneId = self.comboRightOne.currentText()
        self.rightTwoId = self.comboRightTwo.currentText()
        self.topOneId = self.comboTopOne.currentText()
        self.topTwoId = self.comboTopTwo.currentText()
        self.bottomOneId = self.comboBottomOne.currentText()
        self.bottomTwoId = self.comboBottomTwo.currentText()

    def generatedCrossData(self):
        #### 直行#####
        # 左2--右2
        common.list.append({"type": "st", "fromroad": self.leftTwoId, "toroad": self.rightTwoId})
        # 右1--左1
        common.list.append({"type": "st", "fromroad": self.rightOneId, "toroad": self.leftOneId})
        # 上1--下1
        common.list.append({"type": "st", "fromroad": self.topOneId, "toroad": self.bottomOneId})
        # 下2--上2
        common.list.append({"type": "st", "fromroad": self.bottomTwoId, "toroad": self.topTwoId})

        #### 左行#####
        # 左2--上2
        common.list.append({"type": "lt", "fromroad": self.leftTwoId, "toroad": self.topTwoId})
        # 右1--下1
        common.list.append({"type": "lt", "fromroad": self.rightOneId, "toroad": self.bottomOneId})
        # 上1--右2
        common.list.append({"type": "lt", "fromroad": self.topOneId, "toroad": self.rightTwoId})
        # 下2--左1
        common.list.append({"type": "lt", "fromroad": self.bottomTwoId, "toroad": self.leftOneId})

        #### 右行#####
        # 左2--下1
        common.list.append({"type": "rt", "fromroad": self.leftTwoId, "toroad": self.bottomOneId})
        # 右1--上2
        common.list.append({"type": "rt", "fromroad": self.rightOneId, "toroad": self.topTwoId})
        # 上1--左1
        common.list.append({"type": "rt", "fromroad": self.topOneId, "toroad": self.leftOneId})
        # 下2--右2
        common.list.append({"type": "rt", "fromroad": self.bottomTwoId, "toroad": self.rightTwoId})

        #### 掉头#####
        # 左2--左1
        common.list.append({"type": "ut", "fromroad": self.leftTwoId, "toroad": self.leftOneId})
        # 右1--右2
        common.list.append({"type": "ut", "fromroad": self.rightOneId, "toroad": self.rightTwoId})
        # 上1--上2
        common.list.append({"type": "ut", "fromroad": self.topOneId, "toroad": self.topTwoId})
        # 下2--下1
        common.list.append({"type": "ut", "fromroad": self.bottomTwoId, "toroad": self.bottomOneId})
        # 连线
        self.initCrossConnectLine()

    # T型路口（没有下边路）
    def generatedTData(self):
        #### 直行#####
        # 左2--右2
        common.list.append({"type": "st", "fromroad": self.leftTwoId, "toroad": self.rightTwoId})
        # 右1--左1
        common.list.append({"type": "st", "fromroad": self.rightOneId, "toroad": self.leftOneId})

        #### 左行#####
        # 左2--上2
        common.list.append({"type": "lt", "fromroad": self.leftTwoId, "toroad": self.topTwoId})
        # 上1--右2
        common.list.append({"type": "lt", "fromroad": self.topOneId, "toroad": self.rightTwoId})

        #### 右行#####
        # 右1--上2
        common.list.append({"type": "rt", "fromroad": self.rightOneId, "toroad": self.topTwoId})
        # 上1--左1
        common.list.append({"type": "rt", "fromroad": self.topOneId, "toroad": self.leftOneId})

        #### 掉头#####
        # 左2--左1
        common.list.append({"type": "ut", "fromroad": self.leftTwoId, "toroad": self.leftOneId})
        # 右1--右2
        common.list.append({"type": "ut", "fromroad": self.rightOneId, "toroad": self.rightTwoId})
        # 上1--上2
        common.list.append({"type": "ut", "fromroad": self.topOneId, "toroad": self.topTwoId})
        self.initTConnectLine()

    # 直行路口（只有左右路的直行和掉头）
    def generatedStraightData(self):
        #### 直行#####
        # 左2--右2
        common.list.append({"type": "st", "fromroad": self.leftTwoId, "toroad": self.rightTwoId})
        # 右1--左1
        common.list.append({"type": "st", "fromroad": self.rightOneId, "toroad": self.leftOneId})

        #### 掉头#####
        # 左2--左1
        common.list.append({"type": "ut", "fromroad": self.leftTwoId, "toroad": self.leftOneId})
        # 右1--右2
        common.list.append({"type": "ut", "fromroad": self.rightOneId, "toroad": self.rightTwoId})
        # 连线
        self.initCrossConnectLine()

    # 拐字型路口（只有右和上路）
    def generatedTurnData(self):
        #### 左行#####
        # 上1--右2
        common.list.append({"type": "lt", "fromroad": self.topOneId, "toroad": self.rightTwoId})

        #### 右行#####
        # 右1--上2
        common.list.append({"type": "rt", "fromroad": self.rightOneId, "toroad": self.topTwoId})

        #### 掉头#####
        # 右1--右2
        common.list.append({"type": "ut", "fromroad": self.rightOneId, "toroad": self.rightTwoId})
        # 上1--上2
        common.list.append({"type": "ut", "fromroad": self.topOneId, "toroad": self.topTwoId})
        # 连线
        self.initCrossConnectLine()

    # 生成数据
    def createContent(self):
        print("createContent...")
        common.list = []
        self.getComboBoxIds()
        if self.bg.checkedId() == 1:  # 十字路口
            self.generatedCrossData()
        elif self.bg.checkedId() == 2:  # 丁字路口
            self.generatedTData()
        elif self.bg.checkedId() == 3:  # 直行路口
            self.generatedStraightData()
        elif self.bg.checkedId() == 4:  # 拐字型路口
            self.generatedTurnData()
        # 初始化表格数据
        self.initTableDatas()

    def getUUID(self):
        uid = str(uuid.uuid4())
        suid = ''.join(uid.split('-'))
        return suid

    def initRoadLine(self):

        # self.__paintBoard.move(1400, 100)

        self.__paintBoard.setPen(QColor("black"), 8)
        # 左
        self.__paintBoard.drawLine(QPoint(0, 150), QPoint(100, 150))
        self.__paintBoard.drawLine(QPoint(0, 250), QPoint(100, 250))
        # 右
        self.__paintBoard.drawLine(QPoint(300, 150), QPoint(400, 150))
        self.__paintBoard.drawLine(QPoint(300, 250), QPoint(400, 250))
        # 上
        self.__paintBoard.drawLine(QPoint(150, 100), QPoint(150, 0))
        self.__paintBoard.drawLine(QPoint(250, 100), QPoint(250, 0))
        # 下
        self.__paintBoard.drawLine(QPoint(150, 300), QPoint(150, 400))
        self.__paintBoard.drawLine(QPoint(250, 300), QPoint(250, 400))

        # 设置道路放像
        self.__paintBoard.drawLine(QPoint(350, 150), QPoint(360, 140))
        self.__paintBoard.drawLine(QPoint(350, 150), QPoint(360, 160))

    def initCrossConnectLine(self):
        # 直行
        self.__paintBoard.setPen(QColor("green"), 4)
        self.__paintBoard.drawLine(QPoint(300, 150), QPoint(100, 150))  # 右1--左1
        self.__paintBoard.drawLine(QPoint(100, 250), QPoint(300, 250))  # 左2--右2
        self.__paintBoard.drawLine(QPoint(150, 100), QPoint(150, 300))  # 上1 -- 下1
        self.__paintBoard.drawLine(QPoint(250, 300), QPoint(250, 100))  # 下2 -- 上2

        # 左行
        self.__paintBoard.setPen(QColor("blue"), 4)
        self.__paintBoard.drawLine(QPoint(100, 250), QPoint(250, 100))  # 左2 -- 上2
        self.__paintBoard.drawLine(QPoint(300, 150), QPoint(150, 300))  # 右1 -- 下1
        self.__paintBoard.drawLine(QPoint(150, 100), QPoint(300, 250))  # 上1 -- 右1
        self.__paintBoard.drawLine(QPoint(250, 300), QPoint(100, 150))  # 下2 -- 左1

        # 右行
        self.__paintBoard.setPen(QColor("red"), 4)
        self.__paintBoard.drawLine(QPoint(100, 250), QPoint(150, 300))  # 左2 -- 下1
        self.__paintBoard.drawLine(QPoint(300, 150), QPoint(250, 100))  # 右1 -- 上2
        self.__paintBoard.drawLine(QPoint(150, 100), QPoint(100, 150))  # 上1 -- 左1
        self.__paintBoard.drawLine(QPoint(250, 300), QPoint(300, 250))  # 下2 -- 右2

        # 掉头
        self.__paintBoard.setPen(QColor("#9e9e9e"), 4)
        self.__paintBoard.drawLine(QPoint(100, 250), QPoint(100, 150))
        self.__paintBoard.drawLine(QPoint(300, 150), QPoint(300, 250))
        self.__paintBoard.drawLine(QPoint(150, 100), QPoint(250, 100))
        self.__paintBoard.drawLine(QPoint(250, 300), QPoint(150, 300))

    def initTConnectLine(self):
        # 直行
        self.__paintBoard.setPen(QColor("green"), 4)
        self.__paintBoard.drawLine(QPoint(300, 150), QPoint(100, 150))  # 右1--左1
        self.__paintBoard.drawLine(QPoint(100, 250), QPoint(300, 250))  # 左2--右2

        # 左行
        self.__paintBoard.setPen(QColor("blue"), 4)
        self.__paintBoard.drawLine(QPoint(100, 250), QPoint(250, 100))  # 左2 -- 上2
        self.__paintBoard.drawLine(QPoint(150, 100), QPoint(300, 250))  # 上1 -- 右1

        # 右行
        self.__paintBoard.setPen(QColor("red"), 4)
        self.__paintBoard.drawLine(QPoint(300, 150), QPoint(250, 100))  # 右1 -- 上2
        self.__paintBoard.drawLine(QPoint(150, 100), QPoint(100, 150))  # 上1 -- 左1

        # 掉头
        self.__paintBoard.setPen(QColor("#9e9e9e"), 4)
        self.__paintBoard.drawLine(QPoint(100, 250), QPoint(100, 150))
        self.__paintBoard.drawLine(QPoint(300, 150), QPoint(300, 250))
        self.__paintBoard.drawLine(QPoint(150, 100), QPoint(250, 100))

    # 获取车道数
    def getRoadNum(self, item):
        type = item.get("type")
        fromroad = item.get("fromroad")
        toroad = item.get("toroad")

        fromRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + fromroad + '"]/lanes/section')
        fromRoadSection = fromRoadSections[-1]
        fromRoadNum = len(fromRoadSection.xpath("@rightlans")[0].split(";"))
        toRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + toroad + '"]/lanes/section')
        toRoadSection = toRoadSections[0]
        toRoadNum = len(toRoadSection.xpath("@rightlans")[0].split(";"))
        return {"fromRoadNum": fromRoadNum, "toRoadNum": toRoadNum}

        # if type == 'st':
        #     fromRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + fromroad + '"]/lanes/section')
        #     fromRoadSection = fromRoadSections[-1]
        #     fromRoadNum = len(fromRoadSection.xpath("@rightlans")[0].split(";"))
        #     toRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + toroad + '"]/lanes/section')
        #     toRoadSection = toRoadSections[0]
        #     toRoadNum = len(toRoadSection.xpath("@rightlans")[0].split(";"))
        #     return {"fromRoadNum": fromRoadNum, "toRoadNum": toRoadNum}
        # elif type == 'lt':
        #     fromRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + fromroad + '"]/lanes/section')
        #     fromRoadSection = fromRoadSections[-1]
        #     fromRoadNum = len(fromRoadSection.xpath("@rightlans")[0].split(";"))
        #     toRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + toroad + '"]/lanes/section')
        #     toRoadSection = toRoadSections[0]
        #     toRoadNum = len(toRoadSection.xpath("@rightlans")[0].split(";"))
        #     return {"fromRoadNum": fromRoadNum, "toRoadNum": toRoadNum}
        # elif type == 'rt':
        #     fromRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + fromroad + '"]/lanes/section')
        #     fromRoadSection = fromRoadSections[-1]
        #     fromRoadNum = len(fromRoadSection.xpath("@rightlans")[0].split(";"))
        #     toRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + toroad + '"]/lanes/section')
        #     toRoadSection = toRoadSections[0]
        #     toRoadNum = len(toRoadSection.xpath("@rightlans")[0].split(";"))
        #     return {"fromRoadNum": fromRoadNum, "toRoadNum": toRoadNum}
        # elif type == 'ut':
        #     fromRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + fromroad + '"]/lanes/section')
        #     fromRoadSection = fromRoadSections[-1]
        #     fromRoadNum = len(fromRoadSection.xpath("@rightlans")[0].split(";"))
        #     toRoadSections = self.root.xpath('//OpenDriveData/road[@id="' + toroad + '"]/lanes/section')
        #     toRoadSection = toRoadSections[0]
        #     toRoadNum = len(toRoadSection.xpath("@rightlans")[0].split(";"))
        #     return {"fromRoadNum": fromRoadNum, "toRoadNum": toRoadNum}

    def openPropsWinEvent(self):
        row = common.tableWidget.currentIndex().row()
        model = common.tableWidget.model()
        index = model.index(row, 0)  # 选中行第一列的内容
        fromroad = model.data(index)
        index = model.index(row, 1)
        toroad = model.data(index)
        if row == -1 or fromroad == None or toroad == None:
            QMessageBox.information(self, "温馨提示", "请选择一条正确记录！", QMessageBox.Yes, QMessageBox.Yes)
            return
        junctionID = self.inputID.text().strip()
        link = self.root.xpath(
            '//OpenDriveData/junction[@id="' + junctionID + '"]/links/link[@id="' + fromroad + toroad + '"]')
        if len(link) == 0:
            QMessageBox.information(self, "温馨提示", "你编辑的记录在文档中不存在，请先生成！", QMessageBox.Yes, QMessageBox.Yes)
            return

        # if len(common.list) == 0:
        #     QMessageBox.information(self, "温馨提示", "请先生成数据！", QMessageBox.Yes, QMessageBox.Yes)
        #     return
        if row == -1:
            print("你没有选择一行记录")
            QMessageBox.information(self, "温馨提示", "你选择你要编辑的记录！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            self.linkPropsWin.showWin(self.root, junctionID, fromroad, toroad)

    def readPropsListEvent(self):
        junctionID = self.inputID.text().strip()
        if junctionID == "":
            QMessageBox.information(self, "温馨提示", "ID不能为空，请输入！", QMessageBox.Yes, QMessageBox.Yes)
            return
        links = self.root.xpath('//OpenDriveData/junction[@id="' + junctionID + '"]/links/link')
        if len(links) == 0:
            QMessageBox.information(self, "温馨提示", "文档中没有这个ID的记录数据！", QMessageBox.Yes, QMessageBox.Yes)
            return
        _readRow = 0
        for readLink in links:
            readfromroad = readLink.xpath("@fromroad")
            readtoroad = readLink.xpath("@toroad")
            readtype = readLink.xpath("@type")
            readlinkid = readLink.xpath("@id")

            common.tableWidget.setItem(_readRow, 0, QTableWidgetItem(readfromroad[0]))
            common.tableWidget.setItem(_readRow, 1, QTableWidgetItem(readtoroad[0]))
            if readtype[0] == "st":
                common.tableWidget.setItem(_readRow, 2, QTableWidgetItem("直行"))
            elif readtype[0] == "lt":
                common.tableWidget.setItem(_readRow, 2, QTableWidgetItem("左行"))
            elif readtype[0] == "rt":
                common.tableWidget.setItem(_readRow, 2, QTableWidgetItem("右行"))
            elif readtype[0] == "ut":
                common.tableWidget.setItem(_readRow, 2, QTableWidgetItem("掉头"))
            _readRow = _readRow + 1

    def openSignalEditEvent(self):

        row = common.tableWidget.currentIndex().row()
        model = common.tableWidget.model()
        index = model.index(row, 0)  # 选中行第一列的内容
        fromroad = model.data(index)
        index = model.index(row, 1)
        toroad = model.data(index)
        if row == -1 or fromroad == None or toroad == None:
            QMessageBox.information(self, "温馨提示", "请选择一条正确记录！", QMessageBox.Yes, QMessageBox.Yes)
            return
        junctionID = self.inputID.text().strip()
        link = self.root.xpath(
            '//OpenDriveData/junction[@id="' + junctionID + '"]/links/link[@id="' + fromroad + toroad + '"]')
        if len(link) == 0:
            QMessageBox.information(self, "温馨提示", "你编辑的记录在文档中不存在，请先生成！", QMessageBox.Yes, QMessageBox.Yes)
            return

        # if len(common.list) == 0:
        #     QMessageBox.information(self, "温馨提示", "请先生成数据！", QMessageBox.Yes, QMessageBox.Yes)
        #     return
        if row == -1:
            print("你没有选择一行记录")
            QMessageBox.information(self, "温馨提示", "你选择你要编辑的记录！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            self.signalEditWin.showWin(junctionID, fromroad + toroad, fromroad, toroad, )
            # self.linkPropsWin.showWin(self.root, junctionID, fromroad, toroad)

    def openSectionWinEvent(self):
        self.sectionWin.showWin()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CrossRoadTool()
    sys.exit(app.exec_())
