import pytest
import terminal
import data_types


@pytest.fixture
def terminal_example():
    terminal_ex = terminal.OstrannaTerminal()
    terminal_ex.text_settings = data_types.TextSettings()
    terminal_ex.port_settings = data_types.ComSettings()
    terminal_ex.CBSTM.setChecked(True)
    terminal_ex.CBNRF.setChecked(False)
    terminal_ex.CBPorts.setCurrentIndex(0)
    terminal_ex.BtnConnect.click()
    yield terminal_ex
    terminal_ex.destroy()


def test_receieve(qtbot, terminal_example):
    terminal_example.text_settings.CRLF = True
    terminal_example.TxtTransmit.setText('Ping')
    terminal_example.TxtBuffer.clear()
    terminal_example.BtnSend.click()

    def check_plain_text():
        assert terminal_example.TxtBuffer.toPlainText() == 'Ping\nAck 0\n'
    qtbot.waitUntil(check_plain_text)


def test_repeat1(qtbot, terminal_example):
    terminal_example.text_settings.CRLF = True
    terminal_example.TxtTransmit.setText('Ping')
    terminal_example.TxtTransmit2.setText('Version')
    terminal_example.CBRepeat.setChecked(True)
    terminal_example.CBRepeat2.setChecked(False)
    terminal_example.SpinRepeat.setValue(1000)
    terminal_example.TxtBuffer.clear()
    terminal_example.BtnSend.click()

    def check_txt_buffer():
        assert terminal_example.TxtBuffer.toPlainText() == \
               'Ping\nAck 0\nPing\nAck 0\n'

    qtbot.waitUntil(check_txt_buffer, timeout=1900)


def test_repeat2(qtbot, terminal_example):
    terminal_example.text_settings.CRLF = True
    terminal_example.TxtTransmit.setText('Ping')
    terminal_example.TxtTransmit2.setText('Test')
    terminal_example.CBRepeat.setChecked(False)
    terminal_example.CBRepeat2.setChecked(True)
    terminal_example.SpinRepeat2.setValue(1000)
    terminal_example.TxtBuffer.clear()
    terminal_example.BtnSend2.click()

    def check_txt_buffer():
        assert terminal_example.TxtBuffer.toPlainText() == \
               'Test\nAck 6\nTest\nAck 6\n'

    qtbot.waitUntil(check_txt_buffer, timeout=2000)

def test_send_file_and_command(qtbot, terminal_example):
    terminal_example.file_to_send = \
        r'C:\Users\juice\Downloads\PycharmProjects\OstrannaTerminal\Ostranna_Logo.ico'
    terminal_example.text_settings.crc_poly = 4129
    terminal_example.text_settings.crc_init = 0
    terminal_example.BtnRefresh.setEnabled(True)
    terminal_example.BtnRefresh.click()
    terminal_example.BtnSendFile.setEnabled(True)
    terminal_example.BtnSendFile.click()
    terminal_example.TxtBuffer.clear()
    terminal_example.text_settings.CRLF = True
    terminal_example.TxtTransmit.setText('Ping')
    terminal_example.TxtBuffer.clear()
    terminal_example.text_settings.show_sent = True
    terminal_example.BtnSend.click()

    def check_txt_buffer():
        assert 'Ping' in terminal_example.TxtBuffer.toPlainText() \
               and 'Ack' in terminal_example.TxtBuffer.toPlainText()

    qtbot.waitUntil(check_txt_buffer, timeout=3000)

