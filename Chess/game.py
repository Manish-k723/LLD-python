from player import Player
from board import Board
class Game:
    def __init__(self, white_player: Player, black_player: Player):
        self.__p1 = white_player
        self.__p2 = black_player
        self.__board = Board(self)
        self.__board.resetBoard()
        self.__game_status = GameStatus.INACTIVE
        
        
    def get_board(self):
        return self.__board
    def startGame(self):
        pass