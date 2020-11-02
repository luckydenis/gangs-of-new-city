# coding: utf8
from enum import Enum
from enum import auto
from enum import unique
from .icons import emojize


@unique
class Commands(Enum):
    def __str__(self):
        return f'{self.name}'.lower()

    def mk(self):
        return f'/{self}'

    def get(self):
        return str(self)

    START = auto()
    AYES = auto()
    ANO = auto()
    HNAME = auto()
    BUG = auto()


class EmojizeCommands(Enum):
    _T = ":{0}:"
    WARNING = _T.format("warning")
    WHITE_CHECK_MARK = _T.format("white_check_mark")
    BUG = _T.format("bug")

    def __str__(self):
        return f'{self.name}'.lower()

    def mk(self):
        return f"{emojize(self.value)}"

    def get(self):
        return f"^{emojize(self.value)}"