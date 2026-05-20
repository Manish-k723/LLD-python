from Chess.Piece.piece import Piece
from Chess.Piece.piece_strategy import KingStrategy
from Chess.Piece.pieces_enum import PieceEnum


class King(Piece):
    def __init__(self, is_white: bool, killed: bool):
        super().__init__(PieceEnum.KING.value, is_white, killed)
        self.__strategy = KingStrategy()

    def can_move(self):
        return True