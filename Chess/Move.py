from Chess.Piece.piece import Piece
from Chess.cell import Cell
from Chess.position import Position


class Move:
    def __init__(self, start: Cell, end: Cell):
        self.__start = start
        self.__end = end

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def is_valid(self):
        return not (self.__start.get_piece().is_white() == self.__end.get_piece().is_white())
