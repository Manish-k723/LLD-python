from Chess.Piece.piece import Piece
from Chess.Piece.piece_strategy import PawnStrategy
from Chess.Piece.pieces_enum import PieceEnum


class Pawn(Piece):
    def __init__(self, is_white: bool, killed: bool):
        super().__init__(PieceEnum.PAWN.value, is_white, killed)
        self.__strategy = PawnStrategy()

    def can_move(self):
        return True