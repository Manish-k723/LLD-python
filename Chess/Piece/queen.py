from Chess.Piece.piece import Piece
from Chess.Piece.piece_strategy import QueenStrategy
from Chess.Piece.pieces_enum import PieceEnum


class Queen(Piece):
    def __init__(self, is_white: bool, killed: bool):
        super().__init__(PieceEnum.QUEEN.value, is_white, killed)
        self.__strategy = QueenStrategy()

    def can_move(self):
        return True