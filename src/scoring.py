import networkx as nx
from board import Board
from tile import Tile

def calculate_score(G, board_type = None):
    score = 0
    road_len = len(longest_path(G, 'road'))

    rail_len= len(longest_path(G, 'rail'))
    connected_group = score_connected_exit_groups(G)
    mid_tiles= count_tiles_around_point(G, (4,4))
    print(f"{road_len}:{rail_len}:{connected_group}:{mid_tiles}")
    score = road_len + rail_len + connected_group + mid_tiles
    return score

def longest_path(graph, route_type):
    # NOT WORKING (ALWAYS RETURNS 0)
    longest_path = []
    filtered_graph = nx.Graph([(u, v, d) for u, v, d in graph.edges(data=True) if d.get('type') == route_type])
    
    valid_nodes = [node for node in filtered_graph.nodes if 1 <= node[0] <= self.size and 1 <= node[1] <= self.size]
    def dfs(node, current_path):
        nonlocal longest_path
        current_path.append(node)
        if len(current_path) > len(longest_path):
            longest_path = current_path.copy()
        for neighbor in filtered_graph.neighbors(node):
            if neighbor in valid_nodes and neighbor not in current_path:
                dfs(neighbor, current_path)
        current_path.pop()
    
    for node in valid_nodes:
        dfs(node, [])
    return longest_path

def score_connected_exit_groups(graph):
    exit_nodes = [node for node, data in graph.nodes(data=True) if data.get('exit')]
    exit_subgraph = graph.subgraph(exit_nodes)
    connected_components = list(nx.connected_components(exit_subgraph))
    group_sizes = [len(component) for component in connected_components]

    score = sum([(n-1) * 4 + (1 if n == 12 else 0) for n in group_sizes])
    return score

def count_tiles_around_point(graph, point):
    # NOT WORKING (ALWAYS RETURNS 9)
    x_pos,y_pos = point
    tile_count = 0

    for x in range(x_pos -1, x_pos + 2):
        for y in range(y_pos -1, y_pos + 2):
            if (x, y) in graph.nodes and 'tile' in graph.nodes[(x, y)]:
                tile_count += 1

    return tile_count