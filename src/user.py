from src.pair import Pair
from src.grid import Grid

class User:
    def __init__(self):
        self.lastMove = Pair(-1,-1)
        self.lastOutcome = "miss"

    def placeShips(self, grid, shipsLength) -> None:
         for shipLength in shipsLength:
            outcome = "fail"
            while outcome == "fail":
                self.moveUserX = int (input("Enter where do you put your ships on X:"))
                self.moveUserY = int (input("Enter where do you put your ships on Y:"))
                self.choicePlaceShips = input("Enter how do you put your ships (n,s,e,o):")
                outcome = grid.tryAddShip(Pair(self.moveUserX, self.moveUserY), shipLength, self.choicePlaceShips)
                if outcome == "fail":
                    print('Error: reposition the ships again...')

    def userMove(self, grid) -> None:
        outcome = "fail"
        while outcome == "fail":
            shipX = int (input("Enter the x of the enemy ships")) 
            shipY = int (input("Enter the y of the enemy ships"))
            if grid.cells[shipX][shipY] in ("miss", "hit"):
                print("the coordinate that you entered has existed. Please try again...")
            else:
                outcome = "success"
        self.lastOutcome = grid.move(shipX, shipY)
