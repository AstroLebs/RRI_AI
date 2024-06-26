from src.board import Board
from src.tile import Tile
import pytest

@pytest.fixture
def board():
    return Board()

# Test Cases:

def test_valid_placement(board):
    straight_road = Tile("Straight Road",[1,0,1,0], {'road' : ['road']})
    result = board.place_tile(straight_road, (2,1))
    assert result == True
    assert 'tile' in board.graph.nodes[(2,1)]