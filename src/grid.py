from pair import Pair
import string

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        cells = []
        for i in range(grid.height):
            cells[i] = []
            for j in range(grid.width):
                cells[i][j] = "empty"
        ships = []

        def tryAddShip(pos, length, orientation) -> str:
            canBePlaced = "true"
            if orientation=="n":
                if pos.x-length>=0:
                    canBePlaced = areCellsFree("vertical", pos.y, pos.x-length, pos.x)
            elif orientation=="s":
                if pos.x+length<height:
                    canBePlaced = areCellsFree("vertical", pos.y, pos.x, pos.x+length)
            elif orientation=="w":
                if pos.y-length>=0:
                    canBePlaced = areCellsFree("orizontal", pos.x, pos.y-length, pos.y)
            elif orientation=="e":
                if pos.y+length<width:
                    canBePlaced = areCellsFree("orizontal", pos.x, pos.y, pos.y+length)

            if canBePlaced == "true":
                addShip(pos, length, orientation)
                return "success"
            else:
                return "fail"

        def areCellsFree(direction, z, start, end) -> str:
            if direction == "vertical":
                for i in range(start, end):
                    if cells[i][z]=="ship":
                        return
            else:
                for i in range(start, end):
                    if cells[z][i]=="ship":
                        return "false"
            return "true"


        def addShip(pos, length, orientation) -> None:
            ship = []
            for k in range(0, length):
                if orientation=="n":
                    cells[pos.x-k][pos.y]="ship"
                    ship.append(Pair(pos.x-k, pos.y))
                elif orientation=="s":
                    cells[pos.x+k][pos.y]="ship"
                    ship.append(Pair(pos.x+k, pos.y))
                elif orientation=="w":
                    cells[pos.x][pos.y-k]="ship"
                    ship.append(Pair(pos.x, pos.y-k))
                elif orientation=="e":
                    cells[pos.x][pos.y+k]="ship"
                    ship.append(Pair(pos.x, pos.y+k))
            ships.append(ship)

        def drawRevealed() -> None:
            print("  ")
            for i in range(0, width):
                print(string.ascii_lowercase[i]+" ")
            print("\n")
            for i in range(0, height):
                print(i+" ")
                for j in range(0, width):
                    if cells[i][j]=="empty":
                        print("O")
                    elif cells[i][j]=="hit":
                        print("X")
                    elif cells[i][j]=="ship":
                        print("B")
                    elif cells[i][j]=="miss":
                        print("M")
                    print(" ")
                print("\n")
            print("\n")
            
        def drawObscured() -> None:
            #TODO

        def move(x, y) -> str:
            if cells[x][y]=="ship":
                for ship in ships:
                    for i in range(0, len(ship)):
                        if ship[i].x=x and ship[i].y=y:
                            cells[x][y]="hit"
                            del ship[i]
                            if len(ship)==0:
                                return "sunk"
                            else:
                                return "hit"
            else:
                cells[i][j]="miss"
                return "miss"
