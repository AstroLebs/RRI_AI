class Tile:
    def __init__(self, exits, overpass=None):
        self.exits = exits
        self.is_overpass = overpass if overpass is not None else False
    
    def rotate(self):
        self.exits[:] = self.exits[-1:] + self.exits[:-1]
    
    def get_exits(self):
        return self.exits

    def get_overpass(self):
        return self.is_overpass

    

basic_tiles = {
    "straight_road": Tile([0,1,0,1]),
    "straight_rail" : Tile([0,2,0,2]),
    "curve_road" : Tile([1,1,0,0]),
    "curve_rail" : Tile([2,2,0,0]),
    "T_road" : Tile([1,1,1,0]),
    "T_rail" : Tile([2,2,2,0])
}

station_tiles = {
    "straight_station" : Tile([0,1,0,2]),
    "curve_station" : Tile([1,2,0,0]),
    "overpass" : Tile([1,2,1,2], True)
}

special_tiles = {
    "special_0" : Tile([1,1,1,1]),
    "special_1" : Tile([1,1,1,2]),
    "special_2" : Tile([1,1,2,2]),
    "special_3" : Tile([1,2,1,2]),
    "special_4" : Tile([1,2,2,2]),
    "special_5" : Tile([2,2,2,2])
}