import networkx as nx
from board import Board
from tile import Tile

def calculate_score(G, board_type = None):
    if board_type is None:
        board_type = 'CLASSIC'
    score = 0
    score += longest_path_len(G, 'road')
    score += longest_path_len(G, 'rail')
    score += tiles_in_grid(G, (4,4))
    score += connected_exits(G)
    score -= unconnected_edges(G)
    return score

def longest_path_len(G, connection_type):
    longest_path = []

    def dfs(node, current_path, visited):
        visited.add(node)
        current_path.append(node)

        for n in G.neighbor(node):
            if n not in visited and G[node][n]['type'] == connection_type and node in G.neighbors(n) and G[n][node]['type'] == connection_type:
                dfs(n, current_path, visited)

        nonlocal longest_path
        if len(current_path) > len(longest_path):
            longest_path = current_path.copy()

        current_path.pop()
        visited.remove(node)

    for node in G.nodes:
        dfs(node, [], set())

    return len(longest_path)

def tiles_in_grid(G, pos):
    x,y = pos
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if G.has_node((i,j)) and G.nodes[(i,j)].get('tile'):
                count += 1
    return count

def unconnected_edges(G):
    pass

def connected_exits(G):
    pass