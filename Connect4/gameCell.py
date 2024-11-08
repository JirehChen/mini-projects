'''
Connect4 GameCell class representing a cell on the game board
Jireh Chen, 8th Nov 2024
'''


# A cell in a Connect4 gameboard
class GameCell():

    def __init__(self):
        self.connectionCounts = {
            'verticalCount': 1,
            'horizontalCount': 1,
            'forwardDiagonalCount': 1,
            'backDiagonal': 1,

        }
        self.neighbouringCells = {
            'northCell': None, 
            'northEastCell': None, 
            'eastCell': None, 
            'southEastCell': None, 
            'southCell': None, 
            'southWestCell': None, 
            'westCell': None, 
            'northWestCell': None, 
        }
        self.value = 0                                           ## Could upgrade with enum? 

    def updateConnections(self):

        pass
