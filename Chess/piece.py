from Chess.color_enum import Color
from abc import ABC, abstractmethod

from Chess.piece_strategy import MoveStrategy
from Chess.position import Position


class Piece(ABC):
    def __init__(self, color: Color, piece_strategy: MoveStrategy):
        self.__color = color
        self.__strategy = piece_strategy
        self._is_killed = False

    @abstractmethod
    def can_move(self, from_position: Position, to_position: Position)-> bool:
        ...

    def get_color(self) -> Color:
        return self.__color

    def get_is_killed(self) -> bool:
        return self._is_killed

    def mark_killed(self) -> None:
        self._is_killed = True


class Pawn(Piece):
    def can_move(self, from_position: Position, to_position: Position):
        ...

class Rook(Piece):
    def can_move(self, from_position: Position, to_position: Position) -> bool:
        ...

class King(Piece):
    def can_move(self, from_position: Position, to_position: Position):
        ...

class Queen(Piece):
    def can_move(self, from_position: Position, to_position: Position) -> bool:
        ...

class Knight(Piece):
    def can_move(self, from_position: Position, to_position: Position) -> bool:
        ...

class Bishop(Piece):
    def can_move(self, from_position: Position, to_position: Position) -> bool:
        ...
