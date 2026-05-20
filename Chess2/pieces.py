from color import Color
from move_strategy import (
    BishopMoveStrategy,
    KingMoveStrategy,
    KnightMoveStrategy,
    PawnMoveStrategy,
    QueenMoveStrategy,
    RookMoveStrategy,
)
from piece import Piece
from piece_type import PieceType


class King(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.KING, color, KingMoveStrategy())


class Queen(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.QUEEN, color, QueenMoveStrategy())


class Rook(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.ROOK, color, RookMoveStrategy())


class Bishop(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.BISHOP, color, BishopMoveStrategy())


class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.KNIGHT, color, KnightMoveStrategy())


class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.PAWN, color, PawnMoveStrategy())
