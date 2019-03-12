from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QComboBox, QPushButton
from PyQt5.QtGui import QFont

class Case(QWidget):
    def __init__(self, parent = None):
        super(Case, self).__init__(parent)
        self.initCaseUI()

    def initCaseUI(self):
        self.setGeometry(525, 225, 1080, 720)
        
        #initialize buttons
        self.newCase_choice = QRadioButton('Create a new case', self)
        self.existingCase_choice = QRadioButton('Update an existing case', self)
        self.recordCreate_button = QPushButton('Next', self)

        #define custom font
        customFont = QFont("SansSerif", 19)

        #assign font to buttons
        self.newCase_choice.setFont(customFont)
        self.existingCase_choice.setFont(customFont)
        self.recordCreate_button.setFont(customFont)

        #resize the buttons
        self.newCase_choice.resize(350, 100)
        self.existingCase_choice.resize(350, 100)
        self.recordCreate_button.resize(200, 75)

        #position buttons
        self.newCase_choice.move(340, 240)
        self.existingCase_choice.move(340, 290)
        self.recordCreate_button.move(375, 370)



