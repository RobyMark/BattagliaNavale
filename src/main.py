from curses import pair_content
from src.pair import Pair
from src.grid import Grid
from src.user import User
from src.ai import AI

def main():
    gridAi = Grid()
    gridUs = Grid()
    user = User()
    ai = AI()
    ai.placeShips(gridAi,4)
    user.placeShips(gridUs,4)
    while (gridAi.checkLenghtShip() != 0 and gridUs.checkLenghtShip() != 0):
        user.userMove(gridUs)
        ai.makeMove(gridAi)
        

if __name__ == "__main__":
    main()