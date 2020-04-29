import ASCII_table_design
from PyQt5 import QtWidgets


class ASCIITable(QtWidgets.QWidget, ASCII_table_design.Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
