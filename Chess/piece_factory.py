from __future__ import annotations

from Chess.piece import Rook, Piece, Pawn, King, Queen, Knight, Bishop
from Chess.piece_enum import PieceEnum
from Chess.color_enum import Color
from Chess.piece_strategy import MoveStrategy


class PieceFactory:
    @staticmethod
    def create_piece(name: PieceEnum, color: Color) -> Piece | None:
        # Maps piece types to corresponding class instances
        if name == PieceEnum.PAWN:
            return Pawn(color, MoveStrategy())
        elif name == PieceEnum.KING:
            return King(color, MoveStrategy())
        elif name == PieceEnum.QUEEN:
            return Queen(color, MoveStrategy())
        elif name == PieceEnum.ROOK:
            return Rook(color, MoveStrategy())
        elif name == PieceEnum.KNIGHT:
            return Knight(color, MoveStrategy())
        elif name == PieceEnum.BISHOP:
            return Bishop(color, MoveStrategy())
        return None