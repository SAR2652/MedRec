from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton 
from PyQt5.QtGui import QFont

class Login(QWidget):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.initLoginWindowUI()

    def initLoginWindowUI(self):
        #set widget resolution
        self.setGeometry(150, 150, 1080, 720)

        #initialize labels
        self.usernameLabel = QLabel('Username : ', self)
        self.passwordLabel = QLabel('Password : ', self)

        #initialize text areas
        self.usernameLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)

        #initialize login button to switch between widgets
        self.loginButton = QPushButton('Login', self)

        #set font characteristics
        newFont = QFont("SansSerif", 16)
        loginFont = QFont("SansSerif", 13)
        self.usernameLabel.setFont(newFont)
        self.passwordLabel.setFont(newFont)
        self.loginButton.setFont(loginFont)

        #resize labels
        self.usernameLabel.resize(450, 30)
        self.passwordLabel.resize(450, 30)

        #resize text areas
        self.usernameLineEdit.resize(500, 30)
        self.passwordLineEdit.resize(500, 30)

        #resize login button
        self.loginButton.resize(150, 30)

        #position labels
        self.usernameLabel.move(340, 500)
        self.passwordLabel.move(347, 540)

        #position text areas
        self.usernameLineEdit.move(470, 500)
        self.passwordLineEdit.move(470, 540)

        #position login button
        self.loginButton.move(400, 580)