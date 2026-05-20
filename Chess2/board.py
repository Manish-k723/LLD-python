from __future__ import annotations

from cell import Cell
from color import Color
from piece_factory import PieceFactory
from piece_type import PieceType
from position import Position


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
        self.reset_board()

    def reset_board(self) -> None:
        self._cells = [[Cell(Position(row, col)) for col in range(8)] for row in range(8)]
        self._place_pieces()

    def _place_pieces(self) -> None:
        self._place_major_pieces(0, Color.BLACK)
        self._place_pawns(1, Color.BLACK)
        self._place_pawns(6, Color.WHITE)
        self._place_major_pieces(7, Color.WHITE)

    def _place_major_pieces(self, row: int, color: Color) -> None:
        order = [
            PieceType.ROOK,
            PieceType.KNIGHT,
            PieceType.BISHOP,
            PieceType.QUEEN,
            PieceType.KING,
            PieceType.BISHOP,
            PieceType.KNIGHT,
            PieceType.ROOK,
        ]
        for col, piece_type in enumerate(order):
            self.get_cell(Position(row, col)).set_piece(PieceFactory.create_piece(piece_type, color))

    def _place_pawns(self, row: int, color: Color) -> None:
        for col in range(8):
            self.get_cell(Position(row, col)).set_piece(PieceFactory.create_piece(PieceType.PAWN, color))

    def is_valid_position(self, position: Position) -> bool:
        return 0 <= position.get_row() < 8 and 0 <= position.get_col() < 8

    def get_cell(self, position: Position) -> Cell:
        return self._cells[position.get_row()][position.get_col()]

    def get_piece(self, position: Position):
        return self.get_cell(position).get_piece()

    def is_path_clear(self, from_position: Position, to_position: Position) -> bool:
        row_step = 0
        if to_position.get_row() > from_position.get_row():
            row_step = 1
        elif to_position.get_row() < from_position.get_row():
            row_step = -1

        col_step = 0
        if to_position.get_col() > from_position.get_col():
            col_step = 1
        elif to_position.get_col() < from_position.get_col():
            col_step = -1

        current_row = from_position.get_row() + row_step
        current_col = from_position.get_col() + col_step

        while current_row != to_position.get_row() or current_col != to_position.get_col():
            if self._cells[current_row][current_col].get_piece() is not None:
                return False
            current_row += row_step
            current_col += col_step
        return True

    def move_piece(self, from_position: Position, to_position: Position) -> None:
        from_cell = self.get_cell(from_position)
        to_cell = self.get_cell(to_position)
        moving_piece = from_cell.get_piece()
        target_piece = to_cell.get_piece()

        if target_piece is not None:
            target_piece.mark_killed()

        to_cell.set_piece(moving_piece)
        from_cell.set_piece(None)

    def display(self) -> None:
        for row in self._cells:
            print(" ".join(cell.get_piece().get_symbol() if cell.get_piece() is not None else "." for cell in row))
