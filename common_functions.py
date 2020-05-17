from PyQt5.QtWidgets import QMessageBox
import re
from typing import List
import binascii
from matplotlib import pyplot
from time import sleep

hex_symbols = '1234567890abcdef'
crc_init_value = 0

def error_message(text: str):
    """
    shows error message with text
    :param text: text of error
    :return:
    """
    error = QMessageBox()
    error.setIcon(QMessageBox.Critical)
    error.setText(text)
    error.setWindowTitle('Error!')
    error.setStandardButtons(QMessageBox.Ok)
    error.exec_()


def split_with_bytes(text: str):
    """
    finds bytes marked as &ff and splits text with them
    :param text: text to split
    :return: result
    """
    # (.*?)(&\w+|$) - regexp to get them all, but the way below is better
    res = re.split(r'(\$*[0-9a-fA-F][0-9a-fA-F])', text)
    return res


def is_byte(text: str):
    """
    checks if string starts with & and other string is a byte
    :param text: text to check
    :return:
    """
    return len(text) == 3 and text[0] == '$' and text[1].lower() in hex_symbols and text[2].lower() in hex_symbols


def hexify(text: str):
    """
    returns hex codes of symbols separated with ' '
    :param text: text to hexifi
    :return: hexified string
    """
    hex_str = ""
    for ch in text:
        add = hex(ord(ch)).replace('0x', '')
        if len(add) == 1:
            add = '0' + add
        hex_str += add + ' '
    return hex_str


def get_crc_table() -> List[int]:
    """
    get crc16_table
    :return:
    """
    res = list()
    poly = 4129
    for i in range(256):
        temp = 0
        a = i << 8
        for j in range(8):
            temp = (temp << 1) ^ poly if (temp ^ a) & 0x8000 else temp << 1
            a <<= 1
        res.append(temp & 0xFFFF)
        # print(hex(temp % 2**16))
    return res


def calculate_crc(crc_table: List[int], data: bytes) -> int:
    """
    calculate crc
    :param crc_table: crc table
    :param data: data to get crc
    :return:
    """
    crc = crc_init_value
    for ch in data:
        crc = ((crc << 8 & 0xFFFF) ^ crc_table[crc >> 8 ^ (0xff & ch)])
    return crc


def test_graph():
    with open("test_graph.txt") as f:
        pyplot.ion()
        fig = pyplot.figure()
        pyplot.title('Realtime file reading')
        ax1 = pyplot.axes()
        data_x = [1]
        data_y = [50]
        l1, = pyplot.plot(data_y)
        pyplot.ylim([0, 10])
        for line in f:
            #sleep(1)
            data_x.append(int(line.split(';')[0]))
            data_y.append(int(line.split(';')[1]))
            pyplot.ylim([0, 10])
            l1.set_xdata(data_x)
            l1.set_ydata(data_y)  # update the data
            pyplot.draw()
        pyplot.savefig("test.png")
        pyplot.show()
        sleep(5)

if __name__ == '__main__':
    test_graph()