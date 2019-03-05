import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Initial(QMainWindow):
    def __init__(self, parent = None):
        super(Initial, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        pb = QPushButton('Click here', self)
        pb.move(100, 250)
        self.show()

        pb.clicked.connect(self.changeLayout)

    def changeLayout(self):
        from gui_final import Final
        f = Final()
        f.show()


def main():
    app = QApplication(sys.argv)
    init = Initial()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
