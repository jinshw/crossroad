#!/usr/bin/env python
# coding:utf-8
from PyQt5.QtCore import QRectF, QLineF, Qt
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import (QGraphicsView, QGraphicsScene, QApplication, QGraphicsLineItem, QGraphicsRectItem,
                             QGraphicsSimpleTextItem)


class MyRoadItem(QGraphicsRectItem):
    def __init__(self, x, y, h, w):
        super(MyRoadItem, self).__init__()
        # self.setFlag(True)
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.pen = self.pen()
        self.pen.setWidth(2)
        self.pen.setColor(QColor("green"))
        self.drawRect()

    def drawRect(self):
        self.setPen(self.pen)
        self.setRect(QRectF(self.x, self.y, self.h, self.w))

    def drawText(self, text):
        st = QGraphicsSimpleTextItem()

    def setStyle(self, width, borderColor):
        self.pen.setWidth(0)
        # self.pen.setWidth(width)
        self.pen.setColor(QColor(borderColor))
        self.setBrush(QColor(197, 197, 197))
        self.drawRect()


class MyQGraphicsSimpleTextItem(QGraphicsSimpleTextItem):
    def __init__(self, text):
        super(MyQGraphicsSimpleTextItem, self).__init__()
        self.setText(text)


class MyQGraphicsLineItem(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2, qcolor):
        super(MyQGraphicsLineItem, self).__init__()
        self.pen = self.pen()
        self.pen.setColor(qcolor)
        self.pen.setWidth(2)
        self.setPen(self.pen)
        # 设置直线位于(x1, y1) 和(x2, y2) 之间
        self.setLine(QLineF(x1, y1, x2, y2))


class MainWindow(QGraphicsView):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 650, 1000, 220)
        # 创建场景
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(-50, -100, 1000, 200)

        # self.list = [
        #     {"s": "0", "rightlans": "3;3;3.75;3.75;3.75", "rightpre": "-1;-2;-3;-4;-5", "rightsuc": "-1;-2;-3;-4;-5"},
        #     {"s": "75", "rightlans": "0;0;3.75;3.75;3.75", "rightpre": "-1;-2;-3;-4;-5", "rightsuc": "-1;-1;-1;-2;-3"},
        #     {"s": "76", "rightlans": "3.75;3.75;3.75", "rightpre": "-3;-4;-5", "rightsuc": "-2;-3;-4"},
        #     {"s": "550", "rightlans": "0;3.75;3.75;3.75", "rightpre": ";-1;-2;-3", "rightsuc": "-1;-2;-3;-4"},
        #     {"s": "570", "rightlans": "3;3.75;3.75;3.75", "rightpre": "-1;-2;-3;-4", "rightsuc": "-1;-2;-3;-4"},
        # ]

        self.list = [
            {"s": "0", "rightlans": "3.75;3.75;3.75", "rightpre": "-1;-2;-3", "rightsuc": "-1;-2;-4"},
            {"s": "150", "rightlans": "3.75;3.75;0;3.75", "rightpre": "-1;-2;;-3", "rightsuc": "-1;-2;-3;-4"},
            {"s": "169", "rightlans": "3.75;3.75;3;3.75", "rightpre": "-1;-2;-3;-4", "rightsuc": "-2;-3;-5;-6"},
            {"s": "170", "rightlans": "0;3.75;3.75;0;3;3.75", "rightpre": ";-1;-2;;-3;-4",
             "rightsuc": "-1;-2;-3;-5;-6"},
            {"s": "190", "rightlans": "3.5;3;3;3;3;3.75", "rightpre": ";-1;-2;-3;-4;-5;-6",
             "rightsuc": "-1;-2;-3;-5;-6"},
        ]
        # self.list = list
        # self.initBoard(self.list)

    def drawSection(self, list):
        self.clearBoard()
        self.list = list
        if len(list) > 0:
            self.initBoard()

    def initBoard(self):
        sectionWidth = 50
        sectionHeight = 10
        roadCount = 10
        startX = 0
        startY = 0
        offsetRoadCount = 0

        # 道路标线
        standardItem = MyQGraphicsLineItem(startX, startY, startX + sectionWidth * roadCount + 100, startY,
                                           QColor(0, 0, 0))
        self.scene.addItem(standardItem)
        # for sectionIndex in range(0, 5):
        listLen = len(self.list)
        for sectionIndex in range(0, listLen - 1):
            # roadCount = roadCount - 1
            currentRightLans = self.list[sectionIndex].get("rightlans")
            nextRightLans = self.list[sectionIndex + 1].get("rightlans")
            offsetRoadCount = self.getRightOffsexCount(offsetRoadCount, currentRightLans, nextRightLans)
            offsetRoadHeight = offsetRoadCount * sectionHeight

            s = self.list[sectionIndex].get("s")
            rightpre = self.list[sectionIndex + 1].get("rightpre")
            rightpreList = rightpre.split(";")
            startX = sectionWidth * sectionIndex + 0

            # 标线右侧道路
            sectionRoadCount = 0
            for i in range(0, len(rightpreList)):
                if rightpreList[i].strip() != "":
                    _y = sectionRoadCount * sectionHeight + startY + offsetRoadHeight
                    sectionRoadCount = sectionRoadCount + 1
                    # _y = i * sectionHeight + startY + offsetRoadHeight
                    myRoad = MyRoadItem(startX, _y, sectionWidth, sectionHeight)
                    myRoad.setStyle(2, "green")
                    myQGraphicsSimpleTextItem = MyQGraphicsSimpleTextItem(rightpreList[i])
                    # myQGraphicsSimpleTextItem = MyQGraphicsSimpleTextItem("-" + str(i + 1))
                    myQGraphicsSimpleTextItem.setPos(startX + (int(sectionWidth) / 2) - 2,
                                                     _y + (int(sectionHeight) / 2 - 4))
                    self.scene.addItem(myRoad)
                    self.scene.addItem(myQGraphicsSimpleTextItem)

            # section竖线
            sectionItem = MyQGraphicsLineItem(startX, startY - 50, startX, _y + 10, QColor(0, 160, 230))
            self.scene.addItem(sectionItem)
            mySectionText = MyQGraphicsSimpleTextItem(s)
            # mySectionText = MyQGraphicsSimpleTextItem(str(sectionIndex))
            # mySectionText = MyQGraphicsSimpleTextItem("0")
            mySectionText.setPos(startX - 10, startY - 50)
            self.scene.addItem(mySectionText)

        # 处理最后一个section
        lastX = sectionWidth * (len(self.list) - 1)
        s = self.list[len(self.list) - 1].get("s")
        sectionItem = MyQGraphicsLineItem(lastX, startY - 50, lastX, _y + 10, QColor(0, 160, 230))
        self.scene.addItem(sectionItem)
        mySectionText = MyQGraphicsSimpleTextItem(s)
        # mySectionText = MyQGraphicsSimpleTextItem(str(sectionIndex))
        # mySectionText = MyQGraphicsSimpleTextItem("0")
        mySectionText.setPos(lastX - 10, startY - 50)
        self.scene.addItem(mySectionText)

        # 将场景加载到窗口
        self.setScene(self.scene)

    def addBorders(self):
        self.borders = []
        rect = QRectF(0, 0, 400, 400)
        self.borders.append(self.scene.addRect(rect, QColor("yellow")))

    def getRightOffsexCount(self, offset, currentLans, nextLans):
        currentLansList = currentLans.split(";")
        nextLansList = nextLans.split(";")
        if len(currentLansList) > len(nextLansList):
            for item in currentLansList:
                if item == "0":  # 向右偏移车道，偏移量+1
                    offset = offset + 1
                else:
                    break;
        else:
            for item in currentLansList:
                if item == "0":  # 偏移量-1
                    offset = offset - 1
                else:
                    break;

        return offset

    def clearBoard(self):
        self.scene.clear()