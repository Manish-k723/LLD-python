from Chess.Piece.piece import Piece
from Chess.Piece.piece_strategy import BishopStrategy
from Chess.Piece.pieces_enum import PieceEnum


class Bishop(Piece):
    def __init__(self, is_white: bool, killed: bool):
        super().__init__(PieceEnum.BISHOP.value, is_white, killed)
        self.__strategy = BishopStrategy()

    def can_move(self):
        return True