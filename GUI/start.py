import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QStackedLayout

class Start(QMainWindow):
    def __init__(self, parent = None):
        super(Start, self).__init__(parent)
        self.initMainWindowUI()

    def initMainWindowUI(self):
        #set window dimensions
        self.setGeometry(150, 150, 1080, 720)

        #define a central widget for login window
        self.central_wid = QWidget()

        #define a stacked layout
        self.layout_for_widgets = QStackedLayout()
        
        #set title
        self.setWindowTitle("MedRec")

        self.show()

def main():
    app = QApplication(sys.argv)
    start = Start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()