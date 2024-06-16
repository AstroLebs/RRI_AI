from board import Board
from tile import Tile

class Game:
    def __init__(self):
        self.board = Board()

game = Game()
new_tile = Tile([2,2,2,2])
print(game.board.place_tile(new_tile, 1, 2))
print(game.board.place_tile(new_tile, 2, 2))