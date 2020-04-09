from PyQt5 import QtWidgets, QtCore, QtSerialPort, QtGui
import sys
from loguru import logger
import terminal_design
import data_types
import common_functions
import settings
import macros

logger.start("logfile.log", rotation="1 week", format="{time} {level} {message}", level="DEBUG", enqueue=True)


class OstrannaTerminal(QtWidgets.QMainWindow, terminal_design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.serial_port = QtSerialPort.QSerialPort()
        self.port_settings = data_types.ComSettings()
        self.scan_ports()
        self.counter = 0
        self.settings_form = None
        self.current_macros = data_types.MacroSet(name="", macros=list())
        self.all_macros = list()
        self.macros_form = None
        self.CBBaudrate.setCurrentText('115200')
        self.serial_port.readyRead.connect(self.read_data)
        self.serial_port.errorOccurred.connect(self.serial_error)
        self.CBBaudrate.currentTextChanged.connect(self.baudrate_changed)
        self.BtnReScan.clicked.connect(self.scan_ports)
        self.BtnConnect.clicked.connect(self.connect)
        self.BtnDisconnect.clicked.connect(self.disconnect)
        self.BtnClear.clicked.connect(self.clear_pressed)
        self.BtnSend.clicked.connect(self.write_data)
        self.BtnCounter.clicked.connect(self.clear_counter)
        self.BtnSave.clicked.connect(self.save_to_file)
        self.BtnCreateMacros.clicked.connect(self.macros_pressed)
        self.CBMacros.currentTextChanged.connect(self.macros_selected)
        self.TxtTransmit.returnPressed.connect(self.write_data)
        self.actionSettings.setShortcut('Ctrl+S')
        self.actionSettings.triggered.connect(self.settings_pressed)
        plain_font = QtGui.QFont("Consolas", 10)
        self.TxtBuffer.setFont(plain_font)
        self.TxtBuffer.setTextColor(QtGui.QColor(0, 0, 0))

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
            print(port.manufacturer())
            if not self.CBSTM.isChecked() or port.manufacturer().startswith('STMicroelectronics'):
                self.CBPorts.addItem("%s: (%s)" % (port.portName(), (port.description())))
        if self.CBPorts.count() > 0:
            self.BtnConnect.setEnabled(True)
        if self.port_settings.last_name:
            for i in range(self.CBPorts.count()):
                if self.CBPorts.itemText(i).startswith(self.port_settings.last_name):
                    self.CBPorts.setCurrentIndex(i)

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

    def disconnect(self):
        """
        disconnects and sets disconnected ui
        :return:
        """
        self.serial_port.close()
        self.LblStatusInfo.setText('Disconnected')
        self.port_settings.name = ""
        self.scan_ports()
        self.BtnSend.setEnabled(False)
        self.counter = 0

    def clear_pressed(self):
        """
        clears log
        :return:
        """
        self.TxtBuffer.clear()
        self.LblCounterData.setText("0")

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
        read = ""
        try:
            read += self.serial_port.readAll().data().decode('utf-8')
        except UnicodeDecodeError:
            pass
        if read:
            self.TxtBuffer.setTextColor(QtGui.QColor(0, 0, 0))
            self.TxtBuffer.insertPlainText(read)
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
        if res != len(command):
            common_functions.error_message('Data was not sent correctly')
        else:
            if self.CBClear.isChecked():
                self.TxtTransmit.clear()
            self.TxtBuffer.setTextColor(QtGui.QColor(0, 255, 0))
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
        self.settings_form = settings.Settings(self.port_settings)
        self.settings_form.show()

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
        self.CBMacros.addItems([macrosset.name for macrosset in self.all_macros])
        if self.current_macros.name:
            self.CBMacros.setCurrentText(self.current_macros.name)

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
        selected_macros = data_types.get_macros_by_name(self.CBMacros.currentText(), self.all_macros)
        if selected_macros:
            self.current_macros = selected_macros


def initiate_exception_logging():
    # generating our hook
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        logger.exception(f"{exctype}, {value}, {traceback}")
        # Call the normal Exception hook after
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
