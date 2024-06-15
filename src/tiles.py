class Tile:
    def __init__(self, connections):
        self.connections = connections
        self.rotation = 0
        self.flip = False
    
    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        for connection_type in self.connections:
            connection_type[:] = connection_type[-1:] + connection_type[:-1]
    
    def flip(self):
        self.flip = not self.flip
        for connection_type in self.connections:
            connection_type.reverse()

    def has_rail_connection(self, direction):
        adj_dir = (direction - self.rotation) % 4
        return self.connections[0][adj_dir]

    def has_road_connection(self, direction):
        adj_dir = (direction + self.rotation) % 4
        return self.connections[1][adj_dir]

    