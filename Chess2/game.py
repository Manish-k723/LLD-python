from board import Board
from color import Color
from game_status import GameStatus
from move import Move
from player import Player


class Game:
    def __init__(self, white_player: Player, black_player: Player):
        self._white_player = white_player
        self._black_player = black_player
        self._board = Board()
        self._board.reset_board()
        self._status = GameStatus.INACTIVE
        self._current_turn = Color.WHITE
        self._game_logs: list[str] = []

    def start_game(self) -> None:
        self._status = GameStatus.ACTIVE

    def get_board(self) -> Board:
        return self._board

    def get_status(self) -> GameStatus:
        return self._status

    def get_game_logs(self) -> list[str]:
        return self._game_logs

    def make_move(self, move: Move) -> bool:
        if self._status != GameStatus.ACTIVE:
            return False

        from_position = move.get_from_position()
        to_position = move.get_to_position()

        if not self._board.is_valid_position(from_position) or not self._board.is_valid_position(to_position):
            return False

        moving_piece = self._board.get_piece(from_position)
        if moving_piece is None:
            return False

        if moving_piece.get_color() != self._current_turn:
            return False

        target_piece = self._board.get_piece(to_position)
        if target_piece is not None and target_piece.get_color() == moving_piece.get_color():
            return False

        if not moving_piece.can_move(self._board, from_position, to_position):
            return False

        self._board.move_piece(from_position, to_position)
        self._game_logs.append(
            f"{self._current_turn.name}: ({from_position.get_row()}, {from_position.get_col()}) -> "
            f"({to_position.get_row()}, {to_position.get_col()})"
        )
        self._switch_turn()
        return True

    def _switch_turn(self) -> None:
        self._current_turn = Color.BLACK if self._current_turn == Color.WHITE else Color.WHITE
