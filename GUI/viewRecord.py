from PyQt5.QtWidgets import QWidget, QListWidget
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import QUrl

class ViewRecord(QWidget):
    def __init__(self, parent = None):
        super(ViewRecord, self).__init__(parent)
        self.initViewRecordUI()

    def initViewRecordUI(self):
        self.setGeometry(525, 225, 1080, 720)
        
        #initialize a list item widget
        self.listItemWidget = QListWidget(self)
        self.listItemWidget.addItem("Record 1")

        #add widget
        self.listItemWidget.resize(300, 400)
        self.listItemWidget.move(200, 200)