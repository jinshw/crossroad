from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget


class CrossPaintBoard(QWidget):
    def __init__(self, Parent=None):
        super().__init__(Parent)
        self.initUI()
        self.initView()

    def initView(self):
        self.setFixedSize(self.__size)

    def initUI(self):
        self.__size = QSize(400, 400)
        self.__board = QPixmap(self.__size)  # 新建QPixmap作为画板，宽350px,高250px
        self.__board.fill(Qt.white)  # 用白色填充画板

        self.__IsEmpty = True  # 默认为空画板
        self.EraserMode = False  # 默认为禁用橡皮擦模式

        self.__lastPos = QPoint(0, 0)
        self.__currentPos = QPoint(0, 0)

        self.__painter = QPainter()

        self.__thickness = 2  # 默认画笔粗细为2px
        self.__penColor = QColor("black")  # 设置默认画笔颜色为黑色
        self.__colorList = QColor.colorNames()  # 获取颜色列表

    def paintEvent(self, paintEvent):
        self.__painter.begin(self)
        self.__painter.drawPixmap(0, 0, self.__board)
        self.__painter.end()

    def setPen(self,penColor,thickness):
        self.__penColor = penColor
        self.__thickness = thickness

    def drawLine(self,startPoint,endPoint):
        self.__painter.begin(self.__board)
        self.__painter.setPen(QPen(self.__penColor, self.__thickness))  # 设置画笔颜色，粗细
        self.__painter.drawLine(startPoint,endPoint)
        self.__painter.end()
        self.update()  # 更新显示

    def clearBoard(self):
        # 清空画板
        self.__board.fill(Qt.white)
        self.update()