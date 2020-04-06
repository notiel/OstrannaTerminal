from dataclasses import dataclass
from enum import Enum
from PyQt5 import QtSerialPort

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
                 7: QtSerialPort.QSerialPort.Data5, 8: QtSerialPort.QSerialPort.Data6}


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


@dataclass
class Macro:
    name: str
    command: str


@dataclass
class MacroSet:
    name: str
    macros: List[Macro]
