import networkx as nx
import matplotlib.pyplot as plt

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
                        self.graph.add_node((x,y), pos=(x,y), exit='road')
                    elif y % 4 == 2:
                        self.graph.add_node((x,y), pos=(x,y), exit='rail')
                    else:
                        self.graph.add_node((x,y), pos=(x,y), exit='border')
                    continue
                
                if (y==0 or y == self.size+1) and (x != 0 and x != self.size+1):
                    if x % 4 == 0:
                        self.graph.add_node((x,y), pos=(x,y), exit='rail')
                    elif x % 4 == 2:
                        self.graph.add_node((x,y), pos=(x,y), exit='road')
                    else:
                        self.graph.add_node((x,y), pos=(x,y), exit='border')
                    continue
                
                self.graph.add_node((x,y), pos=(x,y), exit='none')

    def plot_board(self, filename = None):
        filename = f"{filename}.png" if filename else "board.png"
        pos = nx.get_node_attributes(self.graph, 'pos')

        nx.draw(self.graph, pos, with_labels=True)
        road_exits = [node for node, data in self.graph.nodes(data=True) if data.get('exit') == 'road']
        rail_exits = [node for node, data in self.graph.nodes(data=True) if data.get('exit') == 'rail']
        border = [node for node, data in self.graph.nodes(data=True) if data.get('exit') == 'border']
        
        nx.draw_networkx_nodes(self.graph, pos, nodelist=road_exits, node_color='r', node_shape='s', label=True)
        nx.draw_networkx_nodes(self.graph, pos, nodelist=rail_exits, node_color='b', node_shape='s')
        nx.draw_networkx_nodes(self.graph, pos, nodelist=border, node_shape='s')

        plt.savefig(filename)
        plt.close()

    def place_tile(self, tile, pos):
        x, y = pos

        if not (1 <= x < self.size+1 and 1 <= y < self.size+1):
            return False

        if 'tile' in self.graph.nodes[x,y]:
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

            neighbour_exit = self.graph.nodes[neighbour_pos]['exit']
            exits = {
                0 : 'none',
                1 : 'road',
                2 : 'rail'

            }
            if neighbour_exit == exits[exit_type] or (neighbour_exit == 'border' and has_connection):
                has_connection = True
            elif neighbour_exit != 'border':
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

            neighbour_exit = self.graph.nodes[neighbour_pos]['exit']
            exits = {
                0 : 'none',
                1 : 'road',
                2 : 'rail'

            }
            if neighbour_exit in [exits[exit_type], 'border']:
                self.graph.add_edge(pos, neighbour_pos, type=exit_type)