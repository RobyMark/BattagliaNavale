from src.pair import Pair

def test_pair() -> None:
    p = Pair(1, 5)
    assert p.x == 1
    assert p.y == 5

def test_pairX() -> None:
    p = Pair(1, 5)
    assert p.getX() == 1

def test_pairX() -> None:
    p = Pair(1, 5)
    assert p.getY() == 5
