from PyQt5.QtWidgets import QPushButton, QWidget
class Dashboard(QWidget):
    def __init__(self, parent = None):
        super(Dashboard, self).__init__(parent)
        self.initDashboardUI()

    def initDashboardUI(self):
        self.setGeometry(525, 225, 900, 600)

        #initialize buttons
        self.makeRecordEntryButton = QPushButton('Enter a new record', self)
        self.viewProfileButton = QPushButton('View Profile', self)
        self.editPrevRecordButton = QPushButton('Edit a record', self)
        self.viewPatientRecordButton = QPushButton('View Patient Records', self)
        self.registerPatientButton = QPushButton('Register Patient', self)

        #position widgets 
        self.makeRecordEntryButton.move(240, 200)
        self.viewProfileButton.move(420, 200)
        self.editPrevRecordButton.move(240, 240)
        self.viewPatientRecordButton.move(420, 240)
        self.registerPatientButton.move(240, 280)