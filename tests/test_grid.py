from src.grid import Grid
from src.pair import Pair

def test_cells() -> None:
    grid = Grid(4, 4)
    for i in range(grid.height):
        for j in range(grid.width):
            assert grid.cells[i][j] == "empty"

def test_tryAddShip() -> None:
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

def test_areCellsFree() -> None:
    grid = Grid(4, 4)
    grid.cells[2][2] = "ship"
    assert grid.areCellsFree("vertical", 2, 0, 3) == "false"
    assert grid.areCellsFree("vertical", 1, 0, 3) == "true"
    assert grid.areCellsFree("vertical", 2, 0, 1) == "true"
    assert grid.areCellsFree("orizontal", 2, 0, 3) == "false"
    assert grid.areCellsFree("orizontal", 1, 0, 3) == "true"

def test_addShip_and_move() -> None:
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

    assert grid.move(0, 1) == "hit"
    assert grid.move(1, 1) == "hit"
    assert grid.move(2, 1) == "sunk"
    assert grid.move(3, 1) == "miss"

    grid = Grid(4, 4)
    grid.cells[0][1] == "ship"
    assert grid.move(0, 1) == "miss"

def test_checkLenghtShip() -> None:
    grid = Grid(4, 4)
    assert grid.checkLenghtShip() == 0
    grid.addShip(Pair(3, 0), 2, "n")
    assert grid.checkLenghtShip() == 1
    grid.addShip(Pair(0, 1), 3, "s")
    assert grid.checkLenghtShip() == 2

def test_drawObscured(capsys) -> None:
    grid = Grid(2, 2)
    grid.cells[0][1] = "hit"
    grid.cells[1][0] = "miss"
    grid.cells[1][1] = "ship"
    grid.drawObscured()
    captured = capsys.readouterr()
    assert captured.out == "  0 1 \n0 O X \n1 M O \n\n"

def test_drawRevealed(capsys) -> None:
    grid = Grid(2, 2)
    grid.cells[0][1] = "hit"
    grid.cells[1][0] = "miss"
    grid.cells[1][1] = "ship"
    grid.drawRevealed()
    captured = capsys.readouterr()
    assert captured.out == "  0 1 \n0 O X \n1 M B \n\n"
