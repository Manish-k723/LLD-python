from Chess.Piece.piece_strategy import PieceStrategy
from Chess.position import Position
from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, label: str, is_white: bool, killed: bool):
        self.__label = label
        self.__is_white = is_white
        self.__killed = killed

    def is_white(self) -> bool:
        return self.__is_white

    @abstractmethod
    def can_move(self) -> bool:
        ...