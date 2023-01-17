from src.pair import Pair
from src.grid import Grid

class User:
    def __init__(self):
        self.lastMove = Pair(-1,-1)
        self.lastOutCome = "miss"
       
  
    def placeShips(self, grid, shipsLength) -> None:
         for shipLength in shipsLength:
            outcome = "fail"
            while outcome == "fail":
                self.moveUserX = int (input("Enter where do you put your ships on X:"))
                self.moveUserY = int (input("Enter where do you put your ships on Y:"))
                self.choisePlaceShips = input("Enter how do you put your ships (n,s,e,o):")
                outcome = grid.tryAddShip(Pair(self.moveUserX,self.moveUserY), shipLength, self.choisePlaceShips)
                if outcome == "fail":
                    print('Error: reposition the ships again...')
                
    def userMove(self, grid) -> None:
        self.shipX = int (input("Enter the x of the enemy ships")) 
        self.shipY = int (input("Enter the y of the enemy ships"))
        outcome = "fail"
        while outcome == "fail":
                self.shipX = int (input("Enter the x of the enemy ships")) 
                self.shipY = int (input("Enter the y of the enemy ships"))

                if grid.cells[self.shipX][self.shipY] in ("miss", "hit"):
                    print("the coordinate that you entered has existed. Please try again...")
                else:
                    outcome = "success"     

        self.lastOutCome = grid.move(self.shipX,self.shipY)
       

        



    