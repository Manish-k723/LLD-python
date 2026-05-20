from player import Player
from color_enum import ColorEnum
from game import Game
from board import Board

manish = Player(1, "Manish_choomuuuuuuu", ColorEnum.WHITE)
priyanka = Player(2, "Husn_Pari", ColorEnum.BLACK)

game = Game(manish, priyanka)
game.startGame()

print("Initial Board")
game.get_board().display()


Moves = [
    
]








