from PyQt5.QtWidgets import *

class CrossRoadPropsWin(QWidget):
    def __init__(self, parent=None):
        super(CrossRoadPropsWin, self).__init__(parent)
        self.resize(1200, 1200)
        self.setStyleSheet("background: white")

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()
