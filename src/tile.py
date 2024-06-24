class Tile:
    """
    Represents a tile in the Railroad Ink game.
    Attributes:
        name (str): The name of the tile.
        exits (list): A list of exit types, where:
            0: No exit
            1: Road exit
            2: Rail exit
        connections (dict): A dictionary specifying valid connections between route types.
        image (any, optional): An optional image representation of the tile.
    """

    def __init__(self, name, exits, connections, image = None):
        self.name = name
        self.exits = exits # 0: No exit, 1: Road exit, 2: Rail exit
        self.connections = connections
        self.image = image

    def rotate(self, clockwise):
        """
        Rotates the tile clockwise or counter-clockwise.
        Args:
            clockwise (bool, optional): If True, rotates clockwise. 
                If False, rotates counter-clockwise. Defaults to True.
        """

        if clockwise is None:
            clockwise = True

        if clockwise:
            self.exits = self.exits[-1] + self.exits[:-1]
        else:
            self.exits = self.exits[1:] + [self.exits[0]]