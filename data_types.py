from dataclasses import dataclass
from enum import Enum

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


class Parity(Enum):
    NONE = 0
    ODD = 1
    EVEN = 2
    MARK = 3
    SPACE = 4


class Handshaking(Enum):
    NONE = 0
    RTSCTS = 1


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
