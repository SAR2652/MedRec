from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton 
from PyQt5.QtGui import QFont, QPixmap

class Login(QWidget):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.initLoginWindowUI()

    def initLoginWindowUI(self):
        #set widget resolution
        self.setGeometry(525, 225, 900, 600)

        #initialize labels
        self.WHOLogo = QLabel(self)
        self.user_idLabel = QLabel('User ID : ', self)
        self.passwordLabel = QLabel('Password : ', self)

        #initialize a pixmap
        pixmap = QPixmap('/home/sarvesh/ML_Github/MedRec/data/who.png')

        #set pixmap
        self.WHOLogo.setPixmap(pixmap)

        #enable scaling
        self.WHOLogo.setScaledContents(True)

        #initialize text areas
        self.user_idLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)

        #set passowrd echomode
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        #initialize login button to switch between widgets
        self.loginButton = QPushButton('Login', self)

        #set font characteristics
        newFont = QFont("SansSerif", 15)
        loginFont = QFont("SansSerif", 13)
        self.user_idLabel.setFont(newFont)
        self.passwordLabel.setFont(newFont)
        self.loginButton.setFont(loginFont)

        #resize labels
        self.user_idLabel.resize(450, 30)
        self.passwordLabel.resize(450, 30)

        #resize text areas
        self.user_idLineEdit.resize(500, 30)
        self.passwordLineEdit.resize(500, 30)

        #resize login button1
        self.loginButton.resize(150, 30)

        #position labels
        self.WHOLogo.move(300, 40)
        self.user_idLabel.move(110, 365)
        self.passwordLabel.move(117, 405)

        #position text areas
        self.user_idLineEdit.move(240, 365)
        self.passwordLineEdit.move(240, 405)

        #position login button
        self.loginButton.move(370, 450)