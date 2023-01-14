from pair import Pair

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

        def tryAddShip(pos, length, orientation) --> str:
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

        def areCellsFree(direction, z, start, end) --> str:
            if direction == "vertical":
                for i in range(start, end):
                    if cells[i][z]=="ship"
                        return
            else:
                for i in range(start, end):
                    if cells[z][i]=="ship"
                        return "false"
            return "true"


        def addShip(pos, length, orientation) --> None:
            ship = []
            for k in range(0, length)
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

        def drawRevealed() --> None:
            #TODO
        def drawObscured() --> None:
            #TODO