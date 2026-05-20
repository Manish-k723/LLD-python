from typing import List

from Chess.move import Move
from Chess.position import Position
from player import Player
from color_enum import Color
from game import Game

manish = Player(1, "Manish", Color.WHITE)
priyanka = Player(2, "Cutie_Penka", Color.BLACK)

game = Game(manish, priyanka)
game.startGame()

print("Initial Board")
game.get_board().display()

moves = [
    Move(Position(1, 1), Position(2, 2)),
    Move(Position(2, 2), Position(3, 3)),
    Move(Position(3, 3), Position(4, 4)),
]

for move in moves:
    print("Success" if game.make_move(move) else "Invalid")
    game.get_board().display()









