from board import Board
from tile import Tile
from dice import Dice

class Game:
    """
    Represents a game of Railroad Ink.
    Attributes:
        board (Board): The game board.
        dice (list): A list of Dice objects.
    """

    GAME_DICE_TYPES = {
        'CLASSIC' : 3 * ['NORMAL_DICE'] + ['CLASSIC_STATION_DICE']
        }

    def __init__(self, game_type = None):
        if game_type is None:
            game_type = 'CLASSIC'
        self.game_type = game_type
        self.board = Board(game_type)
        #self.dice = [Dice(die) for die in GAME_DICE_TYPES[game_type]]

    def roll_dice(self):
        roll = []
        for die in self.dice:
            roll.append(die.roll())
        return roll
        

if __name__ == "__main__":
    game = Game()
    straight_road = Tile("Straight Road",[1,0,1,0], {'road' : ['road']})
    game.board.place_tile(straight_road, (2,1))
    game.board.plot_board()

    