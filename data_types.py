from dataclasses import dataclass
from enum import Enum


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
    baudrate: int = 115200
    databits: int = 8
    parity: Parity = Parity.NONE
    stopbits: float = 1
    handshaking: Handshaking = Handshaking.NONE
    CRLF: bool = True
