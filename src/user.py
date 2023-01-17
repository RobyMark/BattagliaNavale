from pair import Pair
from grid import Grid

class User:
    def __init__(self, name, grid):
        self.name = name
        self.lastMove = Pair(-1,-1)
        self.lastOutCome = "miss"
        self.movesY = []
        self.movesX = []
  
    def placeShips(self, grid, shipsLength) -> None:
         for shipLength in shipsLength:
            self.moveUserX = int (input("Enter where do you put your ships on X:"))
            self.moveUserY = int (input("Enter where do you put your ships on Y:"))
            self.choisePlaceShips = int (input("Enter how do you put your ships (n,s,e,o):"))
            outcome = "fail"
            i = 0
            while outcome == "fail":
                outcome = grid.tryAddShip(self.moveUserX, self.moveUserY, shipLength, self.choisePlaceShips)
                print('Error: reposition the ships again...')
                i+=1

    def makeMove(self, grid) -> None:
        count = 0
        if self.lastOutCome  == "miss" or self.lastOutCome == "sunk":
            self.userMove(grid,count)
            
    
    def userMove(self, grid, countM) -> None:
        i = 0 
        count = 1
        self.shipX = int (input("Enter the x of the enemy ships")) 
        self.shipY = int (input("Enter the y of the enemy ships"))
        for i in range(len(self.movesX)):
            if count == 1:
                self.shipX = int (input("Enter the x of the enemy ships")) 
                self.shipY = int (input("Enter the y of the enemy ships"))

            if self.shipX is self.movesX[i] and self.shipY is self.movesY[i]:
                print("the coordinate that you entered has existed. Please try again...")
                count = 1
            else :
                i += 1        
        self.movesY[countM] = self.shipX
        self.movesX[countM] = self.shipY 
        countM += 1
        self.lastOutCome = grid.move(self.shipX,self.shipY )
       

        



    