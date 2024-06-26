from board import Board
from dice import Dice
from scoring import calculate_score

class Game:
    def __init__(self, board_type = None):
        if board_type is None:
            board_type = 'CLASSIC'
        self.using_ai = False
        self.board = Board(board_type)
        self.current_round = 1
        self.available_tiles = []
        self.dice = [Dice(), Dice(), Dice(), Dice('CLASSIC')]

    def roll_dice(self):
        self.available_tiles = [die.roll() for die in self.dice]

    def place_tile(self, tile, pos):
        return self.board.place_tile(tile, pos)

    def play_game(self):
        num_rounds = 7
        for round in range(num_rounds):
            self.current_round = round + 1
            print(f'Round {self.current_round}')

            self.roll_dice()

            while self.available_tiles:
                chosen_tile, chosen_position, rot_num = self.get_player_choice()
                for _ in range(rot_num):
                    chosen_tile.rotate(True)
                if self.place_tile(chosen_tile, chosen_position):
                    self.available_tiles.remove(chosen_tile)
                else:
                    print("Illegal move! Try again")

            self.board.plot_board(f"board_{self.current_round}")
            print(f"Score: {calculate_score(self.board.graph)}")

    
    def get_player_choice(self):
        if self.using_ai:
            tile_index, pos, rot_num = self.get_choice_from_ai()
        else:
            tile_index, pos, rot_num = self.get_choice_from_user()
        return self.available_tiles[tile_index], pos, rot_num

    def get_choice_from_ai(self):
        pass

    def get_choice_from_user(self):
        rot_num = 0
        print("Available Tiles")
        for i, tile in enumerate(self.available_tiles):
            print(f"{i}: {tile.name}")

        while True:
            try:
                tile_index = int(input("Choose a tile (by number): "))
                if 0 <= tile_index < len(self.available_tiles):
                    break
                else:
                    print("Invalid tile index. Please try again.")
            except ValueError:
                print("Invalid input. Please select a tile")

        while True:
            try:
                x = int(input("Enter x-coordinate: "))
                y = int(input("Enter y-coordinate: "))
                pos = (x, y)
                break
            except ValueError:
                print("Invalid input. Please enter numbers for coords")

        while True:
            try:
                user_input = input("Rotate piece? (y/n): ").lower()
                if user_input in ['y','n']:
                    if user_input == 'y':
                        rot_num = int(input("How many rotations?"))
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n")
            except ValueError:
                print("Invalid input.")
        return tile_index, pos, rot_num


if __name__ == "__main__":
    game = Game()
    game.board.plot_board()
    print(game.board.graph.nodes[2,0])
    game.play_game()