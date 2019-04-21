from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QStackedWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtCore import pyqtSlot
from datetime import datetime
import sys, os, sqlite3
import requests as req
import json
import urllib.parse as up
from hashlib import md5
from urllib.request import urlopen
from urllib.error import URLError
path = 'C:/MedRec'
sys.path.append(path + '/data/')
sys.path.append(path + '/databases/')
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
host_url = 'http://127.0.0.1:8000/'
start_widget = None
patient_widget = None
newRecordWidget = None
logged_user = None

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(525, 225, 1080, 720)
        title = 'MedRec'
        self.setWindowTitle(title)
        self.conn = sqlite3.connect(path + '/databases/medi_colab.db')

        #initialize and set a central widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        #initialize empty common names list
        self.common_names = []

        #initialize empty scientific names list
        self.scientific_names = []

        if self.checkInternetConn:
            #fetch token from offline database
            token = self.retrieve_token()
            if self.verify_token(token):
                dashboard_widget = Dashboard(self)
                #log in to dashboard
                dashboard = Dashboard(self)
                self.central_widget.addWidget(dashboard)
                self.central_widget.setCurrentWidget(dashboard)

                #define methods to access on clicking buttons
                dashboard.makeRecordEntryButton.clicked.connect(self.chooseCase)
                dashboard.viewProfileButton.clicked.connect(self.viewProfile)
                dashboard.registerPatientButton.clicked.connect(self.register_patient)
                dashboard.viewPatientRecordButton.clicked.connect(self.viewRecord)


            else:
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
    
     #check internet connecivity    
    def checkInternetConn(self):
        try:
            urlopen('https://www.google.co.in', timeout = 1)
            return True
        except URLError as err: 
            return False

    def obtain_token(self, payload):
        data = payload
        ourRequestkaResponse = req.post(
        up.urljoin(host_url, '/api/v1/token-auth/'), data=data)
        response_data = json.loads(ourRequestkaResponse.text)
        print(ourRequestkaResponse.text)
        token = response_data.get('token')
        return token
        #insert into auth_token_data with token value and timestamp

    def retrieve_token(self):
        c = self.conn.cursor()
        c.execute("""SELECT token FROM auth_token_data""")
        op = c.fetchall()[0]
        return op

    def verify_token(self, token):
        data = {
            "token": token
        }
        ourRequestkaResponse = req.post(
        up.urljoin(host_url, '/api/v1/api-token-verify/'), data=data)
        response_data = json.loads(ourRequestkaResponse.text)
        verify_token = response_data.get('token')
        if(verify_token == token):
            print('Token Verified')
            return True
        else:
            print('Token Invalid')
            return False

    

    #register a new user
    def register(self):
        global start_widget
        last_name = start_widget.lastnameEntry.text()
        print(last_name)
        first_name = start_widget.firstnameEntry.text()
        middle_name = start_widget.middlenameEntry.text()
        email = start_widget.emailEntry.text()
        dob = start_widget.dobEntry.selectedDate().toString("yyyy-MM-dd")
        sex = 0 #default
        if start_widget.femaleSexEntry.isChecked():
            sex = 1
        address = start_widget.addressEntry.toPlainText()
        clinic_address = start_widget.clinicAddressEntry.toPlainText()
        degree = start_widget.degreeEntry.text()
        field = start_widget.fieldEntry.text()
        password = start_widget.passwordEntry.text()
        confpassword = start_widget.confpasswordEntry.text()
        if password != confpassword:
            print("Passwords do not match!!!")
        else:
            payload = {
                'first_name': first_name,
                'last_name': last_name,
                'middle_name': middle_name,
                'email': email,
                'password': password,
                #'dob' : dob,
                #'sex' : sex, 
            }

            if self.checkInternetConn():
                ourRequest = req.post(up.urljoin(host_url, 'api/v1/patient_/user/'), data=payload)

                print(ourRequest.text)
                print(ourRequest.status_code)

                #if status code is 201, then perform this logic, else re-register
                response_data = json.loads(ourRequest.text)
                id = response_data.get('id')
                token_payload = {
                    'email' : email,
                    'password' : password,
                }
                token = self.obtain_token(token_payload)
                if self.verify_token(token):
                    #register practitioner
                    Auth_data = "JWT {}".format(token)
                    headers = {
                    'Authorization': Auth_data
                    }  

                    ourRequestkaResponse = req.post(up.urljoin(
                    host_url, '/api/v1/patient_/medical_practitioner/'), headers=headers)

                    response_data = json.loads(ourRequestkaResponse.text)
                    print(ourRequestkaResponse)
                    result = response_data.get('results')
                    c = self.conn.cursor()
                    c.execute("""INSERT INTO auth_token_data(token, created_at) VALUES (?, ?)""", (token, timestamp))

                else:
                    #re-register 
                    dashboard_widget = Dashboard(self)
                    #log in to dashboard
                    dashboard = Dashboard(self)
                    self.central_widget.addWidget(dashboard)
                    self.central_widget.setCurrentWidget(dashboard)

                    #define methods to access on clicking buttons
                    dashboard.makeRecordEntryButton.clicked.connect(self.chooseCase)
                    dashboard.viewProfileButton.clicked.connect(self.viewProfile)
                    dashboard.registerPatientButton.clicked.connect(self.register_patient)
                    dashboard.viewPatientRecordButton.clicked.connect(self.viewRecord)

        #region = 
        #affiliation =

    def login(self):
        global start_widget
        email = start_widget.emailLineEdit.text()
        password = start_widget.passwordLineEdit.text()
        payload = {
            'email' : email,
            'password' : password,
        }

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
    

    #def submitPatientOnline(self)
    def viewProfile(self):
        profile_widget = Profile(self)
        self.central_widget.addWidget(profile_widget)
        self.central_widget.setCurrentWidget(profile_widget)

        #return to dashboard
        profile_widget.backButton.clicked.connect(self.login)

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
        newRecordWidget.saveLocallyandUpload.clicked.connect(self.saveRecord)

    def saveRecord(self):
        global newRecordWidget
        patient_name = newRecordWidget.patient_name_entry.currentText()
        case_name = newRecordWidget.case_name_entry.currentText()
        common_name = newRecordWidget.common_autocomplete.currentText()
        scientific_name = newRecordWidget.scientific_autocomplete.currentText()
        hpc = newRecordWidget.hpc_entry.toPlainText()
        moi = newRecordWidget.moi_entry.text()
        if newRecordWidget.dv_yes.isChecked():
            dv = 1
        else:
            dv = 0
        o_a = newRecordWidget.on_arrival_entry.toPlainText()
        print(o_a)
        diagnosis = newRecordWidget.diagnosis_entry.toPlainText()
        tx = newRecordWidget.Tx_entry.toPlainText()
        report_suggestions_entry = newRecordWidget.report_suggestions_entry.toPlainText()
        medication = newRecordWidget.medication_entry.toPlainText()
        advice = newRecordWidget.advice_entry.toPlainText()
        query = newRecordWidget.query_entry.text()





    #view saved records
    def viewRecord(self):
        view_record_widget = ViewRecord(self)
        self.central_widget.addWidget(view_record_widget)
        self.central_widget.setCurrentWidget(view_record_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

