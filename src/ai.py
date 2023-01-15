import random
from src.pair import Pair
from src.grid import Grid

class AI:
    def __init__(self, grid):
        self.lastMove = Pair(-1, -1)
        self.lastOutcome = "miss"
        self.availableMoves=[]
        initAvailableMoves(grid)

    def initAvailableMoves(self, grid) -> None:
        for i in range(grid.height):
            for j in range(grid.width):
                self.availableMoves.append(Pair(i, j))

    #note: shipsLength is an array of int which contains the lenght of each ship
    def placeShips(self, grid, shipsLength, attempts=50) -> None:
        for shipLength in shipsLength:
            outcome = "fail"
            i = 0
            while outcome == "fail" and i<attempts:
                outcome = grid.tryAddShip(randint(0, height-1), randint(0, width-1), shipLength, random.choice(["n", "s", "w", "e"]))
                i+=1

    def makeMove(self, grid) -> None:
        if self.lastOutcome == "miss" or self.lastOutcome == "sunk":
            randomMove(grid)
        else:
            checkNeighbours(grid)

    def randomMove(self, grid) -> None:
        i = random.randint(0, len(self.availableMoves)-1)
        self.lastMove = self.availableMoves[i]
        self.lastOutcome = grid.move(self.lastMove.x, self.lastMove.y)
        del self.availableMoves[i]

    def checkNeighbours(self, grid) -> None:
        moveFound = 0
        if self.lastMove.x>0 and grid.cells[self.lastMove.x-1][self.lastMove.y]!="hit":
            self.lastMove = Pair([self.lastMove.x-1][self.lastMove.y])
        elif self.lastMove.x<grid.height-1 and grid.cells[self.lastMove.x+1][self.lastMove.y]!="hit":
            self.lastMove = Pair([self.lastMove.x+1][self.lastMove.y])
        elif self.lastMove.y>0 and grid.cells[self.lastMove.x][self.lastMove.y-1]!="hit":
            self.lastMove = Pair([self.lastMove.x][self.lastMove.y-1])
        elif self.lastMove.y<grid.width-1 and grid.cells[self.lastMove.x][self.lastMove.y+1]!="hit":
            self.lastMove = Pair([self.lastMove.x][self.lastMove.y+1])

        if moveFound == 1:
            lastOutcome = grid.move(self.lastMove.x, self.lastMove.y)
            removeLastMove()
        else:
            randomMove()

    def removeLastMove(self) -> None:
        for i in range(0, len(self.availableMoves)):
            if self.availableMoves[i].x == self.lastMove.x and self.availableMoves[i].y == self.lastMove.y:
                del self.availableMoves[i]
                break
