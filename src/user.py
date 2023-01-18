from src.pair import Pair

class User:
    def __init__(self):
        self.lastMove = Pair(-1,-1)
        self.lastOutcome = "miss"

    def placeShips(self, grid, shipsLength) -> None:
        print ("Lenghts of ships to place: ")
        print (shipsLength)
        for shipLength in shipsLength:
            print ("Lenght of ship to place: " + str(shipLength))
            outcome = "fail"
            while outcome == "fail":
                moveUserX = int (input("Enter where do you put your ships on X: "))
                moveUserY = int (input("Enter where do you put your ships on Y: "))
                choicePlaceShips = input("Enter the orientazion your ships (n,s,e,o): ")
                outcome = grid.tryAddShip(Pair(moveUserX, moveUserY), shipLength, choicePlaceShips)
                if outcome == "fail":
                    print('Error: reposition the ships again...')
            grid.drawRevealed()

    def userMove(self, grid) -> None:
        outcome = "fail"
        while outcome == "fail":
            shipX = int (input("Enter the x of the enemy ships: "))
            shipY = int (input("Enter the y of the enemy ships: "))
            if shipX<0 or shipX>=grid.height or shipY<0 or shipY>=grid.width or grid.cells[shipX][shipY] in ("miss", "hit"):
                print("Invalid or existing coordinates. Please try again...")
            else:
                outcome = "success"
        self.lastMove.x = shipX
        self.lastMove.y = shipY
        self.lastOutcome = grid.move(shipX, shipY)
