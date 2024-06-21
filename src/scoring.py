import networkx as nx
from board import Board
from tile import Tile

def longest_path(graph, route_type):
    longest_path = []
    filtered_graph = nx.Graph([(u, v, d) for u, v, d in graph.edges(data=True)
     if d.get('route_type') == route_type])

    for node in filtered_graph.nodes:
        for path in nx.all_simple_paths(filtered_graph, source=node):
            if len(path) > len(longest_path):
                longest_path = path
    
    return len(longest_path)

def count_connected_exit_groups(graph):
    exit_nodes = [node for node, data in graph.nodes(data=True) if data.get('exit')]
    exit_subgraph = graph.subgraph(exit_nodes)
    connected_components = list(nx.connected_components(exit_subgraph))
    group_sizes = [len(component) for component in connected_components]

    score = sum([(n-1) * 4 + (1 if n == 12 else 0) for n in group_sizes])
    return score
