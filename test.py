import unittest
import terminal
import data_types
from PyQt5 import QtWidgets, QtGui
import sys


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

    def testConnectAndSisconnect(self):
        self.terminal_example.CBSTM.setChecked(False)
        self.terminal_example.CBNRF.setChecked(False)
        self.terminal_example.show()
        self.terminal_example.connect()
        self.assertTrue(self.terminal_example.BtnDisconnect.isEnabled())
        self.assertEqual(self.terminal_example.port_settings.name, 'COM3')
        self.terminal_example.disconnect()
        self.assertTrue(self.terminal_example.BtnConnect.isEnabled())
        self.assertEqual(self.terminal_example.port_settings.name, '')

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



