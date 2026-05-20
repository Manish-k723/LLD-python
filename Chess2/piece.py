from __future__ import annotations

from abc import ABC

from color import Color
from move_strategy import MoveStrategy
from piece_type import PieceType
from position import Position


class Piece(ABC):
    def __init__(self, piece_type: PieceType, color: Color, move_strategy: MoveStrategy):
        self._piece_type = piece_type
        self._color = color
        self._move_strategy = move_strategy
        self._is_killed = False

    def get_piece_type(self) -> PieceType:
        return self._piece_type

    def get_color(self) -> Color:
        return self._color

    def is_killed(self) -> bool:
        return self._is_killed

    def mark_killed(self) -> None:
        self._is_killed = True

    def can_move(self, board, from_position: Position, to_position: Position) -> bool:
        return self._move_strategy.can_move(board, self, from_position, to_position)

    def get_symbol(self) -> str:
        symbol_map = {
            PieceType.ROOK: "R",
            PieceType.KNIGHT: "N",
            PieceType.BISHOP: "B",
            PieceType.QUEEN: "Q",
            PieceType.KING: "K",
            PieceType.PAWN: "P",
        }
        symbol = symbol_map[self._piece_type]
        return symbol if self._color == Color.WHITE else symbol.lower()
