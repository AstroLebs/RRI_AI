from tile import Tile
import NetworkX as nx

class Board:
    def __init__(self):
        self.board = [[None for _ in range(9)] for _ in range(9)]
        self.init_board()
        self.G = nx.Graph()

    def init_board(self):
        for i in range(9):
            self.board[i][0] = Tile([0,0,0,0])
            self.board[i][8] = Tile([0,0,0,0])
            self.board[0][i] = Tile([0,0,0,0])
            self.board[8][i] = Tile([0,0,0,0])
            G.add_nodes_from(['border_'+i+'0',
            'border_'+i+'8',
            'border_'+'0'+i,
            'border_'+'8'+i])

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

        G.add_nodes_from([
        'exit_02',
        'exit_04',
        'exit_06',
        'exit_82',
        'exit_84',
        'exit_86',
        'exit_20',
        'exit_40',
        'exit_60',
        'exit_28',
        'exit_48',
        'exit_68'])

        G.add_nodes_from([])

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
                exit_rotation += 1
                continue
            
            print(tile.get_exits()[(exit_rotation+2)%4])
            print(self.get_tile(x+dx, y+dy).get_exits()[(exit_rotation)%4])
            if tile.get_exits()[(exit_rotation+2)%4] != 0 and self.get_tile(x+dx, y+dy).get_exits()[exit_rotation] != 0:
                if tile.get_exits()[(exit_rotation+2)%4] != self.get_tile(x+dx, y+dy).get_exits()[exit_rotation]:
                    return False
                else:
                    is_valid = True
                
            exit_rotation += 1
                    
        return is_valid
    
    def get_connections(self, x, y):

        connections = []
        exit_rotation = 0
        for dx, dy in [(0,-1), (-1,0), (0,1), (1,0)]:
            if self.get_tile(x+dx, y+dy) is None:
                exit_rotation += 1
                continue

            if self.get_tile(x, y).get_exists()[(exit_rotation+2)%4] != 0 and self.get_tile(x+dx, y+dy).get_exits()[exit_rotation] != 0:
                if self.get_tile(x, y).get_exits()[(exit_rotation+2)%4] == self.get_tile(x+dx, y+dy).get_exits()[exit_rotation]:
                    connections.append((x+dx, y+dy))
            
            exit_rotation += 1

        return connections

    def get_tile(self, x, y):
        return self.board[x][y]

    def get_board(self):
        return self.board
