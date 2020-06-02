from PyQt5 import QtWidgets, QtCore, QtSerialPort, QtGui
import sys
import os
from loguru import logger
from typing import List, Dict, Tuple, Optional, Union
import datetime
import json
import terminal_design
import data_types
import common_functions
import terminal_graph
import settings
import macros
import ASCII_table
import help
import variables


logger.start("logfile.log", rotation="1 week", format="{time} {level} {message}", level="DEBUG", enqueue=True)


class OstrannaTerminal(QtWidgets.QMainWindow, terminal_design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_connections()
        self.serial_port = QtSerialPort.QSerialPort()
        self.port_settings: data_types.ComSettings = data_types.ComSettings()
        self.text_settings: data_types.TextSettings = data_types.TextSettings()
        self.all_macros: List[data_types.MacroSet] = list()
        self.current_macros: data_types.MacroSet = data_types.MacroSet(name="", macros=list())
        self.load_macros()
        self.counter: int = 0
        self.time_shown = False
        self.tail = ""
        self.count = 0
        self.file_to_send = ""
        self.graph_form = Optional[terminal_graph.MainWindow]
        self.graph = False
        self.start_time = datetime.datetime.now()
        self.settings_form: Optional[settings.Settings] = None
        self.macros_form: Optional[macros.Macros] = None
        self.ascii_form: Optional[ASCII_table.ASCIITable] = None
        self.help_form: Optional[help.Help] = None
        self.var_form: Optional[variables.Variables] = None
        self.current_font = QtGui.QFont("Consolas", 10)
        self.apply_styles()
        self.macros_btns_list = list()
        self.macros_ui()
        self.load_settings()
        self.serial_port_ui()

        self.time1 = 0
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.timerEvent)
        self.time2 = 0
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.timerEvent)
        self.text_repeat1 = ""
        self.text_repeat2 = ""

    def create_connections(self):
        """
        connections created
        :return:
        """
        self.CBBaudrate.activated.connect(self.baudrate_changed)
        self.BtnReScan.clicked.connect(self.scan_ports)
        self.BtnConnect.clicked.connect(self.connect)
        self.BtnDisconnect.clicked.connect(self.disconnect_stub)
        self.CBNRF.stateChanged.connect(self.scan_ports)
        self.CBSTM.stateChanged.connect(self.scan_ports)
        self.BtnClear.clicked.connect(self.clear_pressed)
        self.BtnClear.setShortcut('Esc')
        self.BtnSend.clicked.connect(self.send_clicked)
        self.BtnSend2.clicked.connect(self.send_clicked)
        self.BtnCounter.clicked.connect(self.clear_counter)
        self.BtnSave.clicked.connect(self.save_to_file)
        self.BtnCreateMacros.clicked.connect(self.macros_pressed)
        self.TxtTransmit.returnPressed.connect(self.send_clicked)
        self.TxtTransmit2.returnPressed.connect(self.send_clicked)
        self.BtnSettings.clicked.connect(self.settings_pressed)
        self.BtnFile.clicked.connect(self.select_file)
        self.BtnSendFile.clicked.connect(self.send_file)
        self.BtnAscii.clicked.connect(self.ascii_show)
        self.LineName.textChanged.connect(self.title_changed)
        self.BtnRefresh.clicked.connect(self.refresh_length)
        self.BtnGraph.clicked.connect(self.graph_clicked)
        self.BtnHelp.clicked.connect(self.help_clicked)
        self.BtnVar.clicked.connect(self.var_pressed)
        self.CBRepeat.stateChanged.connect(self.repeat_pressed)
        self.CBRepeat2.stateChanged.connect(self.repeat_pressed)

    def serial_port_ui(self):
        """
        set UI for serial port
        :return:
        """
        self.serial_port.readyRead.connect(self.read_data)
        self.serial_port.errorOccurred.connect(self.serial_error)
        self.CBBaudrate.setCurrentText('115200')
        self.scan_ports()

    def macros_ui(self):
        """
        sets macros ui
        :return:
        """
        self.macros_btns_list = [self.BtnMacros1, self.BtnMacros2, self.BtnMacros3, self.BtnMacros4, self.BtnMacros5,
                                 self.BtnMacros6, self.BtnMacros7, self.BtnMacros8, self.BtnMacros9, self.BtnMacros10,
                                 self.BtnMacros11, self.BtnMacros12, self.BtnMacros13, self.BtnMacros14,
                                 self.BtnMacros15, self.BtnMacros16, self.BtnMacros17, self.BtnMacros18,
                                 self.BtnMacros19, self.BtnMacros20, self.BtnMacros21, self.BtnMacros22,
                                 self.BtnMacros23, self.BtnMacros24, self.BtnMacros25, self.BtnMacros26,
                                 self.BtnMacros27, self.BtnMacros28, self.BtnMacros29, self.BtnMacros30]
        for btn in self.macros_btns_list:
            btn.clicked.connect(self.macro_btn_pressed)
        self.CBMacros.currentTextChanged.connect(self.macros_selected)

    def apply_styles(self):
        """
        apply styles to GUI
        :return:
        """
        # noinspection PyAttributeOutsideInit
        self.colors: Dict[str, Tuple[int, int, int]] = \
            {'background-color': (255, 255, 255), 'font-transmit': (50, 250, 00), 'font-receive': (0, 0, 0),
             'bytes-color': (255, 0, 0)}
        self.TxtBuffer.setFont(self.current_font)
        self.TxtTransmit.setFont(self.current_font)
        self.TxtTransmit2.setFont(self.current_font)
        self.TxtBuffer.setTextBackgroundColor(QtGui.QColor(*self.colors['background-color']))
        self.TxtBuffer.setTextColor(QtGui.QColor(*self.colors['font-transmit']))

    def load_settings(self):
        """
        loads settings from file if any and overwrites default
        :return:
        """
        if os.path.exists("settings.json"):
            with open("settings.json") as f:
                try:
                    settings_json = json.load(f)
                    if 'COM settings' in settings_json.keys():
                        if 'baudrate' in settings_json['COM settings'].keys():
                            self.port_settings.baudrate = settings_json['COM settings']['baudrate']
                            if self.port_settings.baudrate not in data_types.baudrates:
                                self.CBBaudrate.addItem(str(self.port_settings.baudrate))
                            self.CBBaudrate.setCurrentText(str(self.port_settings.baudrate))
                        if 'stopbits' in settings_json['COM settings'].keys():
                            self.port_settings.stopbits = settings_json['COM settings']['stopbits']
                        if 'parity' in settings_json['COM settings'].keys():
                            self.port_settings.parity = data_types.Parity(settings_json['COM settings']['parity'])
                        if 'databits' in settings_json['COM settings'].keys():
                            self.port_settings.databits = settings_json['COM settings']['databits']
                    if 'Text settings' in settings_json.keys():
                        if 'CRLF' in settings_json['Text settings'].keys():
                            self.text_settings.CRLF = settings_json['Text settings']['CRLF']
                        if 'bytecodes' in settings_json['Text settings'].keys():
                            self.text_settings.bytecodes = settings_json['Text settings']['bytecodes']
                        if 'scroll' in settings_json['Text settings'].keys():
                            self.text_settings.scroll = settings_json['Text settings']['scroll']
                        if 'show sent' in settings_json['Text settings'].keys():
                            self.text_settings.show_sent = settings_json['Text settings']['show sent']
                        if 'timestamps' in settings_json['Text settings'].keys():
                            self.text_settings.timestamps = settings_json['Text settings']['timestamps']
                        if 'decode' in settings_json['Text settings'].keys():
                            self.text_settings.decode = settings_json['Text settings']['decode']
                    if 'Filters' in settings_json.keys():
                        if 'STM' in settings_json['Filters'].keys():
                            self.port_settings.STMFilter = settings_json['Filters']['STM']
                            self.CBSTM.setChecked(self.port_settings.STMFilter)
                        if 'NRF' in settings_json['Filters'].keys():
                            self.port_settings.NRFFilter = settings_json['Filters']['NRF']
                            self.CBNRF.setChecked(self.port_settings.NRFFilter)
                    if 'CRC' in settings_json.keys():
                        if 'polynom' in settings_json['CRC'].keys():
                            self.text_settings.crc_poly = settings_json['CRC']['polynom']
                            if 'init value' in settings_json['CRC'].keys():
                                self.text_settings.crc_init = settings_json['CRC']['init value']
                    if 'Colors' in settings_json.keys():
                        if 'background-color' in settings_json['Colors'].keys():
                            self.colors['background-color'] = tuple(settings_json['Colors']['background-color'])
                            self.back_color_changed()
                        if 'font-transmit' in settings_json['Colors'].keys():
                            self.colors['font-transmit'] = tuple(settings_json['Colors']['font-transmit'])
                        if 'font-receive' in settings_json['Colors'].keys():
                            self.colors['font-receive'] = tuple(settings_json['Colors']['font-receive'])
                        if 'bytes-color' in settings_json['Colors'].keys():
                            self.colors['bytes-color'] = tuple(settings_json['Colors']['bytes-color'])
                    if 'Font' in settings_json.keys():
                        font_family = settings_json['Font']['family'] if 'family' in settings_json['Font'].keys() \
                            else 'Consolas'
                        font_size = settings_json['Font']['size'] if 'size' in settings_json['Font'].keys() else 10
                        self.current_font = QtGui.QFont(font_family, font_size)
                        self.TxtBuffer.setFont(self.current_font)
                        self.TxtTransmit.setFont(self.current_font)
                        self.TxtTransmit2.setFont(self.current_font)
                    if 'Macros set' in settings_json.keys():
                        self.current_macros = data_types.get_macros_by_name(settings_json['Macros set'],
                                                                            self.all_macros)
                        if self.current_macros:
                            self.port_settings.last_macros_set = settings_json['Macros set']
                            self.CBMacros.setCurrentText(self.port_settings.last_macros_set)
                except (json.JSONDecodeError, AttributeError, KeyError, ValueError):
                    common_functions.error_message("Settings file is incorrect, default settings used")

    def scan_ports(self):
        """
        scans ports, sets disconnected state UI, selects last port name if any
        :return:
        """
        self.port_settings.STMFilter = self.CBSTM.isChecked()
        self.port_settings.NRFFilter = self.CBNRF.isChecked()
        self.settings_form = settings.Settings(self.port_settings, self.text_settings,
                                               self.colors, self.current_font)
        self.settings_form.save_settings()
        self.CBPorts.clear()
        # noinspection PyArgumentList
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            if self.CBSTM.isChecked():
                if port.manufacturer().lower().startswith('stmicroelectronics'):
                    self.CBPorts.addItem("%s: (%s)" % (port.portName(), (port.description())))
            if self.CBNRF.isChecked():
                if port.manufacturer().lower().startswith('nordic') or port.manufacturer().lower().startswith('segger'):
                    self.CBPorts.addItem("%s: (%s)" % (port.portName(), (port.description())))
            if not self.CBSTM.isChecked() and not self.CBNRF.isChecked():
                self.CBPorts.addItem("%s: (%s)" % (port.portName(), (port.description())))
        if self.CBPorts.count() > 0 and self.port_settings.name == "":
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
                self.CBMacros.clear()
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
            self.start_time = datetime.datetime.now()
            self.LblStatus.setPixmap(QtGui.QPixmap(":/status-conn/icon/status con2.gif"))
            self.BtnDisconnect.setEnabled(True)
            self.BtnConnect.setEnabled(False)
            self.port_settings.name = name
            self.port_settings.last_name = name
            self.BtnSend.setEnabled(True)
            self.BtnSend2.setEnabled(True)
            self.statusbar.clearMessage()
            self.TxtBuffer.clear()
            self.clear_counter()

    def disconnect_stub(self):
        self.disconnect(True)

    def disconnect(self, rescan=True):
        """
        disconnects and sets disconnected ui
        :return:
        """
        self.serial_port.close()
        self.LblStatus.setPixmap(QtGui.QPixmap(":/status-disconn/icon/status discon2.gif"))
        self.BtnDisconnect.setEnabled(False)
        self.port_settings.name = ""
        self.counter = 0
        if rescan:
            self.scan_ports()
        self.BtnSend.setEnabled(False)
        self.BtnSend2.setEnabled(False)

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
        else:
            # noinspection PyCallByClass,PyArgumentList
            text, ok = QtWidgets.QInputDialog.getText(self, 'Custom baudrate', 'Enter baudrate')
            if ok:
                try:
                    new_baudrate: Optional[int] = int(text)
                except ValueError:
                    new_baudrate = None
                if not new_baudrate or new_baudrate <= 0:
                    common_functions.error_message("Baudrate must be positive number")
                else:
                    self.port_settings.baudrate = new_baudrate

    def read_data(self):
        """
        reads data from comport
        :return:
        """
        read: str = ""
        data: bytes = self.serial_port.readAll().data()
        self.TxtBuffer.setTextBackgroundColor(QtGui.QColor(*self.colors['background-color']))
        # decoding block
        try:
            read += data.decode('ascii')
            self.statusbar.clearMessage()
        except UnicodeDecodeError:
            if self.text_settings.decode == 1:
                for byte in data:
                    try:
                        if byte < 128:
                            char = chr(byte)
                            self.TxtBuffer.setTextColor(QtGui.QColor(*self.colors['font-receive']))
                        else:
                            char = '?'
                            self.TxtBuffer.setTextColor(QtGui.QColor(255, 0, 0))
                    except ValueError:
                        char = '?'
                        self.TxtBuffer.setTextColor(QtGui.QColor(255, 0, 0))
                    self.TxtBuffer.insertPlainText(char)
                    self.counter += 1
            if self.text_settings.decode == 2:
                try:
                    read = data.decode('cp1251')
                except UnicodeDecodeError:
                    self.counter += len(data)
            self.statusbar.showMessage("Unicode decode error")

        if read:
            self.TxtBuffer.setTextColor(QtGui.QColor(*self.colors['font-receive']))
            self.counter += len(read)
            # if timestamps
            if self.text_settings.timestamps:
                delta = datetime.datetime.now() - self.start_time
                lines = read.split('\r')
                start = str(delta) + ': ' if not self.time_shown else ""
                if len(lines) == 1 or lines[-1] not in ['', '\n']:
                    self.time_shown = True
                else:
                    self.time_shown = False
                if self.CBHex.isChecked():
                    lines = [common_functions.hexify(line) for line in lines]
                read_to_show = ('\r' + str(delta) + ': ').join(lines) if lines[-1] not in ['', '\n'] else \
                    ('\r' + str(delta) + ': ').join(lines[:-1]) + lines[-1]
                read_to_show = start + read_to_show
            else:
                read_to_show: str = common_functions.hexify(read) if self.CBHex.isChecked() else read.replace("\n", "")
            self.TxtBuffer.insertPlainText(read_to_show)

            if self.graph and self.graph_form:
                lines = (self.tail + read).split('\r')
                logger.debug(lines)
                self.tail = lines[-1]
                # lines = (self.tail + stub[self.count]).split('\r')
                # self.count += 1
                if len(lines) > 1:
                    for line in lines[:-1]:
                        logger.debug(line)
                        if line.strip():
                            try:
                                data_graph = line.strip().split(';')
                                data_x = float(data_graph[0].strip())
                                data_y = [float(value) for value in data_graph[1:] if value.strip()]
                                if self.graph_form.data_x:
                                    self.graph_form.update_plot_data(data_x, data_y)
                                else:
                                    self.graph_form.create_graph(data_x, data_y)
                                    self.graph_form.show()
                            except (ValueError, IndexError):
                                pass
        self.LblCounterData.setText(str(self.counter))
        if self.text_settings.scroll:
            scroll = self.TxtBuffer.verticalScrollBar().maximum()
            self.TxtBuffer.verticalScrollBar().setValue(scroll)

    def send_clicked(self):
        """
        send data to comport
        :return:
        """
        sender = self.sender()
        source = self.TxtTransmit if sender in [self.TxtTransmit, self.BtnSend] else self.TxtTransmit2
        cb_timer = self.CBRepeat if source == self.TxtTransmit else self.CBRepeat2
        text: str = source.text()
        if self.text_settings.CRLF:
            text += '\r\n'
        # timer block
        if cb_timer.isChecked():
            timer = self.timer1 if source == self.TxtTransmit else self.timer2
            if not timer.isActive():
                timeout = int(self.SpinRepeat.value()) if source == self.TxtTransmit else int(self.SpinRepeat2.value())
                timer.start(timeout)
                if source == self.TxtTransmit:
                    self.text_repeat1 = text
                else:
                    self.text_repeat2 = text
        error: int = self.write_data(text, True, self.text_settings.bytecodes)
        if not error:
            if self.CBClear.isChecked():
                source.clear()

    def write_data(self, text: Union[str, bytes], encode=True, hexes=True) -> int:
        """
        writes data to comport
        :param hexes: convert hexes or not
        :param encode: True if we need to encode
        :param text: text to send
        :return: -1 if failed 0 if ok
        """
        commands = common_functions.split_with_bytes(text) if hexes and encode else [text]
        res_command = bytes()
        for command in commands:
            if common_functions.is_byte(command):
                add_command = bytes.fromhex(command[1:]) if encode else command
            else:
                add_command = bytes(command, encoding='utf-8') if encode else command
            res_command += add_command
        res = self.serial_port.write(res_command)
        self.serial_port.flush()
        if res != len(res_command):
            common_functions.error_message('Data was not sent correctly')
            return -1
        if self.text_settings.show_sent and encode:
            self.TxtBuffer.setStyleSheet("background-color:rgb%s" % str(self.colors['background-color']))
            self.TxtBuffer.setTextBackgroundColor(QtGui.QColor(*self.colors['background-color']))
            for command in commands:
                if common_functions.is_byte(command):
                    self.TxtBuffer.setTextColor(QtGui.QColor(*self.colors['bytes-color']))
                else:
                    self.TxtBuffer.setTextColor(QtGui.QColor(*self.colors['font-transmit']))
                command_to_show: str = common_functions.hexify(command) if self.CBHex.isChecked() else command
                self.TxtBuffer.insertPlainText(command_to_show)
                if self.text_settings.scroll:
                    scroll = self.TxtBuffer.verticalScrollBar().maximum()
                    self.TxtBuffer.verticalScrollBar().setValue(scroll)
        return 0

    def serial_error(self):
        """
        process error
        :return:
        """
        # noinspection PyCallingNonCallable
        code = self.serial_port.error()
        if code and self.port_settings.name:
            # common_functions.error_message(data_types.error_codes[code])
            self.statusbar.showMessage(data_types.error_codes[code])
            self.serial_port.clearError()
            self.BtnConnect.setEnabled(True)
            self.disconnect(False)
            
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
        self.settings_form = settings.Settings(self.port_settings, self.text_settings, self.colors, self.current_font)
        self.settings_form.show()
        self.settings_form.color_signal.connect(self.back_color_changed)
        self.settings_form.font_signal[QtGui.QFont].connect(self.font_changed)

    def macros_pressed(self):
        """
        opens macros form
        :return:
        """
        self.macros_form = macros.Macros(self.current_macros, self.all_macros, self.current_font)
        self.load_macros()
        self.CBMacros.setCurrentText(self.current_macros.name)
        self.macros_form.show()
        self.macros_form.edited_signal.connect(self.macros_edited)
        self.macros_form.applied_signal[str].connect(self.macros_applied)
        self.macros_form.send_signal[str].connect(self.send_macros)

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
            self.port_settings.last_macros_set = self.current_macros.name
        else:
            self.CBMacros.setCurrentText('None')
            self.port_settings.last_macros_set = ""

    def macros_applied(self, macros_name: str):
        """
        applies new macros
        :return:
        """
        self.load_macros()
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
            self.port_settings.last_macros_set = selected_macros.name
            self.settings_form = settings.Settings(self.port_settings, self.text_settings,
                                                   self.colors, self.current_font)
            self.settings_form.save_settings()
            for (index, btn) in enumerate(self.macros_btns_list):
                caption = self.current_macros.macros[index].name if self.current_macros.macros[
                    index].name else '<Not used>'
                btn.setText(caption)
                if self.current_macros.macros[index].name:
                    btn.setToolTip(self.current_macros.macros[index].command)
                if self.current_macros.macros[index].icon_path and \
                        os.path.exists(self.current_macros.macros[index].icon_path):
                    icon = QtGui.QIcon(self.current_macros.macros[index].icon_path)
                    btn.setIcon(icon)
                btn.setEnabled(caption != '<Not used>')
        else:
            self.port_settings.last_macros_set = ""
            for (index, btn) in enumerate(self.macros_btns_list):
                btn.setText('M%i' % (index+1))
                btn.setEnabled(False)
                btn.setIcon(QtGui.QIcon())

    def macro_btn_pressed(self):
        """
        command to send when macro pressed
        :return:
        """
        btn = self.sender()
        text_to_send = self.current_macros.macros[self.macros_btns_list.index(btn)].command
        if self.text_settings.CRLF:
            text_to_send += '\r\n'
        self.write_data(text_to_send, True, self.text_settings.bytecodes)

    def send_macros(self, command: str):
        """
        sends command from macros selected on macros form
        :param command:
        :return:
        """
        if self.text_settings.CRLF:
            command += '\r\n'
        self.write_data(command, True, self.text_settings.bytecodes)

    def back_color_changed(self):
        """
        changes TxtBuffer background color
        :return:
        """
        self.TxtBuffer.setStyleSheet("background-color:rgb%s" % str(self.colors['background-color']))

    def font_changed(self, font: QtGui.QFont):
        """
        changes used font to TxtBuffer
        :return:
        """
        self.current_font = font
        self.TxtBuffer.setFont(font)
        self.TxtTransmit.setFont(self.current_font)
        self.TxtTransmit2.setFont(self.current_font)

    def select_file(self):
        """
        selects file for sending
        :return:
        """
        # noinspection PyCallByClass,PyArgumentList
        new_filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file to send...', "")[0]
        if new_filename:
            self.file_to_send = new_filename
            self.LblFile.setText("File: %s" % self.file_to_send)
            self.BtnSendFile.setEnabled(True)
            self.BtnRefresh.setEnabled(True)
            self.refresh_length()

    def send_file(self):
        """
        sends selected file data to serial port
        :return:
        """
        if self.port_settings.name and self.file_to_send:
            if os.path.exists(self.file_to_send) and not os.path.isdir(self.file_to_send):
                with open(self.file_to_send, "rb") as f:
                    data = f.read()
                    self.write_data(data, False, self.text_settings.bytecodes)

    def ascii_show(self):
        """
        shows window with ASCII table
        :return:
        """
        self.ascii_form = ASCII_table.ASCIITable()
        self.ascii_form.show()

    def title_changed(self):
        """
        changes title
        :return:
        """
        title = self.LineName.text()
        if title:
            self.setWindowTitle(self.LineName.text())
        else:
            self.setWindowTitle('Quetima')

    def refresh_length(self):
        """
        recalculates length of selected file
        :return:
        """
        if self.file_to_send and os.path.exists(self.file_to_send):
            self.LblLength.setText("Length: %i" % os.path.getsize(self.file_to_send))
            self.LblCrc.setText("CRC: " + hex(common_functions.calculate_crc16(
                common_functions.get_crc16_table(self.text_settings.crc_poly), open(self.file_to_send, "rb").read(),
                self.text_settings.crc_init)))
        else:
            self.LblLength.setText("Length: None")
            self.LblCrc.setText('Crc: None')

    def graph_clicked(self):
        """
        starts or stops showing graphs
        :return:
        """
        if self.graph:
            self.graph = False
            self.BtnGraph.setText("ShowGraph")
            self.graph_form.destroy()
            self.graph_form = terminal_graph.MainWindow()
        else:
            self.graph = True
            self.BtnGraph.setText("StopGraph")
            self.graph_form = terminal_graph.MainWindow()

    def help_clicked(self):
        """
        help window opened
        :return:
        """
        self.help_form = help.Help()
        self.help_form.show()

    def var_pressed(self):
        """
        var form show
        :return:
        """
        self.var_form = variables.Variables()
        self.var_form.send_signal[str].connect(self.var_signal_send)
        self.var_form.show()

    def var_signal_send(self, command: str):
        """
        send signal from var form
        :return:
        """
        if self.text_settings.CRLF:
            command += '\r\n'
        self.write_data(command, True, False)

    def repeat_pressed(self):
        """
        repeat checkbox pressed
        :return:
        """
        sender = self.sender()
        timer = self.timer1 if sender == self.CBRepeat else self.timer2
        if timer.isActive():
            timer.stop()

    def timerEvent(self):
        """
        send text in serial port by timer
        :return:
        """
        sender = self.sender()
        text_to_send = self.text_repeat1 if sender == self.timer1 else self.text_repeat2
        self.write_data(text_to_send)



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
