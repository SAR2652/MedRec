from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QComboBox, QLineEdit, QTextEdit, QGroupBox, QFormLayout
from autocompletecombo import CommonNameAutocomplete
from PyQt5.QtCore import pyqtSlot 

class NewRecord(QWidget):
    def __init__(self, parent = None):
        super(NewRecord, self).__init__(parent)
        self.initFormRecordUI()

    def initFormRecordUI(self):
        self.setGeometry(525, 225, 900, 600)

        #initialize group box
        #self.formGroupBox = QGroupBox(self)

        #initialize form layout
        #self.formLayout = QFormLayout(self)
        
        #initialize labels
        self.common_name_label = QLabel('Common Disease Name : ', self)
        self.scientific_name_label = QLabel('Scientific Disease Name : ', self)

        #initialize combo boxes
        self.common_autocomplete = CommonNameAutocomplete(self)
        self.scientific_autocomplete = QComboBox(self)

        self.common_autocomplete.resize(700, 30)
        self.scientific_autocomplete.resize(700, 30)

        #position the widgets
        self.common_autocomplete.move(20, 50)
        self.scientific_autocomplete.move(20, 90)
        
