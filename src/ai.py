import random
from pair import Pair
from grid import Grid

class AI:
    def __init__(self, grid):
        pair lastMove = null
        str lastOutcome = "miss"
        availableMoves=[]
        initAvailableMoves(grid)
    
    def initAvailableMoves(grid) --> None:
        for i in range(grid.height):
            for j in range(grid.width):
                availableMoves.append(Pair(i, j))
    
    #note: ships is an array of int which contains the lenght of each ship
    def placeShips(grid, ships) --> None:
        #TODO

    def makeMove(grid) --> None:
        if lastOutcome == "miss" or lastOutcome == "sunk":
            randomMove(grid)
        else:
            checkNeighbours(grid)
    
    def randomMove(grid) --> None:
        i = random.randint(0, len(availableMoves)-1)
        lastMove = availableMoves[i]
        lastOutcome = grid.move(lastMove.x, lastMove.y)
        del availableMoves[i]

    def checkNeighbours(grid) --> None:
        moveFound = 0
        if lastMove.x>0 and grid.cells[lastMove.x-1][lastMove.y]!="hit":
            lastMove = Pair([lastMove.x-1][lastMove.y])
        elif lastMove.x<grid.height-1 and grid.cells[lastMove.x+1][lastMove.y]!="hit":
            lastMove = Pair([lastMove.x+1][lastMove.y])
        elif lastMove.y>0 and grid.cells[lastMove.x][lastMove.y-1]!="hit":
            lastMove = Pair([lastMove.x][lastMove.y-1])
        elif lastMove.y<grid.width-1 and grid.cells[lastMove.x][lastMove.y+1]!="hit":
            lastMove = Pair([lastMove.x][lastMove.y+1])

        if moveFound == 1:
            lastOutcome = grid.move(lastMove.x, lastMove.y)
            removeLastMove()
        else:
            randomMove()

    def removeLastMove() --> None:
        for i in range(0, len(availableMoves)):
            if availableMoves[i].x == lastMove.x and availableMoves[i].y == lastMove.y:
                del availableMoves[i]
                break
