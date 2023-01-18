from src.pair import Pair
from src.grid import Grid
from src.user import User
from pytest_mock import MockerFixture

def test_placeShips(monkeypatch) -> None:
    grid = Grid(4,4)
    user = User()
    inputs = iter ([1, 1, "s", 0, 0, "n", 3, 3, "n"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    user.placeShips(grid,[2,2])
    assert len(grid.ships) == 2

def test_userMove(mocker: MockerFixture, monkeypatch) -> None:
    grid = Grid(4,4)
    user = User()
    inputs = iter ([1, 1, 1, 1, 3, 3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    spy = mocker.spy(grid, "move")
    assert grid.cells[1][1] == "empty"
    user.userMove(grid)
    assert grid.cells[1][1] == "miss"
    assert spy.call_count == 1
    user.userMove(grid)
    assert grid.cells[3][3] == "miss"
    assert spy.call_count == 2
