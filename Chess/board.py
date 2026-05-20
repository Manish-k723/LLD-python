from __future__ import annotations

from Chess.cell import Cell
from Chess.piece import Piece
from Chess.piece_factory import PieceFactory
from Chess.position import Position
from color_enum import Color
from piece_enum import PieceEnum

class Board:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if getattr(self, "_initialized", False):
            return 
        self._initialized = True
        self.resetBoard()
        
    def resetBoard(self):
        self._cells = [[Cell(Position(i, j)) for i in range(8)] for j in range(8)]
        self.place_pieces()

    def place_pieces(self):
        self.place_major_pieces()
        self.place_pawns()

    def place_major_pieces(self):
        main_pieces = [PieceEnum.ROOK, PieceEnum.KNIGHT, PieceEnum.BISHOP, PieceEnum.QUEEN, PieceEnum.KING, PieceEnum.BISHOP, PieceEnum.KNIGHT, PieceEnum.ROOK]
        colors = [Color.WHITE, Color.BLACK]
        # Places major chess pieces on starting rows
        for row in [0, 7]:
            color = colors.pop(0)
            for col, piece_tye in enumerate(main_pieces):
                self.get_cell(row, col).set_piece(PieceFactory.create_piece(piece_tye, Color.WHITE if row == 1 else Color.BLACK))

    def place_pawns(self):
        """Places pawns on their respective starting rows"""
        for row in [1, 6]:
            for col in range(8):
                self.get_cell(row, col).set_piece(PieceFactory.create_piece(PieceEnum.PAWN, Color.WHITE if row == 1 else Color.BLACK))

    def get_cell(self, row, col) -> Cell:
        return self._cells[row][col]

    def get_cell_from_position(self, position: Position) -> Cell:
        return self.get_cell(position.get_row(), position.get_col())

    def get_piece(self, position: Position) -> Piece | None:
        return self.get_cell_from_position(position).get_piece()
    
    def display(self):
        for i in range(8):
            for j in range(8):
                print(f"{self.get_cell(i, j).get_piece().__class__.__name__}")

    def move_piece(self, from_position: Position, to_position: Position):
        moving_piece = self.get_piece(from_position)
        target_piece = self.get_piece(to_position)
        if target_piece is not None:
            target_piece.mark_killed()
        self.get_cell_from_position(from_position).set_piece(None)
        self.get_cell_from_position(to_position).set_piece(moving_piece)
