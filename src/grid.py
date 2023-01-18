from src.pair import Pair
import string

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = []
        for i in range(self.height):
            self.cells.append([])
            j=0
            while j<self.width:
                self.cells[i].append("empty")
                j+=1
        self.ships = []

    def tryAddShip(self, pos, length, orientation) -> str:
        canBePlaced = "false"
        if orientation=="n" and pos.x-length>=0:
            canBePlaced = self.areCellsFree("vertical", pos.y, pos.x-length, pos.x)
        elif orientation=="s" and pos.x+length<=self.height:
            canBePlaced = self.areCellsFree("vertical", pos.y, pos.x, pos.x+length)
        elif orientation=="w" and pos.y-length>=0:
            canBePlaced = self.areCellsFree("orizontal", pos.x, pos.y-length, pos.y)
        elif orientation=="e" and (pos.y+length) <= self.width:
            canBePlaced = self.areCellsFree("orizontal", pos.x, pos.y, pos.y+length)

        if canBePlaced == "true":
            self.addShip(pos, length, orientation)
            return "success"
        return "fail"

    def areCellsFree(self, direction, z, start, end) -> str:
        if direction == "vertical":
            for i in range(start, end):
                if self.cells[i][z]=="ship":
                    return "false"
        else:
            for i in range(start, end):
                if self.cells[z][i]=="ship":
                    return "false"
        return "true"


    def addShip(self, pos, length, orientation) -> None:
        ship = []
        for k in range(0, length):
            if orientation=="n":
                self.cells[pos.x-k][pos.y]="ship"
                ship.append(Pair(pos.x-k, pos.y))
            elif orientation=="s":
                self.cells[pos.x+k][pos.y]="ship"
                ship.append(Pair(pos.x+k, pos.y))
            elif orientation=="w":
                self.cells[pos.x][pos.y-k]="ship"
                ship.append(Pair(pos.x, pos.y-k))
            elif orientation=="e":
                self.cells[pos.x][pos.y+k]="ship"
                ship.append(Pair(pos.x, pos.y+k))
        self.ships.append(ship)

    def drawRevealed(self) -> None:
        print("  ", end = '')
        for i in range(0, self.width):
            print(str(i)+" ", end = '')
        print("\n", end = '')
        for i in range(0, self.height):
            print(str(i)+" ", end = '')
            for j in range(0, self.width):
                if self.cells[i][j]=="empty":
                    print("O", end = '')
                elif self.cells[i][j]=="hit":
                    print("X", end = '')
                elif self.cells[i][j]=="ship":
                    print("B", end = '')
                elif self.cells[i][j]=="miss":
                    print("M", end = '')
                print(" ", end = '')
            print("\n", end = '')
        print("\n", end = '')

    def drawObscured(self) -> None:
        print("  ", end = '')
        for i in range(0, self.width):
            print(str(i)+" ", end = '')
        print("\n", end = '')
        for i in range(0, self.height):
            print(str(i)+" ", end = '')
            for j in range(0, self.width):
                if self.cells[i][j]=="hit":
                    print("X", end = '')
                elif self.cells[i][j]=="miss":
                    print("M", end = '')
                else:
                    print("O", end = '')
                print(" ", end = '')
            print("\n", end = '')
        print("\n", end = '')

    def move(self, x, y) -> str:
        if self.cells[x][y] == "ship":
            k = 0
            for ship in self.ships:
                n = len(ship)
                i = 0
                while i < n:
                    if ship[i].x == x and ship[i].y == y:
                        self.cells[x][y] = "hit"
                        del ship[i]
                        if len(ship) == 0:
                            del self.ships[k]
                            return "sunk"
                        return "hit"
                    i+=1
                k+=1

            print("Error: ship was not in ship list")
            return "miss"
        self.cells[x][y]="miss"
        return "miss"

    def checkLenghtShip (self) -> int :
        return len(self.ships)
