from src.main import main
from src.grid import Grid
from src.pair import Pair
from src.ai import AI
from pytest_mock import MockerFixture
import random

def test_main1(mocker: MockerFixture, monkeypatch) -> None:
    inputList=[1, 1, "s", 6, 0, "n", 0, 2, "e", 1, 2, "s", 1, 3, "s", 2, 4, "s", 7, 7, "w", 6, 6, "n"]
    for i in range(8):
        for j in range(8):
            inputList.append(i)
            inputList.append(j)
    inputs = iter (inputList)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    randintL = [0, 0, 6, 1, 2, 3, 0, 4, 7, 0, 6, 5, 7, 7, 0, 7]
    someRandAIMoves = [63, 50, 23, 5, 40, 20, 1, 0, 6, 0, 0]
    randintL += someRandAIMoves
    for i in range(52):
        randintL.append(0)
    randint = iter (randintL)
    monkeypatch.setattr('random.randint', lambda a, b: next(randint))
    choice = iter (["s", "n", "s", "s", "e", "n", "n", "w"])
    monkeypatch.setattr('random.choice', lambda _: next(choice))
    assert main() == 0

def test_main2(mocker: MockerFixture, monkeypatch) -> None:
    inputList=[1, 1, "s", 6, 0, "n", 0, 2, "e", 1, 2, "s", 1, 3, "s", 2, 4, "s", 7, 7, "w", 6, 6, "n"]
    for i in range(8):
        for j in range(8):
            inputList.append(i)
            inputList.append(j)
    inputs = iter (inputList)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    randintL = [0, 0, 6, 1, 2, 3, 0, 4, 7, 0, 6, 5, 6, 7, 0, 7]
    for i in range(64):
        randintL.append(0)
    randint = iter (randintL)
    monkeypatch.setattr('random.randint', lambda a, b: next(randint))
    choice = iter (["s", "n", "s", "s", "e", "n", "n", "w"])
    monkeypatch.setattr('random.choice', lambda _: next(choice))
    assert main() == 0