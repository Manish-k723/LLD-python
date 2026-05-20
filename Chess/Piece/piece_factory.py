from __future__ import annotations

from Chess.Piece.bishop import Bishop
from Chess.Piece.king import King
from Chess.Piece.knight import Knight
from Chess.Piece.pawn import Pawn
from Chess.Piece.piece import Piece
from Chess.Piece.piece_strategy import PieceStrategy
from Chess.Piece.queen import Queen
from Chess.Piece.rook import Rook
from Chess.position import Position


class PieceFactory:
    @staticmethod
    def create_piece(label, is_white: bool) -> Piece | None:
        if label == 'king':
            return King(label, is_white, False)
        elif label == 'queen':
            return Queen(label, is_white, False)
        elif label == 'rook':
            return Rook(label, is_white, False)
        elif label == 'knight':
            return Knight(label, is_white, False)
        elif label == 'bishop':
            return Bishop(label, is_white, False)
        elif label == "pawn":
            return Pawn(label, is_white, False)
        return None