from src.pair import Pair
import string

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = []
        for i in range(self.height):
            self.cells[i] = []
            for j in range(self.width):
                self.cells[i][j] = "empty"
        self.ships = []

    def tryAddShip(self, pos, length, orientation) -> str:
        canBePlaced = "true"
        if orientation=="n":
            if pos.x-length>=0:
                canBePlaced = self.areCellsFree("vertical", pos.y, pos.x-length, pos.x)
        elif orientation=="s":
            if pos.x+length<height:
                canBePlaced = self.areCellsFree("vertical", pos.y, pos.x, pos.x+length)
        elif orientation=="w":
            if pos.y-length>=0:
                canBePlaced = self.areCellsFree("orizontal", pos.x, pos.y-length, pos.y)
        elif orientation=="e":
            if pos.y+length<width:
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
        print("  ")
        for i in range(0, width):
            print(string.ascii_lowercase[i]+" ")
        print("\n")
        for i in range(0, height):
            print(i+" ")
            for j in range(0, width):
                if self.cells[i][j]=="empty":
                    print("O")
                elif self.cells[i][j]=="hit":
                    print("X")
                elif self.cells[i][j]=="ship":
                    print("B")
                elif self.cells[i][j]=="miss":
                    print("M")
                print(" ")
            print("\n")
        print("\n")

    def drawObscured(self) -> None:
        #TODO
        self.drawRevealed() #to remove

    def move(self, x, y) -> str:
        if self.cells[x][y]=="ship":
            for ship in self.ships:
                for i in range(0, len(ship)):
                    if ship[i].x==x and ship[i].y==y:
                        self.cells[x][y]="hit"
                        del ship[i]
                        if len(ship)==0:
                            return "sunk"
                        return "hit"
            print("Error: ship was not in ship list")
            return "miss"
        else:
            self.cells[i][j]="miss"
            return "miss"
