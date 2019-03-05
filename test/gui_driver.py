import sys
path = '/home/sarvesh/ML_Github/MedRec'
sys.path.append(path + '/data/')
sys.path.append(path + '/GUI/')
from autocomplete import DiseaseList
from formwindow import formwindowGUI
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    gui = formwindowGUI()   #instantiate GUI
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



