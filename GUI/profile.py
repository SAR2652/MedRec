from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QIcon
import cv2

class Profile(QWidget):
    def __init__(self, parent = None):
        super(Profile, self).__init__(parent)
        self.initProfileUI()

    def initProfileUI(self):
        self.setGeometry(525, 225, 900, 600)

        #create a central label for profile picture
        self.profilePicture = QLabel(self)

        #enable scaling
        self.profilePicture.setScaledContents(True)

        #create a pixel map for the profile picture
        pixmap = QPixmap('/home/sarvesh/ML_Github/MedRec/data/default-male.png')

        #set the pixmap on the label
        self.profilePicture.setPixmap(pixmap)

        #resize and position image
        self.profilePicture.resize(150, 150)
        self.profilePicture.move(375, 25)

        #create a label for the back button
        self.backButton = QPushButton(self)

        #create and set an icon object
        backIcon = QIcon("/home/sarvesh/ML_Github/MedRec/data/backarrow.jpeg")
        self.backButton.setIcon(backIcon)
        
        #resize and scale icon
        self.backButton.resize(50, 50)



