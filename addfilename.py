import os
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox

from addname import Ui_AddFileName


class AddFileName(QWidget, Ui_AddFileName):
    def __init__(self):
        super(AddFileName, self).__init__()
        self.setupUi(self)
        self.selectBT.clicked.connect(self.selectFolder)
        self.folderPath = "./"

    def selectFolder(self):
        try:
            self.folderPath = QFileDialog.getExistingDirectory(self, "选取文件夹", self.folderPath)
            self.path.setText(self.folderPath)
            self.eachFolder(self.folderPath)
            QMessageBox.information(self, "温馨提示", "执行成功！", QMessageBox.Yes, QMessageBox.Yes)
        except Exception as err:
            QMessageBox.information(self, "温馨提示", "执行失败！", QMessageBox.Yes, QMessageBox.Yes)

        # 遍历指定目录，显示目录下的所有文件名

    def eachFolder(self, filepath):
        pathDir = os.listdir(filepath)
        print(pathDir)
        for item in pathDir:
            self.folderName = item
            path = os.path.join(self.folderPath, item)
            if os.path.isdir(path):  # 文件夹，遍历其中文件
                self.eachFiles(path)

    def eachFiles(self, folderPath):
        files = os.listdir(folderPath)
        for item in files:
            file = os.path.join(folderPath, item)
            if os.path.isfile(file):
                nameFile = os.path.join(folderPath, self.folderName + item)
                os.rename(file, nameFile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AddFileName()
    win.show()
    sys.exit(app.exec_())
