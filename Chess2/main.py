from color import Color
from game import Game
from move import Move
from player import Player
from position import Position


white_player = Player(1, "Manish", Color.WHITE) # Safedi ki chamak
black_player = Player(2, "Prenka", Color.BLACK) # Kallu

game = Game(white_player, black_player)
game.start_game()
board = game.get_board()

print("Initial board:")
board.display()

moves = [
    Move(Position(6, 4), Position(4, 4)),
    Move(Position(1, 4), Position(3, 4)),
    Move(Position(7, 6), Position(5, 5)),
    Move(Position(0, 1), Position(2, 2)),
    Move(Position(7, 5), Position(4, 2)),
]

for move in moves:
    print(f"Move {move.get_from_position().get_row()},{move.get_from_position().get_col()} -> "
          f"{move.get_to_position().get_row()},{move.get_to_position().get_col()}")
    print("Success" if game.make_move(move) else "Invalid")
    board.display()

print("Logs:")
for log in game.get_game_logs():
    print(log)
