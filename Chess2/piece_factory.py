from color import Color
from piece import Piece
from piece_type import PieceType
from pieces import Bishop, King, Knight, Pawn, Queen, Rook


class PieceFactory:
    @staticmethod
    def create_piece(piece_type: PieceType, color: Color) -> Piece:
        if piece_type == PieceType.KING:
            return King(color)
        if piece_type == PieceType.QUEEN:
            return Queen(color)
        if piece_type == PieceType.ROOK:
            return Rook(color)
        if piece_type == PieceType.BISHOP:
            return Bishop(color)
        if piece_type == PieceType.KNIGHT:
            return Knight(color)
        return Pawn(color)
