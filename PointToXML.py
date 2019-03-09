import os
import re
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QMessageBox
from PyQt5.uic.properties import QtCore
from lxml import etree

from ptoxml import Ui_PointToXML


class PointToXML(QWidget, Ui_PointToXML):
    def __init__(self):
        super(PointToXML, self).__init__()
        self.setupUi(self)
        self.xmlDic = {}
        self.setWindowTitle("点文件生成XML工具")
        self.openBT.clicked.connect(self.openFolderAction)
        self.show()
        self.folderPath = "./"

    def openFolderAction(self):
        # self.openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', "All Files (*);;Text Files (*.txt);xyz Files (*.xyz)")
        # print(self.openfile_name)
        self.folderPath = QFileDialog.getExistingDirectory(self, "选取文件夹", self.folderPath)
        self.pathLE.setText(self.folderPath)
        self.eachFile(self.folderPath)
        # print(self.folderPath)

    # 遍历指定目录，显示目录下的所有文件名
    def eachFile(self, filepath):
        pathDir = os.listdir(filepath)
        for allDir in pathDir:
            id = allDir.split(".")[0]
            child = os.path.join('%s\%s' % (filepath, allDir))
            if os.path.isfile(child):
                print(child, id)
                self.getDicList(child, id)
                # for line in open(child):
                #     print(line)

        print(self.xmlDic)
        self.createXML()

    def getDicList(self, child, id):
        list = []

        for line in open(child):
            xyzList = line.strip("\n").split(" ")
            list.append({"x": xyzList[0], "y": xyzList[1], "z": xyzList[2]})
        self.xmlDic[id] = list

    def createXML(self):
        try:
            # parser = etree.XMLParser(remove_blank_text=True)
            # xml = etree.parse('yf_sample_data.xml', parser)

            self.root = etree.Element("OpenDriveData")
            for k, v in self.xmlDic.items():
                print(k, v)
                road = etree.SubElement(self.root, 'road')
                road.set("id", k)
                road.set("name", "")
                road.set("pretype", "junction")
                road.set("pre", "none")
                road.set("suctype", "road")
                road.set("suc", "999")
                planView = etree.SubElement(road, "planView")
                for positionItem in v:
                    position = etree.SubElement(planView, "position")
                    position.set("x", positionItem.get("x"))
                    position.set("y", positionItem.get("y"))
                    position.set("z", positionItem.get("z"))

                lanes = etree.SubElement(road, "lanes")
                section = etree.SubElement(lanes, "section")
                section.set("s", "0")
                objects = etree.SubElement(road, "objects")

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
            print('生成xml OK!')
            QMessageBox.information(self, "温馨提示", "生成xml成功！", QMessageBox.Yes, QMessageBox.Yes)
            # self.close()
        except Exception as err:
            print('错误信息：{0}'.format(err))
            QMessageBox.information(self, "温馨提示", "生成xml失败！", QMessageBox.Yes, QMessageBox.Yes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    arr = []

    ex = PointToXML()
    sys.exit(app.exec_())
