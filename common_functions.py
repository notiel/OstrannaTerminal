from PyQt5.QtWidgets import QMessageBox
import re

hex_symbols = '1234567890abcdef'


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


# def split_with_bytes(text: str):
    # """
    # finds bytes marked as &ff and splits text with them
    # :param text: text to split
    # :return:
    # """
    # last = 0
    # i = 0
    # res = list()
    # while i < len(text):
    #     if text[i] != '&':
    #         i += 1
    #     else:
    #         if i+2 < len(text) and text[i+1].lower() in hex_symbols and text[i+2].lower() in hex_symbols:
    #             res.append(text[last:i])
    #             res.append(text[i:i+3])
    #             last = i + 3
    #             i = i + 3
    #         else:
    #             i += 1
    # if last != len(text):
    #     res.append(text[last:])
    # return res
