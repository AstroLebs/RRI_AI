from tile import Tile
import random

NORMAL_DICE = {
    1 : Tile("Straight Road", [1,0,1,0], {'road':['road']}),
    2 : Tile("Curved Road", [1,1,0,0], {'road':['road']}),
    3 : Tile("T Road", [1,1,1,0], {'road':['road']}),
    4 : Tile("Straight Rail", [2,0,2,0], {'rail':['rail']}),
    5 : Tile("Curved Rail", [2,2,0,0], {'rail':['rail']}),
    6 : Tile("T Rail", [2,2,2,0], {'rail':['rail']})
    }

CLASSIC_STATION_DICE = {
    1 : Tile("Straight Station", [1,0,2,0], {'road':['road','rail'],'rail':['road','rail']}),
    2 : Tile("Curved Station", [1,2,0,0], {'road':['road','rail'],'rail':['road','rail']}),
    3 : Tile("Overpass", [1,2,1,2], {'road':['road'], 'rail':['rail']})
    }

DICE = {
    'NORMAL' : NORMAL_DICE,
    'CLASSIC' : CLASSIC_STATION_DICE
}

class Dice:
    def __init__(self, dice_type = None):
        if dice_type is None:
            dice_type = 'NORMAL'
        self.faces = DICE[dice_type]

    def roll(self):
        return random.choice(list(self.faces.values()))