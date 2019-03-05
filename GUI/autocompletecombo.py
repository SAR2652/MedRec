import sys
from PyQt5.QtWidgets import QComboBox, QCompleter, QApplication, QWidget
from PyQt5.QtCore import QSortFilterProxyModel, Qt 

class autocompleteGUI(QComboBox):
    def __init__(self, parent = None):
        super(autocompleteGUI, self).__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)

        self.setCompleter(self.completer)
        self.resize(700, 30)

        # connect signals
        def filter(text):
            self.pFilterModel.setFilterFixedString(str(text))

        self.lineEdit().textEdited.connect(filter)
        self.completer.activated.connect(self.on_completer_activated)

    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(str(text))
            self.setCurrentIndex(index)

