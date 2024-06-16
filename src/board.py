from tile import Tile

class Board:
    def __init__(self):
        self.board = [[None for _ in range(9)] for _ in range(9)]
        self.init_board()

    def init_board(self):
            self.board[0][2] = Tile([0,2,0,0])
            self.board[0][4] = Tile([0,1,0,0])
            self.board[0][6] = Tile([0,2,0,0])
            
            self.board[8][2] = Tile([0,0,0,2])
            self.board[8][4] = Tile([0,0,0,1])
            self.board[8][6] = Tile([0,0,0,2])

            self.board[2][0] = Tile([0,0,1,0])
            self.board[4][0] = Tile([0,0,2,0])
            self.board[6][0] = Tile([0,0,1,0])

            self.board[2][8] = Tile([1,0,0,0])
            self.board[4][8] = Tile([2,0,0,0])
            self.board[6][8] = Tile([1,0,0,0])

    def place_tile(self, tile, x, y):
        if self.valid_move(tile, x, y):
            self.board[x][y] = tile
            return True
        return False

    def valid_move(self, tile, x, y):
        is_valid = False
        exit_rotation = 0
        for dx, dy in [(0,-1),(-1,0),(0,1),(1,0)]:
            if self.get_tile(x+dx, y+dy) is None:
                continue

            print(tile.get_exits())
            print(self.get_tile(x+dx, y+dy).get_exits())
            if tile.get_exits()[exit_rotation] == self.get_tile(x+dx, y+dy).get_exits()[(exit_rotation+2)%4]:
                is_valid = True
                break
            exit_rotation += 1
                    
        return is_valid

    def get_tile(self, x, y):
        return self.board[x][y]

    def get_board(self):
        return self.board
