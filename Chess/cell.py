from __future__ import annotations

from Chess.Piece.piece import Piece
from Chess.position import Position


class Cell:
    def __init__(self, position: Position, piece: Piece | None = None ):
        self.__position = position
        self.__piece = piece

    def get_position(self) -> Position:
        return self.__position
    def get_piece(self) -> Piece:
        return self.__piece

    def update_cell(self, piece: Piece| None) -> None:
        self.__piece = piece

