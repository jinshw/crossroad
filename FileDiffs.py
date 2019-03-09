import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QTreeWidgetItem, QFileDialog, QMessageBox, \
    QButtonGroup
from lxml import etree

from diffs import Ui_diffs


class FileDiffs(QWidget, Ui_diffs):
    def __init__(self):
        super(FileDiffs, self).__init__()
        self.setupUi(self)
        self.initUI()

        self.leftRoot = None
        self.rightRoot = None
        self.rightPath = ""

    def initUI(self):
        # 保留原有数据 为默认
        # self.retainRadioButton.setChecked(True)
        self.replaceAddRadioButton.setChecked(True)
        self.bg = QButtonGroup(self)
        self.bg.addButton(self.retainRadioButton, 1)
        self.bg.addButton(self.replaceRadioButton, 2)
        self.bg.addButton(self.replaceAddRadioButton, 3)
        self.bg.buttonClicked.connect(self.btnstate)

        self.initTree()
        self.initAction()

    def initAction(self):
        self.leftSelectAllBT.clicked.connect(self.selectAll)
        self.rightSelectAllBT.clicked.connect(self.selectRightAll)
        self.leftClearBT.clicked.connect(self.clearLeftAll)
        self.rightClearBT.clicked.connect(self.clearRightAll)
        self.leftOpenBT.clicked.connect(self.leftOpenAction)
        self.rightOpenBT.clicked.connect(self.rightOpenAction)
        self.runBT.clicked.connect(self.runAction)
        self.readRightBT.clicked.connect(self.readRightBTAction)
        self.rightRemoveBT.clicked.connect(self.rightRemoveAction)
        self.leftFilterBT.clicked.connect(self.leftFilterBTAction)
        self.rightFilterBT.clicked.connect(self.rightFilterBTAction)

    def initTree(self):
        # 设置列数
        # self.leftTreeWidget.setColumnCount(6)
        # 设置树形控件头部的标题
        # self.leftTreeWidget.setHeaderLabels(['id', 'type', "name", "s", "t", "zOffset"])
        self.leftTreeWidget.setColumnWidth(0, 140)
        self.leftTreeWidget.setColumnWidth(1, 140)
        self.leftTreeWidget.setColumnWidth(2, 160)
        self.leftTreeWidget.setColumnWidth(3, 160)
        self.leftTreeWidget.setColumnWidth(4, 160)
        self.leftTreeWidget.setColumnWidth(5, 70)
        self.leftTreeWidget.setMinimumWidth(850)
        self.leftTreeWidget.itemClicked.connect(self.selectRow)

        self.rightTreeWidget.setColumnWidth(0, 140)
        self.rightTreeWidget.setColumnWidth(1, 140)
        self.rightTreeWidget.setColumnWidth(2, 160)
        self.rightTreeWidget.setColumnWidth(3, 160)
        self.rightTreeWidget.setColumnWidth(4, 160)
        self.rightTreeWidget.setColumnWidth(5, 70)
        self.rightTreeWidget.setMinimumWidth(850)
        self.rightTreeWidget.itemClicked.connect(self.selectRow)
        # self.rightTreeWidget.itemClicked.connect(self.selectRow)

        # # 设置根节点
        # self.root = QTreeWidgetItem(self.leftTreeWidget)
        # self.root.setText(0, 'Root')
        # self.root.setCheckState(0, Qt.Checked)
        #
        # # 设置树形控件的列的宽度
        # self.leftTreeWidget.setColumnWidth(0, 150)
        #
        # child1 = QTreeWidgetItem()
        # child1.setText(0, 'child1')
        # child1.setText(1, 'ios1')
        # child1.setText(2, 'ios2')
        # child1.setText(3, 'ios3')
        # child1.setText(4, 'ios4')
        # child1.setText(5, 'ios5')
        #
        # # todo 优化1 设置节点的状态
        # child1.setCheckState(0, Qt.Checked)
        # self.root.addChild(child1)
        #
        # # 设置子节点2
        # child2 = QTreeWidgetItem(self.root)
        # child2.setText(0, 'child2')
        # child2.setText(1, '')
        # child2.setCheckState(0, Qt.Checked)
        #
        # # 加载根节点的所有属性与子控件
        # self.leftTreeWidget.addTopLevelItem(self.root)
        #
        # root2 = QTreeWidgetItem(self.leftTreeWidget)
        # root2.setText(0, 'Root222')
        # root2.setCheckState(0, Qt.Checked)
        # self.leftTreeWidget.addTopLevelItem(root2)

        # 节点全部展开
        # self.leftTreeWidget.expandAll()
        # self.leftTreeWidget.itemClicked.connect(self.selectRow)

    def selectRow(self, item, column):
        print(item, column)
        if column != 0:
            return
        # self.checkParent(item)
        # self.checkChildren(item)
        for i in range(0, item.childCount()):
            item.child(i).setCheckState(0, item.checkState(0))

        p = item.parent()
        if p != 0 and p != None:
            p.setCheckState(0, item.checkState(0))
            for k in range(0, p.childCount()):
                if p.child(k).checkState(0) != item.checkState(0):
                    p.setCheckState(0, Qt.PartiallyChecked)
                    return;

    def selectAll(self):
        for k in range(0, self.leftTreeWidget.topLevelItemCount()):
            root = self.leftTreeWidget.topLevelItem(k)
            root.setCheckState(0, Qt.Checked)
            for i in range(0, root.childCount()):
                root.child(i).setCheckState(0, Qt.Checked)

    def selectRightAll(self):
        for k in range(0, self.rightTreeWidget.topLevelItemCount()):
            root = self.rightTreeWidget.topLevelItem(k)
            root.setCheckState(0, Qt.Checked)
            for i in range(0, root.childCount()):
                root.child(i).setCheckState(0, Qt.Checked)

    def clearLeftAll(self):
        for k in range(0, self.leftTreeWidget.topLevelItemCount()):
            root = self.leftTreeWidget.topLevelItem(k)
            root.setCheckState(0, 0)
            for i in range(0, root.childCount()):
                root.child(i).setCheckState(0, 0)

    def clearRightAll(self):
        for k in range(0, self.rightTreeWidget.topLevelItemCount()):
            root = self.rightTreeWidget.topLevelItem(k)
            root.setCheckState(0, 0)
            for i in range(0, root.childCount()):
                root.child(i).setCheckState(0, 0)

    def leftOpenAction(self):
        self.leftPath, self.leftRoot = self.openAction()
        if self.leftPath == "":
            return
        print(self.leftPath, self.leftRoot)
        self.readLeftXML()

    def readLeftXML(self):
        self.leftPathLE.setText(self.leftPath)
        self.getLeftRoadList()

        self.leftTreeWidget.clear()
        self.leftRoadList.sort()
        for i in range(0, len(self.leftRoadList)):
            id = self.leftRoadList[i]
            roadNote = QTreeWidgetItem(self.leftTreeWidget)
            roadNote.setText(0, id)
            roadNote.setCheckState(0, 0)
            # roadNote.setCheckState(0, Qt.Checked)

            objectList = self.leftRoot.xpath("//OpenDRIVE/road[@id='" + id + "']/objects/object")
            for objectIndex in range(0, len(objectList)):
                object = objectList[objectIndex]
                objectId = object.xpath("@id")[0]
                objectType = object.xpath("@type")[0]
                objectName = object.xpath("@name")[0]
                s = object.xpath("@s")[0]
                t = object.xpath("@t")[0]
                zOffset = object.xpath("@zOffset")[0]

                # 子节点
                child1 = QTreeWidgetItem()
                child1.setText(0, objectId)
                child1.setText(1, objectType)
                child1.setText(2, objectName)
                child1.setText(3, s)
                child1.setText(4, t)
                child1.setText(5, zOffset)
                child1.setCheckState(0, 0)
                # child1.setCheckState(0, Qt.Checked)
                roadNote.addChild(child1)
            self.leftTreeWidget.addTopLevelItem(roadNote)
            self.leftTreeWidget.collapseAll()

    def rightOpenAction(self):
        self.rightPath, self.rightRoot = self.openAction()
        if self.rightPath == "":
            return
        self.readRightXML()

    def readRightXML(self):
        parserRight = etree.XMLParser(remove_blank_text=True)
        xmlRight = etree.parse(self.rightPath, parserRight)
        self.rightRoot = xmlRight.getroot()  # 获取根节点

        self.rightPathLE.setText(self.rightPath)
        self.getRightRoadList()
        self.rightTreeWidget.clear()
        self.rightRoadList.sort()
        for i in range(0, len(self.rightRoadList)):
            id = self.rightRoadList[i]
            roadNote = QTreeWidgetItem(self.rightTreeWidget)
            roadNote.setText(0, id)
            roadNote.setCheckState(0, 0)

            objectList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + id + "']/objects/object")
            for objectIndex in range(0, len(objectList)):
                object = objectList[objectIndex]
                objectId = object.xpath("@id")[0]
                objectType = object.xpath("@type")[0]
                objectName = object.xpath("@name")[0]
                s = object.xpath("@s")[0]
                t = object.xpath("@t")[0]
                zOffset = object.xpath("@zOffset")[0]

                # 子节点
                child1 = QTreeWidgetItem()
                child1.setText(0, objectId)
                child1.setText(1, objectType)
                child1.setText(2, objectName)
                child1.setText(3, s)
                child1.setText(4, t)
                child1.setText(5, zOffset)
                child1.setCheckState(0, 0)
                roadNote.addChild(child1)

            self.rightTreeWidget.addTopLevelItem(roadNote)
            # 树收起
            self.rightTreeWidget.collapseAll()

    def readRightBTAction(self):
        if self.rightPath == "":
            return
        self.readRightXML()

    def openAction(self):
        path = QFileDialog.getOpenFileName(self, '选择文件', '',
                                           "All Files (*);;Text Files (*.xml);;xyz Files (*.xodr)")
        root = ""
        if path[0] != "":
            root = self.getXMLRoot(path[0])
        return path[0], root

    # 获取XML的根节点
    def getXMLRoot(self, filepath):
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            xml = etree.parse(filepath, parser)
            root = xml.getroot()  # 获取根节点
        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", '错误信息：{0}'.format(err), QMessageBox.Yes, QMessageBox.Yes)
        return root

    def getLeftRoadList(self):
        filterStr = self.leftRoadidLE.text().strip()
        root = self.leftRoot
        self.leftRoadList = []
        if filterStr == "":
            roadEleList = root.xpath("//OpenDRIVE/road")
        else:
            roadEleList = root.xpath("//OpenDRIVE/road[@id='" + filterStr + "']")

        for i in range(0, len(roadEleList)):
            roadEle = roadEleList[i]
            id = roadEle.xpath("@id")[0]
            self.leftRoadList.append(id)

    def getRightRoadList(self):
        filterStr = self.rightRoadidLE.text().strip()
        root = self.rightRoot
        self.rightRoadList = []
        if filterStr == "":
            roadEleList = root.xpath("//OpenDriveData/road")
        else:
            roadEleList = root.xpath("//OpenDriveData/road[@id='" + filterStr + "']")

        for i in range(0, len(roadEleList)):
            roadEle = roadEleList[i]
            id = roadEle.xpath("@id")[0]
            self.rightRoadList.append(id)

    def getLeftSelectedTreeDataAction(self):
        self.leftSelectDatas = {}
        topCount = self.leftTreeWidget.topLevelItemCount()
        for i in range(0, topCount):
            currentItem = self.leftTreeWidget.topLevelItem(i)
            # QtCore.Qt.Checked选中，QtCore.Qt.PartiallyChecked 部分选中
            if currentItem.checkState(0) == QtCore.Qt.Checked or currentItem.checkState(
                    0) == QtCore.Qt.PartiallyChecked:
                roadId = currentItem.text(0)
                print(roadId)
                childList = []
                for cindex in range(0, currentItem.childCount()):
                    childItem = currentItem.child(cindex)
                    if childItem.checkState(0) == QtCore.Qt.Checked:
                        cid = childItem.text(0)
                        ctype = childItem.text(1)
                        cname = childItem.text(2)
                        cs = childItem.text(3)
                        ct = childItem.text(4)
                        czOffset = childItem.text(5)
                        print("object id=" + childItem.text(0))
                        childList.append(
                            {"id": cid, "type": ctype, "name": cname, "s": cs, "t": ct, "zOffset": czOffset})

                self.leftSelectDatas[roadId] = childList

    def getRightSelectedTreeDataAction(self):
        self.rightSelectDatas = {}
        topCount = self.rightTreeWidget.topLevelItemCount()
        for i in range(0, topCount):
            currentItem = self.rightTreeWidget.topLevelItem(i)
            # QtCore.Qt.Checked选中，QtCore.Qt.PartiallyChecked 部分选中
            if currentItem.checkState(0) == QtCore.Qt.Checked or currentItem.checkState(
                    0) == QtCore.Qt.PartiallyChecked:
                roadId = currentItem.text(0)
                childList = []
                for cindex in range(0, currentItem.childCount()):
                    childItem = currentItem.child(cindex)
                    if childItem.checkState(0) == QtCore.Qt.Checked:
                        cid = childItem.text(0)
                        ctype = childItem.text(1)
                        cname = childItem.text(2)
                        cs = childItem.text(3)
                        ct = childItem.text(4)
                        czOffset = childItem.text(5)
                        print("object id=" + childItem.text(0))
                        childList.append(
                            {"id": cid, "type": ctype, "name": cname, "s": cs, "t": ct, "zOffset": czOffset})

                self.rightSelectDatas[roadId] = childList

    def getLeftAllTreeDataAction(self):
        self.leftSelectDatas = {}
        topCount = self.leftTreeWidget.topLevelItemCount()
        for i in range(0, topCount):
            currentItem = self.leftTreeWidget.topLevelItem(i)
            # QtCore.Qt.Checked选中，QtCore.Qt.PartiallyChecked 部分选中
            # if currentItem.checkState(0) == QtCore.Qt.Checked or currentItem.checkState(
            #         0) == QtCore.Qt.PartiallyChecked:
            roadId = currentItem.text(0)
            childList = []
            self.leftSelectDatas[roadId] = childList

    def getRightTreeDataAction(self):
        pass

    def runAction(self):
        if self.leftRoot == None or self.leftRoot == "":
            QMessageBox.information(self, "温馨提示", "请先选xodr文件！", QMessageBox.Yes, QMessageBox.Yes)
            return
        if self.rightRoot == None or self.rightRoot == "":
            QMessageBox.information(self, "温馨提示", "请先选XML文件！", QMessageBox.Yes, QMessageBox.Yes)
            return

        # 获取xodr（左侧）中objects数据
        parser = etree.XMLParser(remove_blank_text=True)
        xml = etree.parse(self.leftPath, parser)
        self.leftRoot = xml.getroot()  # 获取根节点

        parserRight = etree.XMLParser(remove_blank_text=True)
        xmlRight = etree.parse(self.rightPath, parserRight)
        self.rightRoot = xmlRight.getroot()  # 获取根节点

        # 保留原有数据和新增
        if self.bg.checkedId() == 1:  # 保留原有数据
            print(self.bg.checkedId())
            # 获取左侧数据
            self.getLeftSelectedTreeDataAction()
            if len(self.leftSelectDatas) == 0:
                QMessageBox.information(self, "温馨提示", "请选择需要新增的记录！", QMessageBox.Yes, QMessageBox.Yes)
                return

            self.retainData()

        # 替换全部数据
        elif self.bg.checkedId() == 2:  # 替换原有数据
            print(self.bg.checkedId())
            self.getLeftAllTreeDataAction()
            try:
                self.replaceData()
            except Exception as err:
                print('错误信息：{0}'.format(err))

        elif self.bg.checkedId() == 3:  # 替换和新增
            # 获取左侧数据
            self.getLeftSelectedTreeDataAction()
            if len(self.leftSelectDatas) == 0:
                QMessageBox.information(self, "温馨提示", "请选择需要执行的记录！", QMessageBox.Yes, QMessageBox.Yes)
                return
            self.replaceAddData()

        try:
            # 节点转为tree对象
            tree = etree.ElementTree(self.rightRoot)
            '''
            各个参数含义如下：
            1）第1个参数是xml的完整路径(包括文件名)；
            2）pretty_print参数是否美化代码；
            3）xml_declaration参数是否写入xml声明，就是我们看到xml文档第1行文字；
            4）encoding参数很明显是保存的编码。
            '''
            tree.write(self.rightPath, pretty_print=True, xml_declaration=True, encoding='utf-8')
            QMessageBox.information(self, "温馨提示", "xml生成成功！", QMessageBox.Yes, QMessageBox.Yes)

            # 重新加载xml
            self.readRightBTAction()
        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", "生成xml失败！", QMessageBox.Yes, QMessageBox.Yes)

    def retainData(self):
        for roadId, childList in self.leftSelectDatas.items():
            print(roadId, childList)
            for cindex in range(0, len(childList)):
                child = childList[cindex]
                self.insertToXML(roadId, child)

    def replaceAddData(self):
        for roadId, childList in self.leftSelectDatas.items():
            print(roadId, childList)
            for cindex in range(0, len(childList)):
                child = childList[cindex]
                self.replaceAddToXML(roadId, child)

    def rightDeleteSelectedNote(self):
        for roadId, childList in self.rightSelectDatas.items():
            for cindex in range(0, len(childList)):
                child = childList[cindex]
                id = child["id"]
                type = child["type"]
                name = child["name"]
                if self.rightRoot == None:
                    QMessageBox.information(self, "温馨提示", "请先选XML文件！", QMessageBox.Yes, QMessageBox.Yes)
                    return

                objectsList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + roadId + "']/objects")
                objectList = self.rightRoot.xpath(
                    "//OpenDriveData/road[@id='" + roadId + "']/objects/object[@id='" +
                    id + "'and @type='" + type + "' and @name='" + name + "' ]")
                objectsList[0].remove(objectList[0])

    def insertToXML(self, roadId, child):
        id = child["id"]
        type = child["type"]
        name = child["name"]
        s = child["s"]
        t = child["t"]
        zOffset = child["zOffset"]
        if self.rightRoot == None:
            QMessageBox.information(self, "温馨提示", "请先选XML文件！", QMessageBox.Yes, QMessageBox.Yes)
            return

        if self.leftRoot == None:
            QMessageBox.information(self, "温馨提示", "请先选xodr文件！", QMessageBox.Yes, QMessageBox.Yes)
            return

        # 从xml文件中查询是否存在该条数据
        roadList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + roadId + "']")
        objectList = self.rightRoot.xpath(
            "//OpenDriveData/road[@id='" + roadId + "']/objects/object[@id='" +
            id + "'and @type='" + type + "' and @name='" + name + "' ]")

        # xml文件中没有该条记录
        if len(objectList) == 0 and len(roadList) == 1:
            leftObjectList = self.leftRoot.xpath("//OpenDRIVE/road[@id='" + roadId + "']/objects/object[@id='" +
                                                 id + "'and @type='" + type + "' and @name='" + name + "']")

            rightObjectsList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + roadId + "']/objects")

            if len(rightObjectsList) == 0:# right 端没有objects节点
                objects = etree.SubElement(roadList[0], "objects")
                objects.append(leftObjectList[0])
            else:
                rightObjectsList[0].append(leftObjectList[0])

            # rightObjectsList[0].append(leftObjectList[0])

    def replaceAddToXML(self, roadId, child):
        id = child["id"]
        type = child["type"]
        name = child["name"]
        s = child["s"]
        t = child["t"]
        zOffset = child["zOffset"]
        if self.rightRoot == None:
            QMessageBox.information(self, "温馨提示", "请先选XML文件！", QMessageBox.Yes, QMessageBox.Yes)
            return

        if self.leftRoot == None:
            QMessageBox.information(self, "温馨提示", "请先选xodr文件！", QMessageBox.Yes, QMessageBox.Yes)
            return

        # 从xml文件中查询是否存在该条数据
        roadList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + roadId + "']")
        objectList = self.rightRoot.xpath(
            "//OpenDriveData/road[@id='" + roadId + "']/objects/object[@id='" +
            id + "'and @type='" + type + "' and @name='" + name + "']")

        # xml文件中没有该条记录
        if len(objectList) == 0 and len(roadList) == 1:  # id|name|type 不同 新增
            leftObjectList = self.leftRoot.xpath("//OpenDRIVE/road[@id='" + roadId + "']/objects/object[@id='" +
                                                 id + "'and @type='" + type + "' and @name='" + name + "']")
            rightObjectsList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + roadId + "']/objects")
            if len(rightObjectsList) == 0:# right 端没有objects节点
                objects = etree.SubElement(roadList[0], "objects")
                objects.append(leftObjectList[0])
            else:
                rightObjectsList[0].append(leftObjectList[0])

        elif len(objectList) > 0 and len(roadList) == 1:  # id|name|type 相同 替换
            leftObjectList = self.leftRoot.xpath("//OpenDRIVE/road[@id='" + roadId + "']/objects/object[@id='" +
                                                 id + "'and @type='" + type + "' and @name='" + name + "']")
            rightObjectsList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + roadId + "']/objects")
            rightObjectsList[0].remove(objectList[0])
            rightObjectsList[0].append(leftObjectList[0])

    def replaceData(self):
        try:
            for roadId, childList in self.leftSelectDatas.items():
                print(roadId, childList)
                self.replaceToXML(roadId)
        except Exception as err:
            print('错误信息：{0}'.format(err))

    def replaceToXML(self, roadId):
        try:
            if self.rightRoot == None:
                QMessageBox.information(self, "温馨提示", "请先选XML文件！", QMessageBox.Yes, QMessageBox.Yes)
                return

            if self.leftRoot == None:
                QMessageBox.information(self, "温馨提示", "请先选xodr文件！", QMessageBox.Yes, QMessageBox.Yes)
                return

            # 从xml文件中查询是否存在该条数据
            roadList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + roadId + "']")
            objectsList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + roadId + "']/objects")
            leftObjectsList = self.leftRoot.xpath("//OpenDRIVE/road[@id='" + roadId + "']/objects")

            if len(leftObjectsList) > 0:
                if len(roadList) == 1 and len(objectsList) != 0:
                    # 删除xml（右侧）中已有的objects节点
                    roadList[0].remove(objectsList[0])
                    roadList[0].append(leftObjectsList[0])
        except Exception as err:
            print('错误信息：{0}'.format(err))

    def btnstate(self):
        if self.bg.checkedId() == 1:  # 保留原有数据和新增
            print(self.bg.checkedId())
        elif self.bg.checkedId() == 2:  # 替换全部数据
            print(self.bg.checkedId())
        elif self.bg.checkedId() == 3:  # 替换和新增
            pass

    def rightRemoveAction(self):
        if self.rightRoot == None or self.rightRoot == "":
            QMessageBox.information(self, "温馨提示", "请先选XML文件！", QMessageBox.Yes, QMessageBox.Yes)
            return

        # 获取左侧数据
        self.getRightSelectedTreeDataAction()
        if len(self.rightSelectDatas) == 0:
            QMessageBox.information(self, "温馨提示", "请选择需要删除的记录！", QMessageBox.Yes, QMessageBox.Yes)
            return

        reply = QMessageBox.information(self, "温馨提示", "是否删除选中记录！", QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.rightDeleteSelectedNote()
            try:
                # 节点转为tree对象
                tree = etree.ElementTree(self.rightRoot)
                '''
                各个参数含义如下：
                1）第1个参数是xml的完整路径(包括文件名)；
                2）pretty_print参数是否美化代码；
                3）xml_declaration参数是否写入xml声明，就是我们看到xml文档第1行文字；
                4）encoding参数很明显是保存的编码。
                '''
                tree.write(self.rightPath, pretty_print=True, xml_declaration=True, encoding='utf-8')
                QMessageBox.information(self, "温馨提示", "删除成功！", QMessageBox.Yes, QMessageBox.Yes)
                # 重新加载xml
                self.readRightBTAction()
            except Exception as err:
                print('错误信息：{0}'.format(err))
                QMessageBox.information(self, "温馨提示", "生成xml失败！", QMessageBox.Yes, QMessageBox.Yes)
        else:
            return

    def leftFilterBTAction(self):
        parser = etree.XMLParser(remove_blank_text=True)
        xml = etree.parse(self.leftPath, parser)
        self.leftRoot = xml.getroot()  # 获取根节点

        if self.leftRoot == None or self.leftRoot == "":
            QMessageBox.information(self, "温馨提示", "请先选xodr文件！", QMessageBox.Yes, QMessageBox.Yes)
            return
        # if self.rightRoot == None or self.rightRoot == "":
        #     QMessageBox.information(self, "温馨提示", "请先选XML文件！", QMessageBox.Yes, QMessageBox.Yes)
        #     return
        self.getLeftRoadList()
        self.leftTreeWidget.clear()
        self.leftRoadList.sort()
        for i in range(0, len(self.leftRoadList)):
            id = self.leftRoadList[i]
            roadNote = QTreeWidgetItem(self.leftTreeWidget)
            roadNote.setText(0, id)
            roadNote.setCheckState(0, Qt.Checked)

            objectList = self.leftRoot.xpath("//OpenDRIVE/road[@id='" + id + "']/objects/object")
            for objectIndex in range(0, len(objectList)):
                object = objectList[objectIndex]
                objectId = object.xpath("@id")[0]
                objectType = object.xpath("@type")[0]
                objectName = object.xpath("@name")[0]
                s = object.xpath("@s")[0]
                t = object.xpath("@t")[0]
                zOffset = object.xpath("@zOffset")[0]

                # 子节点
                child1 = QTreeWidgetItem()
                child1.setText(0, objectId)
                child1.setText(1, objectType)
                child1.setText(2, objectName)
                child1.setText(3, s)
                child1.setText(4, t)
                child1.setText(5, zOffset)
                child1.setCheckState(0, Qt.Checked)
                roadNote.addChild(child1)
            self.leftTreeWidget.addTopLevelItem(roadNote)
            self.leftTreeWidget.collapseAll()

    def rightFilterBTAction(self):
        parserRight = etree.XMLParser(remove_blank_text=True)
        xmlRight = etree.parse(self.rightPath, parserRight)
        self.rightRoot = xmlRight.getroot()  # 获取根节点

        if self.rightRoot == None or self.rightRoot == "":
            QMessageBox.information(self, "温馨提示", "请先选XML文件！", QMessageBox.Yes, QMessageBox.Yes)
            return

        parserRight = etree.XMLParser(remove_blank_text=True)
        xmlRight = etree.parse(self.rightPath, parserRight)
        self.rightRoot = xmlRight.getroot()  # 获取根节点

        self.rightPathLE.setText(self.rightPath)
        self.getRightRoadList()
        self.rightTreeWidget.clear()
        self.rightRoadList.sort()
        for i in range(0, len(self.rightRoadList)):
            id = self.rightRoadList[i]
            roadNote = QTreeWidgetItem(self.rightTreeWidget)
            roadNote.setText(0, id)
            roadNote.setCheckState(0, 0)

            objectList = self.rightRoot.xpath("//OpenDriveData/road[@id='" + id + "']/objects/object")
            for objectIndex in range(0, len(objectList)):
                object = objectList[objectIndex]
                objectId = object.xpath("@id")[0]
                objectType = object.xpath("@type")[0]
                objectName = object.xpath("@name")[0]
                s = object.xpath("@s")[0]
                t = object.xpath("@t")[0]
                zOffset = object.xpath("@zOffset")[0]

                # 子节点
                child1 = QTreeWidgetItem()
                child1.setText(0, objectId)
                child1.setText(1, objectType)
                child1.setText(2, objectName)
                child1.setText(3, s)
                child1.setText(4, t)
                child1.setText(5, zOffset)
                child1.setCheckState(0, 0)
                roadNote.addChild(child1)

            self.rightTreeWidget.addTopLevelItem(roadNote)
            # 树收起
            self.rightTreeWidget.collapseAll()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FileDiffs()
    win.show()
    sys.exit(app.exec_())
