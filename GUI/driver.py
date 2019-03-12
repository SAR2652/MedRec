from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QStackedWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtCore import pyqtSlot
import sys, os
from hashlib import md5
from urllib.request import urlopen
from urllib.error import URLError
path = '/home/sarvesh/ML_Github/MedRec/'
sys.path.append(path + '/data/')
from diseaselist import DiseaseList
from login import Login
from dashboard import Dashboard
from case_screen import Case
from profile import Profile
from register_user_screen import Register
from register_patient_screen import PatientRegister
from newCaseRecord import NewRecord
from viewRecord import ViewRecord

#define global variables for ease in submitting values
start_widget = None
patient_widget = None
newRecordWidget = None
logged_user = None

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(525, 225, 1080, 720)

        #initialize and set a central widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        #initialize empty common names list
        self.common_names = []

        #initialize empty scientific names list
        self.scientific_names = []

        if os.path.isfile(path + '/data/usercreds.txt'):
            global start_widget
            #initialize a login widget
            start_widget = Login(self)
            start_widget.loginButton.clicked.connect(self.login)
        else:
            start_widget = Register(self)
            start_widget.registerButton.clicked.connect(self.register)

        #make it initial widget
        self.central_widget.addWidget(start_widget)
        self.central_widget.setCurrentWidget(start_widget)

    def login(self):
        global start_widget
        if logged_user is not None:
            user_id = start_widget.user_idLineEdit.text()
            md5sum = md5(start_widget.passwordLineEdit.text().encode())
            encrypted = str(md5sum.digest())
            

        #log in to dashboard
        dashboard = Dashboard(self)
        self.central_widget.addWidget(dashboard)
        self.central_widget.setCurrentWidget(dashboard)

        #define methods to access on clicking buttons
        dashboard.makeRecordEntryButton.clicked.connect(self.chooseCase)
        dashboard.viewProfileButton.clicked.connect(self.viewProfile)
        dashboard.registerPatientButton.clicked.connect(self.register_patient)
        dashboard.viewPatientRecordButton.clicked.connect(self.viewRecord)

    def chooseCase(self):
        #define case
        case_widget = Case(self)
        self.central_widget.addWidget(case_widget)
        self.central_widget.setCurrentWidget(case_widget)

        #methods available
        if case_widget.newCase_choice.isChecked():
            case_widget.recordCreate_button.clicked.connect(lambda : self.createNewCaseRecord(0))
        else:
            case_widget.recordCreate_button.clicked.connect(lambda : self.createNewCaseRecord(1))

    def register_patient(self):

        #define and add patient registry form to the list of widgets
        patient_widget = PatientRegister(self)
        self.central_widget.addWidget(patient_widget)
        self.central_widget.setCurrentWidget(patient_widget)

        #add methods to submit data offline and online
        patient_widget.offlineSubmitButton.clicked.connect(self.savePatientOffline)
        patient_widget.onlineSubmitButton.clicked.connect(self.submitPatientOnline)

    #def savePatientOffline(self):
    #def saveRecord(self):

    #def submitRecordOnline(self)
    def viewProfile(self):
        profile_widget = Profile(self)
        self.central_widget.addWidget(profile_widget)
        self.central_widget.setCurrentWidget(profile_widget)

        #return to dashboard
        profile_widget.backButton.clicked.connect(self.login)
        
    #register a new user
    def register(self):
        global start_widget
        last_name = start_widget.lastnameEntry.text()
        print(last_name)
        first_name = start_widget.firstnameEntry.text()
        middle_name = start_widget.middlenameEntry.text()
        dob = start_widget.dobEntry.selectedDate().toString("yyyy-MM-dd")
        sex = 0 #default
        if start_widget.femaleSexEntry.isChecked():
            sex = 1
        address = start_widget.addressEntry.text()
        clinic_address = start_widget.clinicAddressEntry.text()
        degree = start_widget.degreeEntry.text()
        field = start_widget.fieldEntry.text()
        password = start_widget.passwordEntry().text()
        confpassword = start_widget.confirmpasswordEntry.text()
        #region = 
        #affiliation =

    #create a record for a completely existing case
    def createNewCaseRecord(self, n):
        global newRecordWidget
        newRecordWidget = NewRecord(self)
        self.central_widget.addWidget(newRecordWidget)
        self.central_widget.setCurrentWidget(newRecordWidget)
        #if n == 0:
            #case_widget.

        dl = DiseaseList()
        common_names = dl.generate_common_names_list()
        self.common_names = common_names

        scientific_names = []
        
        #initialize common names list
        newRecordWidget.common_autocomplete.addItems(common_names)

        #nested function to set contents of icd_sub_codes dropdown depending on icd_code selected
        def on_currentIndexChanged(self):
            #empty list
            del scientific_names[:]
            
            #empty combobox
            newRecordWidget.scientific_autocomplete.clear()

            #get index of item in icd_code dropdown
            index = newRecordWidget.common_autocomplete.currentIndex()
            if index == 0:
                newRecordWidget.scientific_autocomplete.setEnabled(False)
            else:
                #enable scientific names box
                newRecordWidget.scientific_autocomplete.setEnabled(True)

                #reference disease name by index
                common_name = common_names[index]
            
                #retrieve ICD Code
                icd_code = common_name.split(' ')[0]

                temp = dl.generate_scientific_names_list(icd_code)
                for item in temp:
                    final = item[0] + ' - ' + item[1] + ' - ' + item[2]
                    scientific_names.append(final)

                newRecordWidget.scientific_autocomplete.addItems(scientific_names)

        #add it to global scientific function
        del self.scientific_names[:]
        self.scientific_names = scientific_names

        #connect to dropdown icd code function
        newRecordWidget.common_autocomplete.currentIndexChanged.connect(on_currentIndexChanged)


    #view saved records
    def viewRecord(self):
        view_record_widget = ViewRecord(self)
        self.central_widget.addWidget(view_record_widget)
        self.central_widget.setCurrentWidget(view_record_widget)

    #check internet connecivity    
    def checkInternetConn(self):
        try:
            urlopen('https://www.google.co.in', timeout = 1)
            return True
        except URLError as err: 
            return False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

