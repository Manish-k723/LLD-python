from __future__ import annotations

from abc import ABC, abstractmethod

from color_enum import Color
from position import Position


class MoveStrategy(ABC):
    @abstractmethod
    def can_move(self, board, piece, from_position: Position, to_position: Position) -> bool:
        ...


class RookMoveStrategy(MoveStrategy):
    def can_move(self, board, piece, from_position: Position, to_position: Position) -> bool:
        same_row = from_position.get_row() == to_position.get_row()
        same_col = from_position.get_col() == to_position.get_col()
        return (same_row or same_col) and board.is_path_clear(from_position, to_position)


class BishopMoveStrategy(MoveStrategy):
    def can_move(self, board, piece, from_position: Position, to_position: Position) -> bool:
        row_diff = abs(from_position.get_row() - to_position.get_row())
        col_diff = abs(from_position.get_col() - to_position.get_col())
        return row_diff == col_diff and board.is_path_clear(from_position, to_position)


class QueenMoveStrategy(MoveStrategy):
    def can_move(self, board, piece, from_position: Position, to_position: Position) -> bool:
        same_row = from_position.get_row() == to_position.get_row()
        same_col = from_position.get_col() == to_position.get_col()
        diagonal = abs(from_position.get_row() - to_position.get_row()) == abs(
            from_position.get_col() - to_position.get_col()
        )
        return (same_row or same_col or diagonal) and board.is_path_clear(from_position, to_position)


class KnightMoveStrategy(MoveStrategy):
    def can_move(self, board, piece, from_position: Position, to_position: Position) -> bool:
        row_diff = abs(from_position.get_row() - to_position.get_row())
        col_diff = abs(from_position.get_col() - to_position.get_col())
        return (row_diff, col_diff) in {(2, 1), (1, 2)}


class KingMoveStrategy(MoveStrategy):
    def can_move(self, board, piece, from_position: Position, to_position: Position) -> bool:
        row_diff = abs(from_position.get_row() - to_position.get_row())
        col_diff = abs(from_position.get_col() - to_position.get_col())
        return max(row_diff, col_diff) == 1


class PawnMoveStrategy(MoveStrategy):
    def can_move(self, board, piece, from_position: Position, to_position: Position) -> bool:
        direction = -1 if piece.get_color() == Color.WHITE else 1
        start_row = 6 if piece.get_color() == Color.WHITE else 1
        target_piece = board.get_piece(to_position)

        same_col = from_position.get_col() == to_position.get_col()
        row_diff = to_position.get_row() - from_position.get_row()
        col_diff = abs(to_position.get_col() - from_position.get_col())

        if same_col and target_piece is None:
            if row_diff == direction:
                return True
            if from_position.get_row() == start_row and row_diff == 2 * direction:
                middle = Position(from_position.get_row() + direction, from_position.get_col())
                return board.get_piece(middle) is None

        if col_diff == 1 and row_diff == direction:
            return target_piece is not None and target_piece.get_color() != piece.get_color()

        return False
