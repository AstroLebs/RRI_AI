class Board:
    def __init__(self):
        self.board = [[None for _ in range(7)] for _ in range(7)]

    def place_tile(self, tile, x, y):
        if self.valid_move(tile, x, y):
            self.board[x][y] = tile
            return True
        return False

    def valid_move(self, tile, x, y):
        if x < 0 or x >= 7 or y < 0 or y >= 7:
            return False
        if self.board[x][y] is not None:
            return False
        for dx, dy in [(0,1), (1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 7 and 0 <= ny < 7:
                adj_tile = self.get_tile(nx, ny)
                if adj_tile is not None:
                    pass
        # Fix once tiles are implimented
        return True

    def get_tile(self, x, y):
        return self.board[x][y]

    def get_board(self):
        return self.board
