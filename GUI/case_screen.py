from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox
from PyQt5.QtGui import QFont

class Case(QWidget):
    def __init__(self, parent = None):
        super(Case, self).__init__(parent)
        self.initCaseUI()

    def initCaseUI(self):
        self.setGeometry(525, 225, 900, 600)
        
        #initialize buttons
        self.new_case_button = QPushButton('Create a new case', self)
        self.existing_case_button = QPushButton('Update an existing case', self)

        #define custom font
        customFont = QFont("SansSerif", 19)

        #assign font to buttons
        self.new_case_button.setFont(customFont)
        self.existing_case_button.setFont(customFont)

        #resize the buttons
        self.new_case_button.resize(350, 100)
        self.existing_case_button.resize(350, 100)

        #position buttons
        self.new_case_button.move(340, 240)
        self.existing_case_button.move(340, 380)

