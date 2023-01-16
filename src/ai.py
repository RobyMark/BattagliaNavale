import random
from src.pair import Pair

class AI:
    def __init__(self, grid):
        self.lastMove = Pair(-1, -1)
        self.lastOutcome = "miss"
        self.availableMoves=[]
        self.initAvailableMoves(grid)

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
                outcome = grid.tryAddShip(Pair(random.randint(0, grid.height-1), random.randint(0, grid.width-1)), shipLength, random.choice(["n", "s", "w", "e"]))
                i+=1

    def makeMove(self, grid) -> None:
        if self.lastOutcome in ("miss", "sunk"):
            self.randomMove(grid)
        else:
            self.checkNeighbours(grid)

    def randomMove(self, grid) -> None:
        i = random.randint(0, len(self.availableMoves)-1)
        self.lastMove = self.availableMoves[i]
        self.lastOutcome = grid.move(self.lastMove.x, self.lastMove.y)
        del self.availableMoves[i]

    def checkNeighbours(self, grid) -> None:
        moveFound = 0
        oldLastMove=lastMove
        if self.lastMove.x>0 and grid.cells[self.lastMove.x-1][self.lastMove.y] not in ("hit", "miss"):
            self.lastMove = Pair(self.lastMove.x-1, self.lastMove.y)
            moveFound = 1
        elif self.lastMove.x<grid.height-1 and grid.cells[self.lastMove.x+1][self.lastMove.y] not in ("hit", "miss"):
            self.lastMove = Pair(self.lastMove.x+1, self.lastMove.y)
            moveFound = 1
        elif self.lastMove.y>0 and grid.cells[self.lastMove.x][self.lastMove.y-1] not in ("hit", "miss"):
            self.lastMove = Pair(self.lastMove.x, self.lastMove.y-1)
            moveFound = 1
        elif self.lastMove.y<grid.width-1 and grid.cells[self.lastMove.x][self.lastMove.y+1] not in ("hit", "miss"):
            self.lastMove = Pair(self.lastMove.x, self.lastMove.y+1)
            moveFound = 1

        if moveFound == 1:
            self.lastOutcome = grid.move(self.lastMove.x, self.lastMove.y)
            self.removeLastMove()
            if lastOutcome == "miss"
                lastMove=oldLastMove
                lastOutcome = "hit"
        else:
            self.randomMove(grid)

    def removeLastMove(self) -> None:
        n=len(self.availableMoves)
        for i in range(n):
            if self.availableMoves[i].x == self.lastMove.x and self.availableMoves[i].y == self.lastMove.y:
                del self.availableMoves[i]
                break
