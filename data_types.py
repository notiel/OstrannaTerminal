from dataclasses import dataclass
from enum import Enum
from PyQt5 import QtSerialPort
from typing import List, Optional, Dict, Any, Tuple

error_codes = {0: 'No error',
               1: 'Device not found',
               2: 'Permission error',
               3: 'Cannot open',
               4: 'Parity error',
               5: 'Framing error',
               6: 'Break condition error',
               7: 'Write error',
               8: 'Read error',
               9: 'Resource error',
               10: 'Unsupported operation error',
               11: 'Unknown error',
               12: 'Timeout error',
               13: 'Not open error'}

max_macros = 20


databits_dict = {5: QtSerialPort.QSerialPort.Data5, 6: QtSerialPort.QSerialPort.Data6,
                 7: QtSerialPort.QSerialPort.Data7, 8: QtSerialPort.QSerialPort.Data8}

baudrates = [9600, 115200, 256000]


class Parity(Enum):
    NONE = 0
    ODD = 1
    EVEN = 2
    MARK = 3
    SPACE = 4


parity_dict = {Parity.NONE: QtSerialPort.QSerialPort.NoParity,
               Parity.ODD: QtSerialPort.QSerialPort.OddParity,
               Parity.EVEN: QtSerialPort.QSerialPort.EvenParity,
               Parity.MARK: QtSerialPort.QSerialPort.MarkParity,
               Parity.SPACE: QtSerialPort.QSerialPort.SpaceParity}

stopbits_dict = {1: QtSerialPort.QSerialPort.OneStop, 2: QtSerialPort.QSerialPort.TwoStop,
                 1.5: QtSerialPort.QSerialPort.OneAndHalfStop}


class Handshaking(Enum):
    NONE = 0
    RTSCTS = 1


hs_dict = {Handshaking.NONE: QtSerialPort.QSerialPort}


@dataclass
class ComSettings:
    name: str = ""
    last_name: str = ""
    baudrate: int = 115200
    databits: int = 8
    parity: Parity = Parity.NONE
    stopbits: float = 1
    handshaking: Handshaking = Handshaking.NONE
    CRLF: bool = True
    bytecodes: bool = True


@dataclass
class Macro:
    name: str
    command: str


@dataclass
class MacroSet:
    name: str
    macros: List[Macro]


def get_macros_by_name(name: str, macros_sets: List[MacroSet]) -> Optional[MacroSet]:
    """
    searches macros in macros list with selected name set
    :param name: macros set name
    :param macros_sets: list of macros sets
    :return: found macroset
    """
    fit = [macros_set for macros_set in macros_sets if macros_set.name == name]
    if fit:
        return fit[0]
    else:
        return None


def create_macros_from_list(data: List[Dict[str, Any]]) -> Tuple[List[MacroSet], str]:
    """
    creates list of macroses from dict
    :param data: list of dicts from json
    :return: list of macroset
    """
    result: List[MacroSet] = list()
    warning = ""
    for macroset in data:
        macros: List[Macro] = list()
        try:
            for macro in macroset['macros']:
                macros.append(Macro(name=macro['name'], command=macro['command']))
        except KeyError:
            warning = "Some macros data is incorrect"
        result.append(MacroSet(name=macroset['name'], macros=macros))
    return result, warning
