import unittest
import terminal
import data_types
from PyQt5 import QtWidgets, QtGui
import sys
import time
import datetime
import common_functions


class TestLoadSettings(unittest.TestCase):

    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()
        self.terminal_example.load_settings("Settings_for_test.json")

    def testComSettings(self):
        right_settings = data_types.ComSettings(name="", last_name="", baudrate=9100, databits=5,
                                                parity=data_types.Parity.MARK, stopbits=2,
                                                handshaking=data_types.Handshaking.NONE, last_macros_set="test2",
                                                STMFilter=False, NRFFilter=True)
        self.assertEqual(self.terminal_example.port_settings, right_settings)
        self.assertFalse(self.terminal_example.CBSTM.isChecked())
        self.assertTrue(self.terminal_example.CBNRF.isChecked())

    def testTextSettings(self):
        right_settings = data_types.TextSettings(CRLF=False, bytecodes=False, scroll=False, timestamps=False,
                                                 show_sent=False, decode=1, crc_poly=1234, crc_init=1024,
                                                 first_transmit="test1", second_transmit="test2", clear=False,
                                                 first_repeat=True, second_repeat=True, first_period=2000,
                                                 second_period=3000)
        self.assertEqual(self.terminal_example.text_settings, right_settings)

    def testColorSettinsgs(self):
        colors = {'background-color': (100, 100, 100), 'font-transmit': (255, 0, 100), 'font-receive': (0, 100, 255),
                  'bytes-color': (24, 255, 21)}
        self.assertEqual(self.terminal_example.colors, colors)

    def testFontSettings(self):
        current_font = QtGui.QFont("Arial", 14)
        self.assertEqual(self.terminal_example.current_font, current_font)

    def testMacrosLoad(self):
        self.terminal_example.load_macros("Macros_test.json")
        self.assertEqual(len(self.terminal_example.all_macros), 2)
        self.assertEqual(self.terminal_example.all_macros[1].name, "locket")
        self.assertEqual(self.terminal_example.all_macros[0].macros[2].name, "3")
        self.assertEqual(self.terminal_example.all_macros[1].macros[1].command, "setid 5")
        self.assertEqual(self.terminal_example.all_macros[1].macros[0].icon_path,
                         r'C:/Users/juice/Downloads/PycharmProjects/OstrannaTerminal/icon/conn.ico')
        self.assertEqual(self.terminal_example.all_macros[0].macros[5], data_types.Macro("", "", ""))

    def tearDown(self):
        self.terminal_example.destroy()
        self.app.quit()


class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()

    def testScanPorts(self):
        self.terminal_example.CBSTM.setChecked(False)
        self.terminal_example.CBNRF.setChecked(False)
        self.terminal_example.scan_ports()
        self.assertGreater(self.terminal_example.CBPorts.count(), 0)
        self.assertIn('COM3', self.terminal_example.CBPorts.currentText())

    def testConnectAndDisconnect(self):
        self.terminal_example.disconnect()
        self.terminal_example.CBSTM.setChecked(False)
        self.terminal_example.CBNRF.setChecked(False)
        self.terminal_example.CBPorts.setCurrentIndex(1)
        self.terminal_example.BtnConnect.click()
        self.assertTrue(self.terminal_example.BtnDisconnect.isEnabled())
        self.assertEqual(self.terminal_example.port_settings.name, 'COM22')
        self.terminal_example.BtnDisconnect.click()
        self.assertTrue(self.terminal_example.BtnConnect.isEnabled())
        self.assertEqual(self.terminal_example.port_settings.name, '')

    def testSendCommandAndReceiveAnswer(self):
        self.terminal_example.CBPorts.setCurrentIndex(1)
        self.terminal_example.BtnConnect.click()
        self.terminal_example.text_settings.CRLF = True
        self.terminal_example.TxtTransmit.setText('Ping')
        self.terminal_example.TxtBuffer.clear()
        self.terminal_example.BtnSend.click()
        self.terminal_example.serial_port.waitForReadyRead(1000)
        self.assertIn("Ack 0", self.terminal_example.TxtBuffer.toPlainText())
        self.terminal_example.BtnDisconnect.click()

    def tearDown(self):
        self.terminal_example.destroy()
        self.app.quit()


class TestMainUI(unittest.TestCase):

    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()

    def testClearButton(self):
        self.terminal_example.TxtBuffer.setPlainText("Котики")
        self.terminal_example.count = 6
        self.terminal_example.BtnClear.click()
        self.assertEqual(self.terminal_example.counter, 0)
        self.assertEqual(self.terminal_example.TxtBuffer.toPlainText(), "")

    def testBaudrateChange(self):
        self.terminal_example.CBBaudrate.setCurrentIndex(2)
        self.assertEqual(self.terminal_example.port_settings.baudrate, 256000)

    def testTitle(self):
        self.terminal_example.LineName.setText("My new terminal")
        self.assertEqual(self.terminal_example.windowTitle(), "My new terminal")

    def testChangeFont(self):
        new_font = QtGui.QFont("Arial", 12)
        self.terminal_example.font_changed(new_font)
        self.assertEqual(self.terminal_example.TxtBuffer.currentFont(), new_font)
        self.assertEqual(self.terminal_example.TxtTransmit.font(), new_font)
        self.assertEqual(self.terminal_example.TxtTransmit2.font(), new_font)

    def tearDown(self):
        self.terminal_example.destroy()
        self.app.quit()


class TestSubForm(unittest.TestCase):

    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()

    def testSettings(self):
        self.terminal_example.BtnSettings.click()
        self.assertIsNotNone(self.terminal_example.settings_form)
        self.terminal_example.settings_form.destroy()

    def testHelp(self):
        self.terminal_example.BtnHelp.click()
        self.assertIsNotNone(self.terminal_example.help_form)
        self.terminal_example.help_form.destroy()

    def testMacros(self):
        self.terminal_example.BtnCreateMacros.click()
        self.assertIsNotNone(self.terminal_example.macros_form)
        self.terminal_example.macros_form.destroy()

    def testVariables(self):
        self.terminal_example.BtnVar.click()
        self.assertIsNotNone(self.terminal_example.var_form)
        self.terminal_example.var_form.destroy()

    def testASCII(self):
        self.terminal_example.BtnAscii.click()
        self.assertIsNotNone(self.terminal_example.ascii_form)
        self.terminal_example.ascii_form.destroy()

    def tearDown(self):
        self.terminal_example.destroy()
        self.app.quit()


class TestFiles(unittest.TestCase):

    def setUp(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()
        self.terminal_example.file_to_send = \
            r'C:\Users\juice\Downloads\PycharmProjects\OstrannaTerminal\Ostranna_Logo.ico'

    def testRefresh(self):
        self.terminal_example.file_to_send = \
            r'C:\Users\juice\Downloads\PycharmProjects\OstrannaTerminal\Ostranna_Logo.ico'
        self.terminal_example.text_settings.crc_poly = 4129
        self.terminal_example.text_settings.crc_init = 0
        self.terminal_example.BtnRefresh.setEnabled(True)
        self.terminal_example.BtnRefresh.click()
        self.assertEqual(self.terminal_example.LblCrc.text(), "CRC: 0x9e02")
        self.assertEqual(self.terminal_example.LblLength.text(), "Length: 69235\n            10e73")
        self.assertEqual(self.terminal_example.var_form.var_dict['length'], "69235")
        self.assertEqual(self.terminal_example.var_form.var_dict['crc'], '0x9e02')
        self.assertTrue(self.terminal_example.var_form.var_dict['filedata'])

    def testSendFile(self):
        self.terminal_example.CBSTM.setChecked(False)
        self.terminal_example.CBNRF.setChecked(False)
        self.terminal_example.CBPorts.setCurrentIndex(1)
        self.terminal_example.BtnConnect.click()
        self.terminal_example.BtnSendFile.setEnabled(True)
        self.terminal_example.BtnSendFile.click()
        self.assertEqual(self.terminal_example.statusbar.currentMessage(), "File sent")
        self.terminal_example.serial_port.waitForReadyRead(1000)
        self.terminal_example.TxtBuffer.clear()
        self.terminal_example.BtnDisconnect.click()

    '''def testSendFileAndCommand(self):
        self.terminal_example.CBSTM.setChecked(False)
        self.terminal_example.CBNRF.setChecked(False)
        self.terminal_example.CBPorts.setCurrentIndex(1)
        self.terminal_example.BtnConnect.click()
        self.terminal_example.BtnSendFile.setEnabled(True)
        self.terminal_example.BtnSendFile.click()
        self.assertEqual(self.terminal_example.statusbar.currentMessage(), "File sent")
        self.terminal_example.serial_port.waitForReadyRead(1000)
        self.terminal_example.TxtBuffer.clear()
        time.sleep(1)
        self.terminal_example.text_settings.CRLF = True
        self.terminal_example.TxtTransmit.setText('Ping')
        self.terminal_example.TxtBuffer.clear()
        self.terminal_example.text_settings.show_sent = True
        self.terminal_example.BtnSend.click()
        self.assertIn("Ping", self.terminal_example.TxtBuffer.toPlainText())
        self.terminal_example.BtnDisconnect.click()'''

    def tearDown(self):
        self.terminal_example.destroy()
        self.app.quit()


class TestMacroses(unittest.TestCase):

    def setUp(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()
        self.terminal_example.load_macros("Macros_test.json")

    def testSendMacros(self):
        self.terminal_example.CBSTM.setChecked(False)
        self.terminal_example.CBNRF.setChecked(False)
        self.terminal_example.text_settings.CRLF = True
        self.terminal_example.text_settings.show_sent = True
        self.terminal_example.CBPorts.setCurrentIndex(1)
        self.terminal_example.BtnConnect.click()
        self.terminal_example.CBMacros.setCurrentText('locket')
        self.terminal_example.BtnMacros2.click()
        self.assertIn('setid 5', self.terminal_example.TxtBuffer.toPlainText())
        self.terminal_example.TxtBuffer.clear()

    def testMacrosChanged(self):
        self.terminal_example.CBMacros.setCurrentText("test2")
        self.assertEqual(self.terminal_example.BtnMacros1.text(), '1')
        self.terminal_example.CBMacros.setCurrentText("locket")
        self.assertEqual(self.terminal_example.BtnMacros1.text(), 'ping')

    def testUnavailableBtn(self):
        self.terminal_example.CBMacros.setCurrentText("test2")
        self.assertEqual(self.terminal_example.BtnMacros4.text(), '<Not used>')
        self.assertFalse(self.terminal_example.BtnMacros4.isEnabled())

    def testTooltipMacros(self):
        self.terminal_example.CBMacros.setCurrentText("locket")
        self.assertEqual(self.terminal_example.BtnMacros2.toolTip(), 'setid 5')

    def testMacroFormButton(self):
        self.terminal_example.BtnCreateMacros.click()
        self.terminal_example.macros_form.show()
        self.terminal_example.text_settings.show_sent = True
        self.terminal_example.CBPorts.setCurrentIndex(1)
        self.terminal_example.BtnConnect.click()
        self.terminal_example.macros_form.CBMacros.setCurrentText("locket")
        self.terminal_example.macros_form.BtnSend2.click()
        self.assertIn("setid 5", self.terminal_example.TxtBuffer.toPlainText())

    def tearDown(self):
        self.terminal_example.destroy()
        self.app.quit()


class testCommonFunctions(unittest.TestCase):

    def testSplitWithBytesSimple(self):
        teststr1 = "qwer$1Aqwer"
        expected = ["qwer", "$1A", "qwer"]
        self.assertEqual(common_functions.split_with_bytes(teststr1), expected)

    def testSplitWithBytesTwice(self):
        teststr2 = "$1Aqwer$23"
        expected = ["", "$1A", "qwer", "$23", ""]
        self.assertEqual(common_functions.split_with_bytes(teststr2), expected)

    def testSplitWithBytesNo(self):
        teststr3 = "&12qwer$1qwer"
        self.assertEqual(common_functions.split_with_bytes(teststr3), [teststr3])

    def testIsByteFalse1(self):
        teststr = '&12'
        self.assertFalse(common_functions.is_byte(teststr))

    def testIsByteFalse2(self):
        teststr = '$1'
        self.assertFalse(common_functions.is_byte(teststr))

    def testIsByteFalse3(self):
        teststr = '$1G'
        self.assertFalse(common_functions.is_byte(teststr))

    def testIsByteTrue(self):
        teststr = '$F1'
        self.assertTrue(common_functions.is_byte(teststr))

    def testHexify(self):
        self.assertTrue(common_functions.hexify('ping\r\n'), '0x700x690x6e0x67')

    def testDefaultVariable(self):
        test_text = "File length is $length, crc $crc, filedata: $filedata"
        var_dict = {'length': '100', 'crc': '0x1212', 'filedata': "sometestdata"}
        self.assertEqual(common_functions.replace_variables(test_text, var_dict),
                         "File length is 100, crc 0x1212, filedata: sometestdata")


class testEncoding(unittest.TestCase):

    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()
        self.terminal_example.load_settings("Settings_for_test.json")

    def testNoEncodingASCII(self):
        test_string = "".join([chr(x) for x in range(0, 128)])
        self.assertEqual(test_string, self.terminal_example.decode_input(bytes(test_string, encoding='ascii')))

    def testNoEncodingUTF8(self):
        test_string = "".join([chr(x) for x in range(0, 128)])
        self.assertEqual(test_string, self.terminal_example.decode_input(bytes(test_string, encoding='utf-8')))

    def testNoEncodingCP1251(self):
        test_string = "".join([chr(x) for x in range(0, 128)])
        self.assertEqual(test_string, self.terminal_example.decode_input(bytes(test_string, encoding='cp1251')))

    def testQuestion(self):
        test_string = "".join([chr(x) for x in range(0, 64)]) + "йцукенгшщзхъ" + \
                      "".join([chr(x) for x in range(64, 128)])
        expected = "".join([chr(x) for x in range(0, 64)]) + "????????????" + \
                   "".join([chr(x) for x in range(64, 128)])
        self.terminal_example.text_settings.decode = 1
        self.assertEqual(expected, self.terminal_example.decode_input(bytes(test_string, encoding='cp1251')))

    def testCP1251(self):
        test_string = "".join([chr(x) for x in range(0, 64)]) + "йцукенгшщзхъ" + \
                      "".join([chr(x) for x in range(64, 128)])
        self.terminal_example.text_settings.decode = 2
        self.assertEqual(test_string, self.terminal_example.decode_input(bytes(test_string, encoding='cp1251')))

    def testNoEncoding(self):
        test_string = "".join([chr(x) for x in range(0, 64)]) + "йцукенгшщзхъ" + \
                      "".join([chr(x) for x in range(64, 128)])
        self.terminal_example.text_settings.decode = 0
        self.assertEqual("".join([chr(x) for x in range(0, 128)]),
                         self.terminal_example.decode_input(bytes(test_string, encoding='cp1251')))

    def tearDown(self):
        self.terminal_example.destroy()
        self.app.quit()


class testTextBuffer(unittest.TestCase):
    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()
        self.terminal_example.load_settings("Settings_for_test.json")

    def test_simple(self):
        data = bytes("Ack 0\r\n", "utf-8")
        self.terminal_example.counter = 0
        self.terminal_example.process_read_data(data)
        self.assertEqual(self.terminal_example.TxtBuffer.toPlainText(), "Ack 0\n")
        self.assertEqual(self.terminal_example.counter, 7)

    def test_hexify(self):
        data = bytes("1234\r\n", "utf-8")
        self.terminal_example.counter = 0
        self.terminal_example.CBHex.setChecked(True)
        self.terminal_example.process_read_data(data)
        self.assertEqual(self.terminal_example.TxtBuffer.toPlainText(), "31 32 33 34 0d 0a ")
        self.assertEqual(self.terminal_example.counter, 6)
        self.terminal_example.CBHex.setChecked(False)

    def test_timestamps(self):
        delta = datetime.datetime.now() - self.terminal_example.start_time
        data = "Ack 5"
        self.terminal_example.counter = 0
        self.terminal_example.text_settings.timestamps = True
        self.terminal_example.process_read_data(bytes(data, encoding='ascii'))
        self.assertEqual(self.terminal_example.TxtBuffer.toPlainText(), str(delta)+': '+'Ack 5')
        self.terminal_example.text_settings.timestamps = False
        self.assertEqual(self.terminal_example.counter, 5)

    def test_timestamps_2strings(self):
        delta = datetime.datetime.now() - self.terminal_example.start_time
        data = "Ack 5\r\nId 6"
        self.terminal_example.counter = 0
        self.terminal_example.text_settings.timestamps = True
        self.terminal_example.process_read_data(bytes(data, encoding='ascii'))
        self.assertEqual(self.terminal_example.TxtBuffer.toPlainText(), str(delta) + ': ' + 'Ack 5' + '\n' +
                         str(delta) + ': ' + 'Id 6')
        self.terminal_example.text_settings.timestamps = False
        self.assertEqual(self.terminal_example.counter, 11)

    def testScrollOn(self):
        data = "Ack 5\r\nId 6"
        self.terminal_example.text_settings.scroll = True
        self.terminal_example.process_read_data(bytes(data, encoding='ascii'))
        self.assertEqual(self.terminal_example.TxtBuffer.verticalScrollBar().value(),
                         self.terminal_example.TxtBuffer.verticalScrollBar().maximum())

    def testScrollOff(self):
        data = "Ack 5\r\nId 6"
        self.terminal_example.text_settings.scroll = False
        self.terminal_example.process_read_data(bytes(data, encoding='ascii'))
        self.assertEqual(self.terminal_example.TxtBuffer.verticalScrollBar().value(), 0)

    def tearDown(self):
        self.terminal_example.destroy()
        self.app.quit()


class testSending(unittest.TestCase):

    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.terminal_example = terminal.OstrannaTerminal()
        self.terminal_example.load_settings("Settings_for_test.json")
        self.terminal_example.CBSTM.setChecked(False)
        self.terminal_example.CBNRF.setChecked(False)
        self.terminal_example.CBPorts.setCurrentIndex(1)
        self.terminal_example.BtnConnect.click()

    def testNoSendInTxtBuffer(self):
        self.terminal_example.text_settings.show_sent = False
        self.terminal_example.TxtTransmit.setText("Test")
        self.terminal_example.TxtTransmit.setText("Test")
        self.terminal_example.BtnSend.click()
        self.terminal_example.BtnSend2.click()
        self.assertEqual(self.terminal_example.TxtBuffer.toPlainText(), "")

    def testSendInTxtBufferAndScroll(self):
        self.terminal_example.text_settings.show_sent = True
        self.terminal_example.text_settings.scroll = True
        self.terminal_example.TxtTransmit.setText("Test")
        self.terminal_example.TxtTransmit.setText("Test2")
        self.terminal_example.BtnSend.click()
        self.terminal_example.BtnSend2.click()
        self.assertEqual(self.terminal_example.TxtBuffer.toPlainText(), "Test\nTest2")
        self.assertEqual(self.terminal_example.TxtBuffer.verticalScrollBar().value(),
                         self.terminal_example.TxtBuffer.verticalScrollBar().maximum())

    def testSendInTxtBufferAndNoScroll(self):
        self.terminal_example.text_settings.show_sent = True
        self.terminal_example.text_settings.scroll = True
        self.terminal_example.TxtTransmit.setText("Test")
        self.terminal_example.TxtTransmit.setText("Test2")
        self.terminal_example.BtnSend.click()
        self.terminal_example.BtnSend2.click()
        self.assertEqual(self.terminal_example.TxtBuffer.toPlainText(), "Test\nTest2")
        self.assertEqual(self.terminal_example.TxtBuffer.verticalScrollBar().value(), 0)
