from pair import Pair
from grid import Grid

class User:
    def __init__(self, name, grid):
        self.name = name
        self.lastMove = Pair(-1,-1)
        self.lastOutCome = "miss"
        self.movesY = []
        self.movesX = []
        self.initAvailableMoves(grid)

    def initAvailableMoves(self, grid) -> None:
        for i in range(grid.height):
            for j in range(grid.width):
                self.availableMoves.append(Pair(i, j))
     
    def placeShips(self, grid, shipsLength, attempts=50) -> None:
         for shipLength in shipsLength:
            self.moveUserX = int (input("Enter where do you put your ships on X:"))
            self.moveUserY = int (input("Enter where do you put your ships on Y:"))
            self.choisePlaceShips = int (input("Enter how do you put your ships (n,s,e,o):"))
            outcome = "fail"
            i = 0
            while outcome == "fail" and i<attempts:
                outcome = grid.tryAddShip(self.moveUserX, self.moveUserY, shipLength, self.choisePlaceShips)
                i+=1

    def makeMove(self, grid) -> None:
        count = 0
        if self.lastOutCome  == "miss" or self.lastOutCome == "sunk":
            self.userMove(grid,count)
            
    
    def userMove(self, grid, countM) -> None:
        i = 0 
        count = 1
        self.positionXofShapes = int (input("Enter the x of the avvers shapes")) 
        self.positionYofShapes = int (input("Enter the y of the avvers shapes"))
        for i in range(len(self.movesX)):
            if count == 1:
                self.positionXofShapes = int (input("Enter the x of the avvers shapes")) 
                self.positionYofShapes = int (input("Enter the y of the avvers shapes"))

            if self.positionXofShapes is self.movesX[i] and self.positionYofShapes is self.movesY[i]:
                print("the coordinate that you entered has existed. Please try again...")
                count = 1
            else :
                i += 1        
        self.movesY[countM] = self.positionYofShapes
        self.movesX[countM] = self.positionXofShapes
        countM += 1
        self.lastOutCome = grid.move(self.positionXofShapes,self.positionYofShapes)
       

        



    