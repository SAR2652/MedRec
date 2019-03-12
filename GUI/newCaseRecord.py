from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QComboBox, QLineEdit, QTextEdit, QGroupBox, QFormLayout, QCheckBox, QHBoxLayout, QRadioButton, QScrollArea
from autocompletecombo import Autocomplete
from PyQt5.QtCore import pyqtSlot 

class NewRecord(QWidget):
    def __init__(self, parent = None):
        super(NewRecord, self).__init__(parent)
        self.initFormRecordUI()

    def initFormRecordUI(self):
        self.setGeometry(525, 225, 1080, 720)

        #initialize a scroll area
        self.scrollArea = QScrollArea(self)
        self.scrollArea.resize(1080, 720)

        #initialize group box and resize it
        self.formGroupBox = QGroupBox(self)
        self.formGroupBox.resize(1080, 720)

        #initialize a form layout
        self.formLayout = QFormLayout(self)
        
        #initialize labels
        self.patient_name_label = QLabel('Patient Name : ', self)
        self.case_name_label = QLabel('Case Name : ', self)
        self.common_name_label = QLabel('Common Disease Name : ', self)
        self.scientific_name_label = QLabel('Scientific Disease Name : ', self)
        self.hpc_label = QLabel('History of Complaint : ', self)
        self.dv_label = QLabel('Diarrhoea & Vomiting : ', self)
        self.moi_label = QLabel('Mechanism of Injury : ', self)
        self.on_arrival_label = QLabel('On Arrival', self)
        self.diagnosis_label = QLabel('Diagnosis : ', self)
        self.Tx_label = QLabel('Specific Treatment : ', self)
        self.report_suggestions_label = QLabel('Report Suggestions : ', self)
        self.medication_label = QLabel('Medication : ', self)
        self.advice_label = QLabel('Advice : ', self)
        self.query_label = QLabel('Query : ', self)

        #initialize all entry fields
        self.patient_name_entry = Autocomplete(self)
        self.case_name_entry = Autocomplete(self)
        #self.common_name_entry = QComboBox(self)
        #self.scientific_name_entry = QComboBox(self)
        self.hpc_entry = QTextEdit(self)

        #generate a horizontal box layout
        self.dv_hbox = QHBoxLayout(self)
        self.dv_yes = QRadioButton('Yes', self)
        self.dv_no = QRadioButton('No', self)
        self.dv_hbox.addWidget(self.dv_yes)
        self.dv_hbox.addWidget(self.dv_no)

        #add further entry fields
        self.moi_entry = QLineEdit(self)
        self.on_arrival_entry = QTextEdit(self)
        self.diagnosis_entry = QTextEdit(self)
        self.Tx_entry = QTextEdit(self)
        self.report_suggestions_entry = QTextEdit(self)
        self.medication_entry = QTextEdit(self)
        self.advice_entry = QTextEdit(self)
        self.query_entry = QLineEdit(self)

        #initialize combo boxes
        self.common_autocomplete = Autocomplete(self)
        self.scientific_autocomplete = QComboBox(self)

        #initialize submit buttons
        self.resetButton = QPushButton('Reset', self)
        self.saveLocally = QPushButton('Save Locally', self)
        self.saveLocallyandUpload = QPushButton('Save Locally and Upload', self)

        #add widgets to the form
        self.formLayout.addRow(self.patient_name_label, self.patient_name_entry)
        self.formLayout.addRow(self.case_name_label, self.case_name_entry)
        self.formLayout.addRow(self.common_name_label, self.common_autocomplete)
        self.formLayout.addRow(self.scientific_name_label,self.scientific_autocomplete)
        self.formLayout.addRow(self.hpc_label, self.hpc_entry)
        self.formLayout.addRow(self.moi_label, self.moi_entry)
        self.formLayout.addRow(self.dv_label, self.dv_hbox)
        self.formLayout.addRow(self.on_arrival_label, self.on_arrival_entry)
        self.formLayout.addRow(self.diagnosis_label, self.diagnosis_entry)
        self.formLayout.addRow(self.Tx_label, self.Tx_entry)
        self.formLayout.addRow(self.report_suggestions_label, self.report_suggestions_entry)
        self.formLayout.addRow(self.medication_label, self.medication_entry)
        self.formLayout.addRow(self.advice_label, self.advice_entry)
        self.formLayout.addRow(self.query_label, self.query_entry)
        self.formLayout.addRow(self.resetButton)
        self.formLayout.addRow(self.saveLocally)
        self.formLayout.addRow(self.saveLocallyandUpload)

        #set layout for group box
        self.formGroupBox.setLayout(self.formLayout)

        #set scrolling
        self.scrollArea.setWidget(self.formGroupBox)
        #self.common_autocomplete.resize(600, 30)
        #self.scientific_autocomplete.resize(600, 30)

        #position the widgets
        #self.common_name_label.move(100, 50)
        #self.scientific_name_label.move(100, 90)
        #self.common_autocomplete.move(270, 50)
        #self.scientific_autocomplete.move(270, 90)
        
