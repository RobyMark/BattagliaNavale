from src.grid import Grid
from src.pair import Pair

def test_Grid() -> None:
    grid = Grid(4, 4)
    for i in range(grid.height):
        for j in range(grid.width):
            assert grid.cells[i][j] == "empty"

    grid = Grid(4, 4)
    assert grid.tryAddShip(Pair(0, 1), 3, "s") == "success"
    grid = Grid(4, 4)
    assert grid.tryAddShip(Pair(0, 1), 3, "n") == "fail"
    grid = Grid(4, 4)
    assert grid.tryAddShip(Pair(2, 3), 2, "e") == "fail"
    grid = Grid(4, 4)
    assert grid.tryAddShip(Pair(2, 3), 2, "w") == "success"
    grid = Grid(4, 4)
    assert grid.tryAddShip(Pair(1, 1), 3, "s") == "success"
    assert grid.tryAddShip(Pair(2, 3), 2, "w") == "fail"

    grid = Grid(4, 4)
    grid.cells[2][2] = "ship"
    assert grid.areCellsFree("vertical", 2, 0, 3) == "false"
    assert grid.areCellsFree("vertical", 1, 0, 3) == "true"
    assert grid.areCellsFree("vertical", 2, 0, 1) == "true"
    assert grid.areCellsFree("orizontal", 2, 0, 3) == "false"
    assert grid.areCellsFree("orizontal", 1, 0, 3) == "true"

    grid = Grid(4, 4)
    grid.addShip(Pair(3, 0), 2, "n")
    assert grid.cells[3][0] == "ship"

    grid = Grid(4, 4)
    grid.addShip(Pair(0, 1), 3, "s")
    grid.addShip(Pair(3, 2), 2, "e")
    grid.addShip(Pair(2, 3), 2, "w")
    grid.addShip(Pair(3, 0), 2, "n")

    assert len(grid.ships) == 4
    assert len(grid.ships[0]) == 3
    assert grid.ships[0][0].x==0
    assert grid.ships[0][0].y==1
    assert grid.ships[0][1].x==1
    assert grid.ships[0][1].y==1
    assert grid.cells[0][1] == "ship"
    assert grid.cells[0][3] == "empty"
    assert grid.cells[3][0] == "ship"

    assert grid.move(0, 1) == "miss"
    assert grid.move(1, 1) == "hit"
    assert grid.move(2, 1) == "hit"
    assert grid.move(3, 1) == "sunk"
    