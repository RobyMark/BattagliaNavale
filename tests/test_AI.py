from src.grid import Grid
from src.pair import Pair
from src.ai import AI
from pytest_mock import MockerFixture

def test_AI(mocker: MockerFixture) -> None:
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

    #placeShips
    grid = Grid(4, 4)
    ai = ai(grid)
    ai.placeShips(grid, [3, 2, 2])
    mocker.patch.object(ai, "random.randint", return_value="success")
    spy = mocker.spy(grid, "tryAddShip")
    assert spy.call_count == 3

    #makeMove
    grid = Grid(4, 4)
    ai = ai(grid)
    spy = mocker.spy(ai, "randomMove")
    assert spy.call_count == 1

    grid = Grid(4, 4)
    ai = ai(grid)
    spy = mocker.spy(ai, "checkNeighbours")
    assert spy.call_count == 1

    #randomMove
    grid = Grid(4, 4)
    ai = ai(grid)
    mock_rand = 1
    mocker.patch.object(ai, "random.randint", return_value=mock_rand)
    ai.randomMove(grid)
    assert ai.lastMove.x == 0
    assert ai.lastMove.x == 2
    assert len(ai.availableMoves) == 15

    #removeLastMove
    grid = Grid(4, 4)
    ai = ai(grid)
    ai.lastMove = Pair(1, 2)
    ai.removeLastMove()
    assert len(ai.availableMoves) == 15

    #checkNeighbours
    grid = Grid(4, 4)
    ai = ai(grid)
    grid.cells[2][2]="hit"
    ai.lastMove=Pair(2, 2)
    ai.checkNeighbours(grid)
    assert ai.lastMove.x == 1
    assert ai.lastMove.y == 2

    grid = Grid(4, 4)
    ai = ai(grid)
    grid.cells[2][2]="hit"
    grid.cells[1][2]="hit"
    ai.lastMove=Pair(2, 2)
    ai.checkNeighbours(grid)
    assert ai.lastMove.x == 3
    assert ai.lastMove.y == 2

    grid = Grid(4, 4)
    ai = ai(grid)
    grid.cells[2][2]="hit"
    grid.cells[1][2]="hit"
    grid.cells[3][2]="hit"
    ai.lastMove=Pair(2, 2)
    ai.checkNeighbours(grid)
    assert ai.lastMove.x == 2
    assert ai.lastMove.y == 1

    grid = Grid(4, 4)
    ai = ai(grid)
    grid.cells[2][2]="hit"
    grid.cells[1][2]="hit"
    grid.cells[3][2]="hit"
    grid.cells[2][1]="hit"
    ai.lastMove=Pair(2, 2)
    ai.checkNeighbours(grid)
    assert ai.lastMove.x == 2
    assert ai.lastMove.y == 3


