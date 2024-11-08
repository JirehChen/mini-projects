'''
Connect4 GameCell class representing a cell on the game board
Jireh Chen, 8th Nov 2024
'''


# A cell in a Connect4 gameboard
class GameCell():

    def __init__(self):
        self.connectionCounts = ConnectionCounts()
        self.neighbouringCells = NeighbouringCells()
        self.value = 0                                           ## Could upgrade with enum? 



class ConnectionCounts():
    def __init__(self):
        self.verticalCount = 1
        self.horizontalCount = 1
        self.rightDiagonalCount = 1
        self.leftDiagonalCount = 1


class NeighbouringCells():
    def __init__(self):
        self.northCell = None
        self.northEastCell = None
        self.eastCell = None
        self.southEastCell = None
        self.southCell = None
        self.southWestCell = None
        self.westCell = None
        self.northWestCell = None
