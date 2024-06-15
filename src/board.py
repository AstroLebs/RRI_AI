class Board:
    def __init__(self):
        self.board = [[None for _ in range(9)] for _ in range(9)]
        self.init_border()

    def init_border(self):
        """
        Initialize the border with rails/roads at the proper locations
        """
        for x in range(9):
            if x == 2 or x == 6:
                self.board[x][0] = Tile([[False, False, True, False],[False, False, False, False]])
                self.board[x][8] = Tile([[True, False, False, False],[False, False, False, False]])
            elif x == 4:
                self.board[x][0] = Tile([[False, False, False, False],[False, False, True, False]])
                self.board[x][8] = Tile([[False, False, False, False],[True, False, False, False]])
            else:
                self.board[x][0] = Tile([[False, False, False, False],[False, False, False, False]])
                self.board[x][8] = Tile([[False, False, False, False],[False, False, False, False]])

        for y in range(1,8):
            if y == 2 or y == 6:
                self.board[0][y] = Tile([[False, False, False, False],[False, True, False, False]])
                self.board[8][y] = Tile([[False, False, False, False],[False, False, False, True]])
            elif y == 4:
                self.board[0][y] = Tile([[False, True, False, False],[False, False, False, False]])
                self.board[8][y] = Tile([[False, False, False, True],[False, False, False, False]])
            else:
                self.board[0][y] = Tile([[False, False, False, False],[False, False, False, False]])
                self.board[8][y] = Tile([[False, False, False, False],[False, False, False, False]])

    def place_tile(self, tile, x, y):
        if self.valid_move(tile, x, y):
            self.board[x][y] = tile
            return True
        return False

    def valid_move(self, tile, x, y):
        if x < 1 or x >= 8 or y < 1 or y >= 8:
            return False
        if self.board[x][y] is not None:
            return False
        dir = 0
        connected = False
        for dx, dy in [(0,1), (1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if self.get_tile(nx, ny) is not None:
                adj_tile = self.get_tile(nx, ny)
                if adj_tile is not None:
                    if adj_tile.has_road_connection((dir-2)%4) and tile.has_rail_connection(dir):
                        return False
                    if adj_tile.has_rail_connection((dir-2)%4) and tile.has_road_connection(dir):
                        return False
                    if adj_tile.has_rail_connection((dir-2)%4) and tile.has_rail_connection(dir):
                        connected = True
                    if adj_tile.has_road_connection((dir-2)%4) and tile.has_road_connection(dir):
                        connected = True
            dir += 1

        return connected

    def get_tile(self, x, y):
        return self.board[x][y]

    def get_board(self):
        return self.board
