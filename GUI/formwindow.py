import sys
path = '/home/sarvesh/ML_Github/MedRec'
sys.path.append(path + '/data/')
sys.path.append(path + '/GUI/')
from autocomplete import DiseaseList
from autocompletecombo import autocompleteGUI
from dropdown import dropdownMenu
from PyQt5.QtWidgets import QMainWindow

class formwindowGUI(QMainWindow):
    def __init__(self, parent = None):
        super(formwindowGUI, self).__init__(parent)
        self.common_names = []
        self.scientific_names = []
        self.dl = DiseaseList()
        self.initUI()

    def initUI(self):
        ac = autocompleteGUI(self)
        dm = dropdownMenu(self)
        #add common names to autocomplete GUI
        self.common_names = self.dl.generate_common_names_list()
        ac.addItems(self.common_names)
        self.setGeometry(150, 150, 1080, 720)
        ac.move(20, 50)
        dm.move(20, 90)
        self.show()

        ac.activated.connect(self.initialize_subdisease_list)

    #connect to generate_scientific_diseases_list in data.autocomplete.DiseaseList
    def initialize_subdisease_list(self, index):
        
        #reference disease name by index
        common_name = self.common_names[index]

        #retrieve ICD Code
        icd_code = common_name.split(' ')[0]

        #if list is not empty, remove all contents
        if not (not self.scientific_names):
            del self.scientific_names[:]

        temp = self.dl.generate_scientific_names_list(icd_code)
        for item in temp:
            final = item[0] + ' - ' + item[1] + ' - ' + item[2]
            self.scientific_names.append(final)
        
        print(self.scientific_names)
        #dm.addItems(self.scientific_names)


    

