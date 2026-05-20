from enum import Enum


class GameStatus(Enum):
    INACTIVE = 1
    ACTIVE = 2
    CHECK = 3
    CHECKMATE = 4
    DRAW = 5
    STALEMATE = 6
