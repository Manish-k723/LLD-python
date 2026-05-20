from Chess.Piece.piece import Piece
from Chess.Piece.piece_strategy import RookStrategy
from Chess.Piece.pieces_enum import PieceEnum


class Rook(Piece):
    def __init__(self, is_white: bool, killed: bool):
        super().__init__(PieceEnum.ROOK.value, is_white, killed)
        self.__strategy = RookStrategy()

    def can_move(self):
        return True