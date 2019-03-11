from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QComboBox, QLineEdit, QTextEdit, QGroupBox, QFormLayout
from autocompletecombo import Autocomplete
from PyQt5.QtCore import pyqtSlot 

class NewRecord(QWidget):
    def __init__(self, parent = None):
        super(NewRecord, self).__init__(parent)
        self.initFormRecordUI()

    def initFormRecordUI(self):
        self.setGeometry(525, 225, 1080, 720)

        self

        #initialize group box and resize it
        self.formGroupBox = QGroupBox(self)
        self.formGroupBox.resize(1080, 720)
                
        #initialize labels
        self.common_name_label = QLabel('Common Disease Name : ', self)
        self.scientific_name_label = QLabel('Scientific Disease Name : ', self)

        #initialize combo boxes
        self.common_autocomplete = Autocomplete(self)
        self.scientific_autocomplete = QComboBox(self)

        self.common_autocomplete.resize(600, 30)
        self.scientific_autocomplete.resize(600, 30)

        #position the widgets
        self.common_name_label.move(100, 50)
        self.scientific_name_label.move(100, 90)
        self.common_autocomplete.move(250, 50)
        self.scientific_autocomplete.move(250, 90)
        
