from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QFormLayout, QLabel, QGroupBox, QTextEdit, QRadioButton, QHBoxLayout, QComboBox, QScrollArea, QCalendarWidget
from PyQt5.QtGui import QFont

class Register(QWidget):
    def __init__(self, parent = None):
        super(Register, self).__init__(parent)
        self.initRegistrationUI()

    def initRegistrationUI(self):
        self.setGeometry(525, 225, 900, 600)

        #initialize a scroll area
        self.formScrollArea = QScrollArea(self)

        #iniialize a groupbox
        self.registryformGroupBox = QGroupBox(self)

        #initialize a form layout
        self.registration_form_layout = QFormLayout(self)

        #initialize a horizontal form layout
        self.hboxLayout = QHBoxLayout()  

        #initialize all labels
        self.lastnameLabel = QLabel('Last Name : ', self)
        self.firstnameLabel = QLabel('First Name : ', self)
        self.middlenameLabel = QLabel('Middle Name : ', self)
        self.dobLabel = QLabel('Date of Birth : ', self)
        self.sexLabel = QLabel('Sex : ', self)
        self.addressLabel = QLabel('Address : ', self)
        self.mobileNumberLabel = QLabel('Mobile Number : ', self)
        self.clinicAddressLabel = QLabel('Address of Clinic : ', self)
        self.degreeLabel = QLabel('Degree : ', self)
        self.fieldLabel = QLabel('Field : ', self)
        self.affiliationLabel = QLabel('Affiliation : ', self)

        #initialize all text fields
        self.lastnameEntry = QLineEdit(self)
        self.firstnameEntry = QLineEdit(self)
        self.middlenameEntry = QLineEdit(self)
        self.dobEntry = QCalendarWidget(self)
        self.maleSexEntry = QRadioButton('Male', self)
        self.femaleSexEntry = QRadioButton('Female', self)
        self.addressEntry = QTextEdit(self)
        self.mobileNumberEntry = QLineEdit(self)
        self.clinicAddressEntry = QTextEdit(self)
        self.degreeEntry = QLineEdit(self)
        self.fieldEntry = QLineEdit(self)
        self.affiliationEntry = QLineEdit(self)

        #initialize clear and register buttons
        self.clearButton = QPushButton('Clear', self)
        self.registerButton = QPushButton('Register', self)

        #add the radio buttons to a horizontal box layout
        self.hboxLayout.addWidget(self.maleSexEntry)
        self.hboxLayout.addWidget(self.femaleSexEntry)
        self.hboxLayout.addStretch()

        #add all labels and text areas to the form layout
        self.registration_form_layout.addRow(self.lastnameLabel, self.lastnameEntry)
        self.registration_form_layout.addRow(self.firstnameLabel, self.firstnameEntry)
        self.registration_form_layout.addRow(self.middlenameLabel, self.middlenameEntry)
        self.registration_form_layout.addRow(self.dobLabel, self.dobEntry)

        #add horizontally oriented gender buttons
        self.registration_form_layout.addRow(self.sexLabel, self.hboxLayout)

        #continue adding rows...
        self.registration_form_layout.addRow(self.addressLabel, self.addressEntry)
        self.registration_form_layout.addRow(self.mobileNumberLabel, self.mobileNumberEntry)
        self.registration_form_layout.addRow(self.clinicAddressLabel, self.clinicAddressEntry)
        self.registration_form_layout.addRow(self.degreeLabel, self.degreeEntry)
        self.registration_form_layout.addRow(self.fieldLabel, self.fieldEntry)
        self.registration_form_layout.addRow(self.affiliationLabel, self.affiliationEntry)

        #add all buttons with their respective column spans
        self.registration_form_layout.addRow(self.clearButton)
        self.registration_form_layout.addRow(self.registerButton)

        #create and seta custom font for the form
        newFont = QFont("SansSerif", 11.5)

        #set the layout and font for the groupbox 
        self.registryformGroupBox.setLayout(self.registration_form_layout)
        self.registryformGroupBox.setFont(newFont)

        #set the final layout
        self.formScrollArea.setWidget(self.registryformGroupBox)
        self.formScrollArea.move(250, 0)
        self.formScrollArea.resize(700, 600)



