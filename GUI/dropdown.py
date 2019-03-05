from PyQt5.QtWidgets import QComboBox

class dropdownMenu(QComboBox):
    def __init__(self, parent = None):
        super(dropdownMenu, self).__init__(parent)
        self.resize(700, 30)
        self.show()
