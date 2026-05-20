from Chess.Piece.piece import Piece
from Chess.Piece.piece_strategy import KnightStrategy
from Chess.Piece.pieces_enum import PieceEnum


class Knight(Piece):
    def __init__(self, is_white: bool, killed: bool):
        super().__init__(PieceEnum.KNIGHT.value, is_white, killed)
        self.__strategy = KnightStrategy()

    def can_move(self):
        return True