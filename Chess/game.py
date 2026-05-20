from Chess.color_enum import Color
from Chess.game_status_enum import GameStatus
from Chess.move import Move
from Chess.piece import Piece
from player import Player
from board import Board
class Game:
    def __init__(self, white_player: Player, black_player: Player):
        self.__p1 = white_player
        self.__p2 = black_player
        self.__board = Board()
        self.__board.resetBoard()
        self.__game_status = GameStatus.INACTIVE
        self.__turn: Color = Color.WHITE
        
    def get_board(self):
        return self.__board

    def get_game_status(self):
        return self.__game_status

    def startGame(self):
        self.__game_status = GameStatus.ACTIVE

    def make_move(self, move: Move):
        if self.__game_status != GameStatus.ACTIVE:
            return False

        if not move.is_valid():
            return False

        moving_piece: Piece = self.__board.get_piece(move.get_from_position())
        if moving_piece is None:
            return False
        if moving_piece.get_color() != self.__is_white_turn:
            return False

        target_piece: Piece = self.__board.get_piece(move.get_to_position())

        if target_piece is not None and target_piece.get_color() == moving_piece.get_color():
            return False

        if not moving_piece.can_move(from_position=move.get_from_position(), to_position=move.get_to_position()):
            return False

        self.__board.move_piece(move.get_from_position(), move.get_to_position())
        self.switch_turn()
        return True

    def switch_turn(self):
        self.__turn = Color.WHITE if self.__turn == Color.BLACK else Color.BLACK

