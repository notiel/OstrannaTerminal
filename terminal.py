from PyQt5 import QtWidgets, QtCore, QtSerialPort, QtGui
import sys
import os
from loguru import logger
import terminal_design
import data_types
import common_functions
import settings
import macros
import json
from typing import List, Dict, Tuple, Optional

logger.start("logfile.log", rotation="1 week", format="{time} {level} {message}", level="DEBUG", enqueue=True)


class OstrannaTerminal(QtWidgets.QMainWindow, terminal_design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.serial_port = QtSerialPort.QSerialPort()
        self.port_settings: data_types.ComSettings = data_types.ComSettings()
        self.scan_ports()
        self.all_macros: List[data_types.MacroSet] = list()
        self.current_macros: data_types.MacroSet = data_types.MacroSet(name="", macros=list())
        self.load_macros()
        self.counter: int = 0
        self.settings_form: Optional[settings.Settings] = None
        self.macros_form: Optional[macros.Macros] = None
        self.colors: Dict[str, Tuple[int, int, int]] = \
            {'background-color': (255, 255, 255), 'font-transmit': (00, 102, 51), 'font-receive': (0, 0, 0)}
        self.CBBaudrate.setCurrentText('115200')
        self.serial_port.readyRead.connect(self.read_data)
        self.serial_port.errorOccurred.connect(self.serial_error)
        self.CBBaudrate.currentTextChanged.connect(self.baudrate_changed)

        self.BtnReScan.clicked.connect(self.scan_ports)
        self.BtnConnect.clicked.connect(self.connect)
        self.BtnDisconnect.clicked.connect(self.disconnect)
        self.BtnClear.clicked.connect(self.clear_pressed)
        self.BtnSend.clicked.connect(self.write_data)
        self.BtnBuffer.clicked.connect(self.read_data)
        self.BtnCounter.clicked.connect(self.clear_counter)
        self.BtnSave.clicked.connect(self.save_to_file)
        self.BtnCreateMacros.clicked.connect(self.macros_pressed)
        self.CBMacros.currentTextChanged.connect(self.macros_selected)
        self.TxtTransmit.returnPressed.connect(self.write_data)
        self.actionSettings.setShortcut('Ctrl+S')
        self.actionSettings.triggered.connect(self.settings_pressed)

        plain_font = QtGui.QFont("Consolas", 10)
        self.TxtBuffer.setFont(plain_font)
        self.TxtBuffer.setTextBackgroundColor(QtGui.QColor(*self.colors['background-color']))
        self.TxtBuffer.setTextColor(QtGui.QColor(*self.colors['font-transmit']))

        self.macros_btns_list = [self.BtnMacros1, self.BtnMacros2, self.BtnMacros3, self.BtnMacros4, self.BtnMacros5,
                                 self.BtnMacros6, self.BtnMacros7, self.BtnMacros8, self.BtnMacros9, self.BtnMacros10,
                                 self.BtnMacros11, self.BtnMacros12, self.BtnMacros13, self.BtnMacros14,
                                 self.BtnMacros15, self.BtnMacros16, self.BtnMacros17, self.BtnMacros18,
                                 self.BtnMacros19, self.BtnMacros20]
        for btn in self.macros_btns_list:
            btn.clicked.connect(self.macro_btn_pressed)

    def scan_ports(self):
        """
        scans ports, sets disconnected state UI, selects last port name if any
        :return:
        """
        self.serial_port.close()
        self.CBPorts.clear()
        self.LblStatusInfo.setText('Disconnected')
        self.BtnDisconnect.setEnabled(False)
        # noinspection PyArgumentList
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            if not self.CBSTM.isChecked() or port.manufacturer().startswith('STMicroelectronics'):
                self.CBPorts.addItem("%s: (%s)" % (port.portName(), (port.description())))
        if self.CBPorts.count() > 0:
            self.BtnConnect.setEnabled(True)
        if self.port_settings.last_name:
            for i in range(self.CBPorts.count()):
                if self.CBPorts.itemText(i).startswith(self.port_settings.last_name):
                    self.CBPorts.setCurrentIndex(i)

    def load_macros(self):
        """
        loads macros sets from "macros.json"
        :return:
        """
        if os.path.exists("macros.json"):
            with open("macros.json") as f:
                macros_data = json.load(f)
                self.all_macros, warning = data_types.create_macros_from_list(macros_data['Macros'])
                if warning:
                    self.LblStatus.setText(warning)
                self.CBMacros.addItem('None')
                self.CBMacros.addItems([macrosset.name for macrosset in self.all_macros])

    def connect(self):
        """
        connects to selected port with selected settings, sets connected UI state if success
        :return:
        """
        name: str = self.CBPorts.currentText().split(':')[0]
        self.serial_port.setPortName(name)
        # noinspection PyArgumentList
        self.serial_port.setBaudRate(self.port_settings.baudrate)
        self.serial_port.setDataBits(data_types.databits_dict[self.port_settings.databits])
        self.serial_port.setParity(data_types.parity_dict[self.port_settings.parity])
        self.serial_port.setStopBits(data_types.stopbits_dict[self.port_settings.stopbits])
        if not self.serial_port.open(QtCore.QIODevice.ReadWrite):
            common_functions.error_message("Unable to open port %s" % name)
        else:
            self.LblStatusInfo.setText("Connected")
            self.BtnDisconnect.setEnabled(True)
            self.BtnConnect.setEnabled(False)
            self.port_settings.name = name
            self.port_settings.last_name = name
            self.BtnSend.setEnabled(True)
            self.BtnBuffer.setEnabled(True)

    def disconnect(self):
        """
        disconnects and sets disconnected ui
        :return:
        """
        self.serial_port.close()
        self.LblStatusInfo.setText('Disconnected')
        self.port_settings.name = ""
        self.counter = 0
        self.scan_ports()
        self.BtnSend.setEnabled(False)
        self.BtnBuffer.setEnabled(False)

    def clear_pressed(self):
        """
        clears log
        :return:
        """
        self.TxtBuffer.clear()
        self.LblCounterData.setText("0")
        self.counter = 0

    def baudrate_changed(self):
        """
        change baudrate in settings
        :return:
        """
        if self.CBBaudrate.currentText() != 'Custom':
            self.port_settings.baudrate = int(self.CBBaudrate.currentText())

    def read_data(self):
        """
        reads data from comport
        :return:
        """
        read: str = ""
        try:
            read += self.serial_port.readAll().data().decode('utf-8')
            self.statusbar.clearMessage()
        except UnicodeDecodeError:
            self.statusbar.showMessage("Unicode decode error")

        if read:
            self.TxtBuffer.setTextBackgroundColor(QtGui.QColor(*self.colors['background-color']))
            self.TxtBuffer.setTextColor(QtGui.QColor(*self.colors['font-receive']))
            self.TxtBuffer.insertPlainText(read)
            if self.CBScroll.isChecked():
                scroll = self.TxtBuffer.verticalScrollBar().maximum()
                self.TxtBuffer.verticalScrollBar().setValue(scroll)
            self.counter += len(read)
            self.LblCounterData.setText(str(self.counter))

    def write_data(self):
        """
        writes data to comport
        :return:
        """
        text: str = self.TxtTransmit.text()
        command: bytes = bytes(text+'\r\n', encoding='utf-8') if self.port_settings.CRLF else \
            bytes(text, encoding='utf-8')
        res = self.serial_port.write(command)
        self.serial_port.flush()
        if res != len(command):
            common_functions.error_message('Data was not sent correctly')
        else:
            if self.CBClear.isChecked():
                self.TxtTransmit.clear()
            if self.CBShowSent.isChecked():
                self.TxtBuffer.setStyleSheet("background-color:rgb%s" % str(self.colors['background-color']))
                self.TxtBuffer.setTextBackgroundColor(QtGui.QColor(*self.colors['background-color']))
                self.TxtBuffer.setTextColor(QtGui.QColor(*self.colors['font-transmit']))
                self.TxtBuffer.insertPlainText(text + '\r\n')

    def serial_error(self):
        """
        process error
        :return:
        """
        code = self.serial_port.error()
        if code and self.port_settings.name:
            common_functions.error_message(data_types.error_codes[code])
            self.serial_port.clearError()
            
    def clear_counter(self):
        """
        clear counter
        :return:
        """
        self.LblCounterData.setText('0')
        self.counter = 0

    def save_to_file(self):
        """
        saves log to file
        :return:
        """
        # noinspection PyArgumentList,PyCallByClass
        new_filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save to file...', "")[0]
        if new_filename:
            with open(new_filename, "w") as f:
                f.write(self.TxtBuffer.toPlainText())

    def settings_pressed(self):
        """
        opens settings form
        :return:
        """
        self.settings_form = settings.Settings(self.port_settings, self.colors)
        self.settings_form.show()
        self.settings_form.color_signal.connect(self.back_color_changed)

    def macros_pressed(self):
        """
        opens macros form
        :return:
        """
        self.macros_form = macros.Macros(self.current_macros, self.all_macros)
        self.macros_form.show()
        self.macros_form.edited_signal.connect(self.macros_edited)
        self.macros_form.applied_signal[str].connect(self.macros_applied)

    def macros_edited(self):
        """
        reloads macros list
        :return:
        """
        self.CBMacros.clear()
        self.CBMacros.addItem('None')
        self.CBMacros.addItems([macrosset.name for macrosset in self.all_macros])
        if self.current_macros.name:
            self.CBMacros.setCurrentText(self.current_macros.name)
        else:
            self.CBMacros.setCurrentText('None')

    def macros_applied(self, macros_name: str):
        """
        applies new macros
        :return:
        """
        selected_macros: data_types.MacroSet = \
            [macrosset for macrosset in self.all_macros if macrosset.name == macros_name][0]
        self.current_macros = selected_macros
        self.macros_edited()

    def macros_selected(self):
        """
        selects new macros
        :return:
        """
        selected_macros: Optional[data_types.MacroSet] = \
            data_types.get_macros_by_name(self.CBMacros.currentText(), self.all_macros)
        if selected_macros:
            self.current_macros = selected_macros
            self.LblMacrosSelected.setText("Macros set selected: %s" % selected_macros.name)
            for (index, btn) in enumerate(self.macros_btns_list):
                caption = self.current_macros.macros[index].name if self.current_macros.macros[
                    index].name else '<Not used>'
                btn.setText(caption)
                btn.setEnabled(caption != '<Not used>')
        else:
            self.LblMacrosSelected.setText("Macros set selected: None")
            for (index, btn) in enumerate(self.macros_btns_list):
                btn.setText('M%i' % (index+1))
                btn.setEnabled(False)

    def macro_btn_pressed(self):
        """
        command to send when macro pressed
        :return:
        """
        btn = self.sender()
        self.TxtTransmit.setText(self.current_macros.macros[self.macros_btns_list.index(btn)].command)

    def back_color_changed(self):
        """
        changes TxtBuffer background color
        :return:
        """
        self.TxtBuffer.setStyleSheet("background-color:rgb%s" % str(self.colors['background-color']))


def initiate_exception_logging():
    # generating our hook
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        logger.exception(f"{exctype}, {value}, {traceback}")
        # Call the normal Exception hook after
        # noinspection PyProtectedMember
        sys._excepthook(exctype, value, traceback)
        # sys.exit(1)

    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook


@logger.catch
def main():
    initiate_exception_logging()
    app = QtWidgets.QApplication(sys.argv)
    window = OstrannaTerminal()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
