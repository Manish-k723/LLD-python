from Chess.Move import Move
from Chess.board import Board
from Chess.cell import Cell
from Chess.game_status import GameStatus
from Chess.player import Player
from Chess.position import Position


class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.__board = Board()
        self.__player1 = player1
        self.__player2 = player2
        self.__status: GameStatus = GameStatus.INACTIVE
        self.__is_white_turn = True
        self.game_logs = [str]

    def start_game(self):
        self.__status = GameStatus.ACTIVE

        # Cell(Position(x1, y1)), Cell(Position(x2, y2))

        while self.__status == GameStatus.ACTIVE:
            x1 = int(input())
            y1 = int(input())
            x2 = int(input())
            y2 = int(input())
            if self.__is_white_turn:
                self.make_move()
            else:
                self.make_move()


    def make_move(self):
        ...
