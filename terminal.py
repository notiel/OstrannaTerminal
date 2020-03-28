from PyQt5 import QtWidgets, QtCore, QtSerialPort
import sys
from loguru import logger
import terminal_design
from data_types import *
import common_functions

logger.start("logfile.log", rotation="1 week", format="{time} {level} {message}", level="DEBUG", enqueue=True)


class OstrannaTerminal(QtWidgets.QMainWindow, terminal_design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.serial_port = QtSerialPort.QSerialPort()
        self.scan_ports()
        self.port_settings = ComSettings()
        self.CBBaudrate.setCurrentText('115200')
        self.serial_port.readyRead.connect(self.read_data)
        self.serial_port.errorOccurred.connect(self.serial_error)
        self.CBBaudrate.currentTextChanged.connect(self.baudrate_changed)
        self.BtnReScan.clicked.connect(self.scan_ports)
        self.BtnConnect.clicked.connect(self.connect)
        self.BtnDisconnect.clicked.connect(self.disconnect)
        self.BtnClear.clicked.connect(self.disconnect)
        self.BtnSend.clicked.connect(self.write_data)

    def scan_ports(self):
        self.serial_port.close()
        self.CBPorts.clear()
        self.LblStatusInfo.setText('Disconnected')
        self.BtnDisconnect.setEnabled(False)
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            print(port.manufacturer())
            if not self.CBSTM.isChecked() or port.manufacturer().startswith('STMicroelectronics'):
                self.CBPorts.addItem("%s: (%s)" % (port.portName(), (port.description())))
        if self.CBPorts.count() > 0:
            self.BtnConnect.setEnabled(True)

    def connect(self):
        name: str = self.CBPorts.currentText().split(':')[0]
        self.serial_port.setPortName(name)
        self.serial_port.setBaudRate(self.port_settings.baudrate)
        if not self.serial_port.open(QtCore.QIODevice.ReadWrite):
            common_functions.error_message("Unable to open port %s" % name)
        else:
            self.LblStatusInfo.setText("Connected")
            self.BtnDisconnect.setEnabled(True)
            self.BtnConnect.setEnabled(False)
            self.port_settings.name = name
            self.BtnSend.setEnabled(True)

    def disconnect(self):
        self.serial_port.close()
        self.LblStatusInfo.setText('Disconnected')
        self.port_settings.name = ""
        self.scan_ports()
        self.BtnSend.setEnabled(False)

    def clear_pressed(self):
        self.TxtBuffer.clear()

    def baudrate_changed(self):
        if self.CBBaudrate.currentText() != 'Custom':
            self.port_settings.baudrate = int(self.CBBaudrate.currentText())

    def read_data(self):
        current: str = self.TxtBuffer.toPlainText()
        current += self.serial_port.readAll().data().decode('utf-8')
        self.TxtBuffer.setPlainText(current)
        self.serial_port.clear()

    def write_data(self):
        text: str = self.TxtTransmit.text()
        command: bytes = bytes(text+'\r\n', encoding='utf-8')
        print(self.serial_port.write(command))
        print(self.serial_port.error())

    def serial_error(self):
        code = self.serial_port.error()
        if code and self.port_settings.name:
            common_functions.error_message(error_codes[code])
            self.serial_port.clearError()


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
