import sys
from PyQt5.QtWidgets import QLabel, QMainWindow
from gui_initial import Initial

class Final(object):
    def __init__(self, Initial):
        self.initUI()

    def initUI(self):
        l1 = QLabel(self)
        l1.move(100, 200)
        l1.setText("Hello")