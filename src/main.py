from src.pair import Pair
from src.grid import Grid
from src.user import User
from src.ai import AI

def main():
    gridAi = Grid(8, 8)
    gridUs = Grid(8, 8)
    user = User()
    ai = AI(gridAi)
    ships = [5, 5, 4, 4, 3, 3, 2, 2]
    ai.placeShips(gridAi, ships)
    gridUs.drawRevealed()
    user.placeShips(gridUs, ships)
    print("START!\n")
    gridAi.drawObscured()
    gridUs.drawRevealed()
    while True:
        user.userMove(gridAi)
        if gridAi.checkLenghtShip() == 0:
            print("You win!")
            break
        ai.makeMove(gridUs)
        if gridUs.checkLenghtShip() == 0:
            print("You lose...")
            break
        gridAi.drawObscured()
        gridUs.drawRevealed()
        print("Enemy's last move: " + str(ai.lastMove.x) + ", " + str(ai.lastMove.y))
        print("Enemy's last outcome: " + ai.lastOutcome)
        print("Your last move: " + str(user.lastMove.x) + ", " + str(user.lastMove.y))
        print("Your last outcome: " + user.lastOutcome)

if __name__ == "__main__":
    main()
