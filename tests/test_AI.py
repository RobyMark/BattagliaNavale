from src.grid import Grid
from src.pair import Pair
from src.ai import AI

def test_AI() -> None:
    grid = Grid(4, 4)
    ai = ai(grid)
    assert ai.availableMoves[0].x==0
    assert ai.availableMoves[0].y==0
    assert ai.availableMoves[1].x==0
    assert ai.availableMoves[1].y==1
    assert ai.availableMoves[2].x==0
    assert ai.availableMoves[2].y==2
    assert ai.availableMoves[15].x==3
    assert ai.availableMoves[15].y==3

    