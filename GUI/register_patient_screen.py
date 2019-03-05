from PyQt5.QtWidgets import QWidget,QLineEdit, QLabel, QComboBox, QFormLayout, QTextEdit, QPushButton, QGroupBox, QHBoxLayout, QRadioButton

class PatientRegister(QWidget):
    def __init__(self, parent=None):
        super(PatientRegister, self).__init__(parent)
        self.initPatientRegisterUI()

    def initPatientRegisterUI(self):
        self.setGeometry(150, 150, 1080, 720)

        #initialize a form groupbox
        self.formGroupBox = QGroupBox(self)

        #initialize a form layout
        self.registration_form_layout = QFormLayout(self)

        #initialize a horizontal form layout
        self.hboxLayout = QHBoxLayout()  

        #initialize all labels for patient registry
        self.lastnameLabel = QLabel('Last Name : ', self)
        self.firstnameLabel = QLabel('First Name : ', self)
        self.middlenameLabel = QLabel('Middle Name : ', self)
        self.ageLabel = QLabel('Age : ', self)
        self.sexLabel = QLabel('Sex : ', self)
        self.addressLabel = QLabel('Address : ', self)
        self.occupationLabel = QLabel('Occupation : ', self)
        self.contact_number_1_label = QLabel('Contact Number 1 : ', self)
        self.contact_number_2_label = QLabel('Contact Number 2 : ', self)

        #initialize all fields for patient registry
        self.lastnameEntry = QLineEdit(self)
        self.firstnameEntry = QLineEdit(self)
        self.middlenameEntry = QLineEdit(self)
        self.ageEntry = QLineEdit(self)
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
        self.hboxLayout.addWidget(self.maleSexEntry)
        self.hboxLayout.addWidget(self.femaleSexEntry)
        self.hboxLayout.addStretch()

        #add all labels and text areas to the form layout
        self.registration_form_layout.addRow(self.lastnameLabel, self.lastnameEntry)
        self.registration_form_layout.addRow(self.firstnameLabel, self.firstnameEntry)
        self.registration_form_layout.addRow(self.middlenameLabel, self.middlenameEntry)
        self.registration_form_layout.addRow(self.ageLabel, self.ageEntry)

        #add horizontally oriented gender buttons
        self.registration_form_layout.addRow(self.sexLabel, self.hboxLayout)

        #continue adding rows...
        self.registration_form_layout.addRow(self.addressLabel, self.addressEntry)
        self.registration_form_layout.addRow(self.occupationLabel, self.occupationEntry)
        self.registration_form_layout.addRow(self.contact_number_1_label, self.contact_number_1_entry)
        self.registration_form_layout.addRow(self.contact_number_2_label, self.contact_number_2_entry)

        #add submit button with column span
        self.registration_form_layout.addRow(self.resetButton)
        self.registration_form_layout.addRow(self.offlineSubmitButton)
        self.registration_form_layout.addRow(self.onlineSubmitButton)

        #set the layout for the groupbox and its position
        self.formGroupBox.setLayout(self.registration_form_layout)
        self.formGroupBox.move(300, 50)

