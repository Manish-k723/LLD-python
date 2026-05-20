from enum import Enum
class GameStatus(Enum):
    INACTIVE = -1
    ACTIVE = 0
    CHECK = 1
    CHECKMATE = 2
    DRAW = 3
    STALEMATE = 4