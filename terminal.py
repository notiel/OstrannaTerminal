from PyQt5 import QtWidgets, QtCore, QtSerialPort, QtGui
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
        self.port_settings = ComSettings()
        self.scan_ports()
        self.counter = 0
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
        self.TxtTransmit.returnPressed.connect(self.write_data)
        plain_font = QtGui.QFont("Consolas", 10)
        self.TxtBuffer.setFont(plain_font)
        self.TxtBuffer.setTextColor(QtGui.QColor(0, 0, 0))

    def scan_ports(self):
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
        name: str = self.CBPorts.currentText().split(':')[0]
        self.serial_port.setPortName(name)
        # noinspection PyArgumentList
        self.serial_port.setBaudRate(self.port_settings.baudrate)
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
        self.serial_port.close()
        self.LblStatusInfo.setText('Disconnected')
        self.port_settings.name = ""
        self.scan_ports()
        self.BtnSend.setEnabled(False)
        self.counter = 0

    def clear_pressed(self):
        self.TxtBuffer.clear()

    def baudrate_changed(self):
        if self.CBBaudrate.currentText() != 'Custom':
            self.port_settings.baudrate = int(self.CBBaudrate.currentText())

    def read_data(self):
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
        text: str = self.TxtTransmit.text()
        command: bytes = bytes(text+'\r\n', encoding='utf-8')
        res = self.serial_port.write(command)
        if res != len(command):
            common_functions.error_message('Data was not sent correctly')
        else:
            if self.CBClear.isChecked():
                self.TxtTransmit.clear()
            # current: str = self.TxtBuffer.toHtml()
            # current += (template_p_start_coloured + (text + '\r\n') + template_p_end + template_end)
            # self.TxtBuffer.setHtml(current)
            self.TxtBuffer.setTextColor(QtGui.QColor(0, 255, 0))
            self.TxtBuffer.insertPlainText(text + '\r\n')

    def serial_error(self):
        code = self.serial_port.error()
        if code and self.port_settings.name:
            common_functions.error_message(error_codes[code])
            self.serial_port.clearError()
            
    def clear_counter(self):
        self.LblCounterData.setText('0')
        self.counter = 0

    def save_to_file(self):
        # noinspection PyArgumentList,PyCallByClass
        new_filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save to file...', "")[0]
        if new_filename:
            with open(new_filename, "w") as f:
                f.write(self.TxtBuffer.toPlainText())


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
