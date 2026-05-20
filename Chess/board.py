from Chess.Piece.piece_factory import PieceFactory
from Chess.Piece.pieces_enum import PieceEnum
from Chess.cell import Cell
from Chess.position import Position


class Board:
    def __init__(self):
        self.__board = [[]*8 for _ in range(8)]
        self.create_board()
    def create_board(self):
        white = True
        for i in [0, 7]:
            self.__board[i][0] = Cell(Position(i, 0), PieceFactory.create_piece(PieceEnum.ROOK, white))
            self.__board[i][1] = Cell(Position(i, 1), PieceFactory.create_piece(PieceEnum.BISHOP, white))
            self.__board[i][2] = Cell(Position(i, 2), PieceFactory.create_piece(PieceEnum.KNIGHT, white))
            self.__board[i][3] = Cell(Position(i, 3), PieceFactory.create_piece(PieceEnum.QUEEN, white))
            self.__board[i][4] = Cell(Position(i, 4), PieceFactory.create_piece(PieceEnum.KING, white))
            self.__board[i][5] = Cell(Position(i, 5), PieceFactory.create_piece(PieceEnum.BISHOP, white))
            self.__board[i][6] = Cell(Position(i, 6), PieceFactory.create_piece(PieceEnum.KNIGHT, white))
            self.__board[i][7] = Cell(Position(i, 7), PieceFactory.create_piece(PieceEnum.ROOK, white))

            white = not white

        for i in [1, 6]:
            for j in range(8):
                self.__board[i][j] = Cell(Position(i, j), PieceFactory.create_piece(PieceEnum.PAWN, white))
            white = not white

        for i in range(2, 6):
            for j in range(8):
                self.__board[i][j] = Cell(Position(i, j))


