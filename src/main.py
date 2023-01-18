from curses import pair_content
from src.pair import Pair
from src.grid import Grid
from src.user import User
from src.ai import AI

def main():
    grid = Grid()
    user = User()
    ai = AI()

    ai.placeShips(grid)
    


if __name__ == "__main__":
    main()