from src.pair import Pair
from src.grid import Grid
from src.user import User
from pytest_mock import MockerFixture


def test_placeShips() -> None:
    grid = Grid(4,4)
    user = User(grid)
    user.placeShips(grid,[2,2])
    mocker.patch.object(input, "input", return_value="2")
    assert grid.cells[2,2] == "ships"

