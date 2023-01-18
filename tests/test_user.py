from src.pair import Pair
from src.grid import Grid
from src.user import User
from pytest_mock import MockerFixture


def test_placeShips() -> None:
    grid = Grid(4,4)
    user = User()
    user.placeShips(grid,[2,2])
    #mocker.patch.object(input, "input", return_value="2")
    assert grid.cells[2][2] == "ship"

def test_userMove() -> None:
    grid = Grid(4,4)
    user = User()
    user.userMove(grid)
    assert grid.cells[2][2] in ("miss", "hit")

