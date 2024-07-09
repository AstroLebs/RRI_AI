import networkx as nx
import matplotlib.pyplot as plt
from tile import Tile

class Board:
    def __init__(self, board_type = None):
        BOARDS = {
        'CLASSIC' : 7,
        'CHALLENGE' : 7,
        'GIANT' : 9,
        'EPIC' : 11
        }
        self.size = BOARDS[board_type if board_type else 'CLASSIC']
        self.graph = nx.Graph()
        self.init_board()

    def init_board(self):
        for x in range(self.size+2):
            for y in range(self.size+2):
                
                if (x==0 or x == self.size+1) and (y != 0 and y != self.size+1):
                    if y % 4 == 0:
                        self.graph.add_node((x,y), pos=(x,y), tile = Tile("Road Exit", [1,1,1,1], {'road':['road']}))

                    elif y % 4 == 2:
                        self.graph.add_node((x,y), pos=(x,y), tile = Tile("Rail Exit", [2,2,2,2], {'rail':['rail']}))
                    else:
                        self.graph.add_node((x,y), pos=(x,y), tile = Tile("Border", [0,0,0,0],{'road':[None],'rail':[None]}))
                    continue
                
                if (y==0 or y == self.size+1) and (x != 0 and x != self.size+1):
                    if x % 4 == 0:
                        self.graph.add_node((x,y), pos=(x,y), tile = Tile("Rail Exit", [2,2,2,2], {'rail':['rail']}))
                    elif x % 4 == 2:
                        self.graph.add_node((x,y), pos=(x,y), tile = Tile("Road Exit", [1,1,1,1], {'road':['road']}))
                    else:
                        self.graph.add_node((x,y), pos=(x,y), tile = Tile("Border", [0,0,0,0],{}))
                    continue
                
                self.graph.add_node((x,y), pos=(x,y), tile = Tile("Empty", [0,0,0,0],{}))

    def plot_board(self, filename = None):
        filename = f"{filename}.png" if filename else "board.png"
        pos = nx.get_node_attributes(self.graph, 'pos')

        nx.draw(self.graph, pos, with_labels=True)
        road_exits = [node for node, data in self.graph.nodes(data=True) if data.get('tile') and data.get('tile').name == 'Road Exit']
        rail_exits = [node for node, data in self.graph.nodes(data=True) if data.get('tile') and data.get('tile').name == 'Rail Exit']
        border = [node for node, data in self.graph.nodes(data=True) if data.get('tile') and data.get('tile').name == 'Border']
        
        nx.draw_networkx_nodes(self.graph, pos, nodelist=border, node_shape='s')
        nx.draw_networkx_nodes(self.graph, pos, nodelist=road_exits, node_color='r', node_shape='s')
        nx.draw_networkx_nodes(self.graph, pos, nodelist=rail_exits, node_color='b', node_shape='s')
        

        plt.axis('off')

        plt.savefig(filename)
        plt.close()

    def place_tile(self, tile, pos):
        x, y = pos

        if not (1 <= x < self.size+1 and 1 <= y < self.size+1):
            return False

        check_tile = self.graph.nodes[x,y].get('tile')
        if check_tile and check_tile.name != "Empty":
            return False

        if not self.check_exit_alignment(tile, pos):
            return False

        self.update_connections(tile, pos)
        self.graph.nodes[pos]['tile'] = tile
        
        return True

    def check_exit_alignment(self, tile, pos):
        x, y = pos
        has_connection = False

        for direction, exit_type in enumerate(tile.exits):
            if exit_type == 0:
                continue

            neighbour_pos = None
            if direction == 0:
                neighbour_pos = (x, y-1)
            elif direction == 1:
                neighbour_pos = (x+1, y)
            elif direction == 2:
                neighbour_pos = (x, y+1)
            elif direction == 3:
                neighbour_pos = (x-1, y)

            if neighbour_pos is None or neighbour_pos not in self.graph.nodes:
                return False
            
            neighbour_exit = self.graph.nodes[neighbour_pos]['tile'].exits[direction]
            if neighbour_exit == exit_type or (neighbour_exit == 0 and has_connection):
                has_connection = True
            elif neighbour_exit != 0:
                return False
            
        return has_connection

    def update_connections(self, tile, pos):
        x, y = pos

        for direction, exit_type in enumerate(tile.exits):
            if exit_type == 0:
                continue

            neighbour_pos = None
            if direction == 0:
                neighbour_pos = (x, y-1)
            elif direction == 1:
                neighbour_pos = (x+1, y)
            elif direction == 2:
                neighbour_pos = (x, y+1)
            elif direction == 3:
                neighbour_pos = (x-1, y)

            if neighbour_pos is None or neighbour_pos not in self.graph.nodes:
                continue

            neighbour_exit = self.graph.nodes[neighbour_pos]['tile'].exits[direction]
            
            if neighbour_exit == exit_type:
                self.graph.add_edge(neighbour_pos, pos, type=exit_type)