import help_design
from PyQt5 import QtWidgets


class Help(QtWidgets.QWidget, help_design.Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
