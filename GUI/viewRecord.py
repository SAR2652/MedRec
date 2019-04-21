import sys
from PyQt5.QtWidgets import QWidget, QListWidget, QLabel, QComboBox
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import QUrl
path = 'C:/MedRec'
sys.path.append(path + '/GUI/')
from autocompletecombo import Autocomplete

class ViewRecord(QWidget):
    def __init__(self, parent = None):
        super(ViewRecord, self).__init__(parent)
        self.initViewRecordUI()

    def initViewRecordUI(self):
        self.setGeometry(525, 225, 1080, 720)
        
        #initialize combo box
        self.patient_name_label = QLabel('Patient Name : ', self)
        self.patient_name_entry = Autocomplete(self)
        