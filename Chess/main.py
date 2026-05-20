
from Chess.game import Game
from Chess.player import Player

player1 = Player(1, "Manish", True)
player2 = Player(2, "Prenka", False)

game = Game(player1, player2)
status, winner = game.start_game()

if status:
    print(f"Won: {winner}")
else:
    print("Game Drawn")