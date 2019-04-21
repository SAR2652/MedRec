from PyQt5.QtWidgets import QWidget,QLineEdit, QLabel, QComboBox, QFormLayout, QTextEdit, QPushButton, QGroupBox, QHBoxLayout, QRadioButton, QCheckBox
from PyQt5.QtGui import QFont

class PatientRegister(QWidget):
    def __init__(self, parent=None):
        super(PatientRegister, self).__init__(parent)
        self.initPatientRegisterUI()

    def initPatientRegisterUI(self):
        self.setGeometry(525, 225, 1080, 720)

        #initialize a form groupbox
        self.formGroupBox = QGroupBox(self)

        #initialize a form layout
        self.registration_form_layout = QFormLayout(self)

        #initialize a horizontal form layout
        self.genderhboxlayout = QHBoxLayout()  

        #initialize all labels for patient registry
        self.lastnameLabel = QLabel('Last Name : ', self)
        self.firstnameLabel = QLabel('First Name : ', self)
        self.middlenameLabel = QLabel('Middle Name : ', self)
        self.dobLabel = QLabel('Date of Birth : ', self)
        self.sexLabel = QLabel('Sex : ', self)
        self.addressLabel = QLabel('Address : ', self)
        self.occupationLabel = QLabel('Occupation : ', self)
        self.contact_number_1_label = QLabel('Contact Number 1 : ', self)
        self.contact_number_2_label = QLabel('Contact Number 2 : ', self)
        self.DHx_label = QCheckBox('DHx : ', self)
        self.Ca_label = QCheckBox('Ca : ', self)
        self.IDDM_label = QCheckBox('IDDM : ', self)
        self.NIDDM_label = QCheckBox('NIDDM : ', self)
        self.MI_label = QCheckBox('MI : ', self)
        self.AF_label = QChec('AF : ', self)

        #initialize all fields for patient registry
        self.lastnameEntry = QLineEdit(self)
        self.firstnameEntry = QLineEdit(self)
        self.middlenameEntry = QLineEdit(self)
        self.dobEntry = QLineEdit(self)
        self.maleSexEntry = QRadioButton('Male', self)
        self.femaleSexEntry = QRadioButton('Female', self)
        self.addressEntry = QTextEdit(self)
        self.occupationEntry = QLineEdit(self)
        self.contact_number_1_entry = QLineEdit(self)
        self.contact_number_2_entry = QLineEdit(self)
        
        
        #initialize submit and reset buttons
        self.offlineSubmitButton = QPushButton('Save locally', self)
        self.onlineSubmitButton = QPushButton('Save and upload', self)
        self.resetButton = QPushButton('Reset', self)

        #add the radio buttons to a horizontal box layout
        self.genderhboxlayout.addWidget(self.maleSexEntry)
        self.genderhboxlayout.addWidget(self.femaleSexEntry)
        self.genderhboxlayout.addStretch()

        #add all labels and text areas to the form layout
        self.registration_form_layout.addRow(self.lastnameLabel, self.lastnameEntry)
        self.registration_form_layout.addRow(self.firstnameLabel, self.firstnameEntry)
        self.registration_form_layout.addRow(self.middlenameLabel, self.middlenameEntry)
        self.registration_form_layout.addRow(self.dobLabel, self.dobEntry)

        #add horizontally oriented gender buttons
        self.registration_form_layout.addRow(self.sexLabel, self.hboxLayout)

        #continue adding rows...
        self.registration_form_layout.addRow(self.addressLabel, self.addressEntry)
        self.registration_form_layout.addRow(self.occupationLabel, self.occupationEntry)
        self.registration_form_layout.addRow(self.contact_number_1_label, self.contact_number_1_entry)
        self.registration_form_layout.addRow(self.contact_number_2_label, self.contact_number_2_entry)

        #add all buttons with their respective column spans
        self.registration_form_layout.addRow(self.resetButton)
        self.registration_form_layout.addRow(self.offlineSubmitButton)
        self.registration_form_layout.addRow(self.onlineSubmitButton)

        #create and seta custom font for the form
        newFont = QFont("SansSerif", 11.5)

        #set the layout for the groupbox along with its position
        self.formGroupBox.setLayout(self.registration_form_layout)
        self.formGroupBox.move(250, 0)
        self.formGroupBox.setFont(newFont)

    
    

