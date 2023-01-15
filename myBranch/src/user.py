from turtle import hideturtle, position
from pair import Pair
from grid import Grid

class User():
    def __init__(self, name, grid):
        self.name = name
        pair lastMove = null
        str  lastOutcome = "miss"
        movesY = []
        movesX = []

    def initAvailableMoves(grid) -> None:
        for i in range(grid.height):
            for j in range(grid.width):
                availableMoves.append(Pair(i, j))
     
    def placeShips(grid, shipsLength, attempts=50) -> None:
         for shipLength in shipsLength:
            moveUserX = int(input("Enter where do you put your ships on X:"))
            moveUserY = int(input("Enter where do you put your ships on Y:"))
            choisePlaceShips = int(input("Enter how do you put your ships (n,s,e,o):"))
            outcome = "fail"
            i = 0
            while outcome == "fail" and i<attempts:
                outcome = grid.tryAddShip(moveUserX, moveUserY, shipLength, choisePlaceShips)
                i+=1

    def makeMove(grid) -> None:
        if lastOutcome == "miss" or lastOutcome == "sunk":
            userMove(grid)
        else:
            checkNeighbours(grid)
    
    def userMove(grid, countM) -> None:
        i = 0 
        count = 1
        positionXofShapes = int (input("Enter the x of the avvers shapes")) 
        positionYofShapes = int (input("Enter the y of the avvers shapes"))
        for i in range(len(movesX)):
            if count is 1:
                positionXofShapes = int (input("Enter the x of the avvers shapes")) 
                positionYofShapes = int (input("Enter the y of the avvers shapes"))

            if positionXofShapes is movesX[i] and positionYofShapes is movesY[i]:
                print("the coordinate that you entered has existed. Please try again...")
                count = 1
            else :
                i += 1        
        movesY[countM] = positionYofShapes
        movesX[countM] = positionXofShapes
        countM += 1
        lastOutCome = grid.move(positionXofShapes,positionYofShapes)
       

        



    