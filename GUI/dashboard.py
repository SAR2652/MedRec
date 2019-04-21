from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtGui import QFont
class Dashboard(QWidget):
    def __init__(self, parent = None):
        super(Dashboard, self).__init__(parent)
        self.initDashboardUI()

    def initDashboardUI(self):
        self.setGeometry(525, 225, 1080, 720)

        #initialize buttons
        self.makeRecordEntryButton = QPushButton('Enter a new record', self)
        self.viewProfileButton = QPushButton('View Profile', self)
        self.editPrevRecordButton = QPushButton('Edit a record', self)
        self.viewPatientRecordButton = QPushButton('View Patient Records', self)
        self.registerPatientButton = QPushButton('Register Patient', self)

        #define custom font
        customFont = QFont("SansSerif", 16)

        #set custom font
        self.makeRecordEntryButton.setFont(customFont)
        self.viewProfileButton.setFont(customFont)
        self.editPrevRecordButton.setFont(customFont)
        self.viewPatientRecordButton.setFont(customFont)
        self.registerPatientButton.setFont(customFont)

        #resize buttons
        self.makeRecordEntryButton.resize(250, 50)
        self.viewProfileButton.resize(250, 50)
        self.editPrevRecordButton.resize(250, 50)
        self.viewPatientRecordButton.resize(250, 50)
        self.registerPatientButton.resize(250, 50)

        #position widgets 
        self.makeRecordEntryButton.move(230, 200)
        self.viewProfileButton.move(600, 200)
        self.editPrevRecordButton.move(230, 260)
        self.viewPatientRecordButton.move(600, 260)
        self.registerPatientButton.move(230, 320)