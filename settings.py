import settings_design
from PyQt5 import QtWidgets, QtCore
import data_types
from typing import Dict, Tuple


class Settings(QtWidgets.QWidget, settings_design.Ui_Form):

    color_signal = QtCore.pyqtSignal()

    def __init__(self, port_settings: data_types.ComSettings, color_settings: Dict[str, Tuple[int, int, int]]):
        super().__init__()
        self.setupUi(self)
        self.settings = port_settings
        self.colors = color_settings

        databits_group = QtWidgets.QButtonGroup(self)
        databits_group.addButton(self.RBDatabits5)
        databits_group.addButton(self.RBDatabits6)
        databits_group.addButton(self.RBDatabits7)
        databits_group.addButton(self.RBDatabits8)

        parity_group = QtWidgets.QButtonGroup(self)
        parity_group.addButton(self.RBParityEven)
        parity_group.addButton(self.RBParityNone)
        parity_group.addButton(self.RBParityOdd)
        parity_group.addButton(self.RBParitySpace)
        parity_group.addButton(self.RBParityMark)

        stop_bits_group = QtWidgets.QButtonGroup(self)
        stop_bits_group.addButton(self.RBStopbits1)
        stop_bits_group.addButton(self.RBStopbits2)
        stop_bits_group.addButton(self.RBStopbits15)

        hs_group = QtWidgets.QButtonGroup(self)
        hs_group.addButton(self.RBHandNone)
        hs_group.addButton(self.RBHandRts)

        self.databits_dict = {self.RBDatabits5: 5, self.RBDatabits6: 6, self.RBDatabits7: 7, self.RBDatabits8: 8}
        self.parity_dict = {self.RBParityEven: data_types.Parity.EVEN, self.RBParityMark: data_types.Parity.MARK,
                            self.RBParityNone: data_types.Parity.NONE, self.RBParitySpace: data_types.Parity.SPACE,
                            self.RBParityOdd: data_types.Parity.ODD}
        self.stopbits_dict = {self.RBStopbits1: 1, self.RBStopbits2: 2, self.RBStopbits15: 1.5}
        self.hs_dict = {self.RBHandNone: data_types.Handshaking.NONE, self.RBHandRts: data_types.Handshaking.RTSCTS}

        for RB in self.databits_dict.keys():
            RB.clicked.connect(self.databits_changed)
        for RB in self.parity_dict.keys():
            RB.clicked.connect(self.parity_changed)
        for RB in self.stopbits_dict.keys():
            RB.clicked.connect(self.stopbits_changed)
        for RB in self.hs_dict.keys():
            RB.clicked.connect(self.handshaking_changed)
        self.CBEndLine.stateChanged.connect(self.end_string_changed)

        for (RB, databits) in self.databits_dict.items():
            if self.settings.databits == databits:
                RB.setChecked(True)
        for (RB, stopbits) in self.stopbits_dict.items():
            if self.settings.stopbits == stopbits:
                RB.setChecked(True)
        for (RB, hs) in self.hs_dict.items():
            if self.settings.handshaking == hs:
                RB.setChecked(True)
        for (RB, parity) in self.parity_dict.items():
            if self.settings.parity == parity:
                RB.setChecked(True)
        self.CBEndLine.setChecked(self.settings.CRLF)

        self.color_ctrl_dict = {self.BtnBackgroundColor: 'background-color', self.BtnSentColor: 'font-transmit',
                                self.BtnReceivedColor: 'font-receive'}

        for color_btn in self.color_ctrl_dict.keys():
            color_btn.clicked.connect(self.color_changed)

        style_back = "background-color:rgb%s" % str(self.colors['background-color'])
        self.LblBackgroundColor.setStyleSheet(style_back)
        self.LblReceivedColor.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['font-receive']))
        self.LblSentColor.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['font-transmit']))

    def databits_changed(self):
        for RB in self.databits_dict.keys():
            if RB.isChecked():
                self.settings.databits = self.databits_dict[RB]
                print(self.databits_dict[RB])

    def parity_changed(self):
        for RB in self.parity_dict.keys():
            if RB.isChecked():
                self.settings.parity = self.parity_dict[RB]
                print(self.parity_dict[RB])

    def stopbits_changed(self):
        for RB in self.stopbits_dict.keys():
            if RB.isChecked():
                self.settings.stopbits = self.stopbits_dict[RB]
                print(self.stopbits_dict[RB])

    def handshaking_changed(self):
        for RB in self.hs_dict.keys():
            if RB.isChecked():
                self.settings.handshaking = self.hs_dict[RB]
                print(self.hs_dict[RB])

    def end_string_changed(self):
        self.settings.CRLF = self.CBEndLine.isChecked()

    # noinspection PyArgumentList
    def color_changed(self):
        sender = self.sender()
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.colors[self.color_ctrl_dict[sender]] = (color.getRgb()[0], color.getRgb()[1], color.getRgb()[2])
            print(color.getRgb())
            style_back = "background-color:rgb%s" % str(self.colors['background-color'])
            self.LblBackgroundColor.setStyleSheet(style_back)
            self.LblReceivedColor.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['font-receive']))
            self.LblSentColor.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['font-transmit']))

    def closeEvent(self, event):
        self.color_signal.emit()
        event.accept()
