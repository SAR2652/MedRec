from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QStackedWidget
from PyQt5.QtGui import QFont
import sys
from login import Login
from dashboard import Dashboard
from case_screen import Case
from register_patient_screen import PatientRegister

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(150, 150, 1080, 720)

        #initialize and set a central widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        #initialize a login widget
        login_widget = Login(self)
        login_widget.loginButton.clicked.connect(self.login)

        #make it initial widget
        self.central_widget.addWidget(login_widget)
        self.central_widget.setCurrentWidget(login_widget)

    def login(self):
        #log in to dashboard
        dashboard = Dashboard(self)
        self.central_widget.addWidget(dashboard)
        self.central_widget.setCurrentWidget(dashboard)

        #define methods to access on clicking buttons
        dashboard.makeRecordEntryButton.clicked.connect(self.createCase)
        #dashboard.viewProfileButton.clicked.connect(self.viewProfile)
        dashboard.registerPatientButton.clicked.connect(self.register_patient)

    def createCase(self):
        #define case
        case_widget = Case(self)
        self.central_widget.addWidget(case_widget)
        self.central_widget.setCurrentWidget(case_widget)

    def register_patient(self):
        #define and add patient registry form to the list of widgets
        patient_widget = PatientRegister(self)
        self.central_widget.addWidget(patient_widget)
        self.central_widget.setCurrentWidget(patient_widget)
        
        

    #def viewProfile(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


