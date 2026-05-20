from __future__ import annotations

from piece import Piece
from position import Position


class Cell:
    def __init__(self, position: Position, piece: Piece | None = None):
        self._position = position
        self._piece = piece

    def get_position(self) -> Position:
        return self._position

    def get_piece(self) -> Piece | None:
        return self._piece

    def set_piece(self, piece: Piece | None) -> None:
        self._piece = piece
