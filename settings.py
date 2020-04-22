import settings_design
from PyQt5 import QtWidgets, QtCore, QtGui
import data_types
from typing import Dict, Tuple
import json


class Settings(QtWidgets.QWidget, settings_design.Ui_Form):
    color_signal = QtCore.pyqtSignal()
    font_signal = QtCore.pyqtSignal(QtGui.QFont)

    def __init__(self, port_settings: data_types.ComSettings, color_settings: Dict[str, Tuple[int, int, int]],
                 current_font: QtGui.QFont):
        super().__init__()
        self.setupUi(self)
        self.settings = port_settings
        self.colors = color_settings
        self.current_font = current_font
        self.databits_dict, self.parity_dict, self.stopbits_dict, self.hs_dict = dict(), dict(), dict(), dict()
        self.create_port_dicts()
        self.create_groups()
        self.CBEndLine.stateChanged.connect(self.end_string_changed)
        self.CBBytes.stateChanged.connect(self.bytecodes_changed)
        self.BtnFont.clicked.connect(self.font_changed)
        self.create_rb_connections()
        self.apply_port_settings()
        self.color_ctrl_dict = dict()
        self.apply_color_font_settings()

    def create_port_dicts(self):
        """
        creates dicts to map our port settings constants and PyQt
        :return:
        """
        self.databits_dict = {self.RBDatabits5: 5, self.RBDatabits6: 6, self.RBDatabits7: 7, self.RBDatabits8: 8}
        self.parity_dict = {self.RBParityEven: data_types.Parity.EVEN, self.RBParityMark: data_types.Parity.MARK,
                            self.RBParityNone: data_types.Parity.NONE, self.RBParitySpace: data_types.Parity.SPACE,
                            self.RBParityOdd: data_types.Parity.ODD}
        self.stopbits_dict = {self.RBStopbits1: 1, self.RBStopbits2: 2, self.RBStopbits15: 1.5}
        self.hs_dict = {self.RBHandNone: data_types.Handshaking.NONE, self.RBHandRts: data_types.Handshaking.RTSCTS}

    def create_groups(self):
        """
        groups radiobuttons
        :return:
        """
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

    def create_rb_connections(self):
        """
        connects radiobuttons to functions
        :return:
        """
        for RB in self.databits_dict.keys():
            RB.clicked.connect(self.databits_changed)
        for RB in self.parity_dict.keys():
            RB.clicked.connect(self.parity_changed)
        for RB in self.stopbits_dict.keys():
            RB.clicked.connect(self.stopbits_changed)
        for RB in self.hs_dict.keys():
            RB.clicked.connect(self.handshaking_changed)

    def apply_port_settings(self):
        """
        applies port settings to gui
        :return:
        """
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
        self.CBBytes.setChecked(self.settings.bytecodes)

    def apply_color_font_settings(self):
        """
        applies color settins to GUI
        :return:
        """
        self.color_ctrl_dict = {self.BtnBackgroundColor: 'background-color', self.BtnSentColor: 'font-transmit',
                                self.BtnReceivedColor: 'font-receive', self.BtnColorByte: 'bytes-color'}

        for color_btn in self.color_ctrl_dict.keys():
            color_btn.clicked.connect(self.color_changed)

        style_back = "background-color:rgb%s" % str(self.colors['background-color'])
        self.LblBackgroundColor.setStyleSheet(style_back)
        self.LblReceivedColor.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['font-receive']))
        self.LblSentColor.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['font-transmit']))
        self.LblColorByte.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['bytes-color']))
        self.LblReceivedColor.setFont(self.current_font)
        self.LblSentColor.setFont(self.current_font)
        self.LblFont.setFont(self.current_font)
        self.LblColorByte.setFont(self.current_font)

    def databits_changed(self):
        """
        changes databits setting to selected
        :return:
        """
        for RB in self.databits_dict.keys():
            if RB.isChecked():
                self.settings.databits = self.databits_dict[RB]

    def parity_changed(self):
        """
        changes parity to selected
        :return:
        """
        for RB in self.parity_dict.keys():
            if RB.isChecked():
                self.settings.parity = self.parity_dict[RB]

    def stopbits_changed(self):
        """
        changes stopbits setting to selected
        :return:
        """
        for RB in self.stopbits_dict.keys():
            if RB.isChecked():
                self.settings.stopbits = self.stopbits_dict[RB]

    def handshaking_changed(self):
        """
        sets handshaking setting as selected
        :return:
        """
        for RB in self.hs_dict.keys():
            if RB.isChecked():
                self.settings.handshaking = self.hs_dict[RB]

    def end_string_changed(self):
        """
        change end string settings as selected
        :return:
        """
        self.settings.CRLF = self.CBEndLine.isChecked()

    def bytecodes_changed(self):
        """
        change bytecode setting as selected
        :return:
        """
        self.settings.bytecodes = self.CBBytes.isChecked()

    # noinspection PyArgumentList
    def color_changed(self):
        """
        applies all color changes to settings and UI examples
        :return:
        """
        sender = self.sender()
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.colors[self.color_ctrl_dict[sender]] = (color.getRgb()[0], color.getRgb()[1], color.getRgb()[2])
            style_back = "background-color:rgb%s" % str(self.colors['background-color'])
            self.LblBackgroundColor.setStyleSheet(style_back)
            self.LblReceivedColor.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['font-receive']))
            self.LblSentColor.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['font-transmit']))
            self.LblColorByte.setStyleSheet(style_back + '; color:rgb%s' % str(self.colors['bytes-color']))
            
    def font_changed(self):
        """
        applies font changes to settings and examples
        :return:
        """
        # noinspection PyCallByClass
        font, ok = QtWidgets.QFontDialog.getFont(self.current_font)
        if ok:
            self.current_font = font
            self.LblReceivedColor.setFont(font)
            self.LblSentColor.setFont(font)
            self.LblFont.setFont(font)
            self.LblColorByte.setFont(font)
            self.font_signal.emit(font)

    def closeEvent(self, event):
        """
        saves settings to settings.json before exit
        :param event:
        :return:
        """
        self.color_signal.emit()
        settings_save = {'COM settings': {'baudrate': self.settings.baudrate, 'databits': self.settings.databits,
                                          'parity': self.settings.parity.value, 'stopbits': self.settings.stopbits},
                         'CRLF': self.settings.CRLF, 'bytecodes': self.settings.bytecodes, 'Colors': self.colors,
                         'Font': {'family': self.current_font.family(), 'size': self.current_font.pointSize()}}
        with open("Settings.json", "w") as f:
            f.write(json.dumps(settings_save, indent=4))
        event.accept()
