'''
Connect4 GameCell class representing a cell on the game board
Jireh Chen, 8th Nov 2024
'''


# A cell in a Connect4 gameboard
class GameCell():

    def __init__(self):
        self.connections = {
            'vertical': 1,
            'horizontal': 1,
            'forwardDiagonal': 1,
            'backDiagonal': 1,

        }
        self.neighbours = {
            'northCell': None,                  # Redundant?
            'northEastCell': None, 
            'eastCell': None, 
            'southEastCell': None, 
            'southCell': None, 
            'southWestCell': None, 
            'westCell': None, 
            'northWestCell': None, 
        }
        self.value = 0                                           ## TODO: Could upgrade to enum

    # Scans neighbouring cells for matching tokens, updating connectionCounts in all connected cells accordingly
    def updateConnectionCounts(self):

        # Calculates vertical conections
        def updateVerticalConnections():
            # Only checks southCells, as there should be no tokens above the latest move.
            
            southCell = self.neighbours["southCell"]
            if southCell is not None and southCell.value == self.value:
                self.connections["vertical"] = 1 + southCell.connections["vertical"]

                # ***Don't have to update other cells, as vertical counts from below won't ever be accessed.***


        def updateHorizontalConnections():
            eastCell, westCell = self.neighbours["eastCell"], self.neighbours["westCell"]

            eastCount = eastCell.connections["horizontal"] if eastCell is not None and eastCell.value == self.value else 0
            westCount = westCell.connections["horizontal"] if westCell is not None and westCell.value == self.value else 0
            
            horizontalConnections = westCount + 1 + eastCount
            self.connections["horizontal"] = horizontalConnections

            for _ in range(eastCount):
                eastCell.connections["horizontal"] = horizontalConnections
                if not eastCell.neighbours["eastCell"] == None:
                    eastCell = eastCell.neighbours["eastCell"]

            for _ in range(westCount):
                westCell.connections["horizontal"] = horizontalConnections
                if not westCell.neighbours["eastCell"] == None:
                    westCell = westCell.neighbours["eastCell"]

                
        def updateforwardDiagonalConnections():
            northEastCell, southWestCell = self.neighbours["northEastCell"], self.neighbours["southWestCell"]

            northEastCount = northEastCell.connections["forwardDiagonal"] if northEastCell is not None and northEastCell.value == self.value else 0
            southWestCount = southWestCell.connections["forwardDiagonal"] if southWestCell is not None and southWestCell.value == self.value else 0
            
            forwardDiagonalConnections = southWestCount + 1 + northEastCount
            self.connections["forwardDiagonal"] = forwardDiagonalConnections

            for _ in range(northEastCount):
                northEastCell.connections["forwardDiagonal"] = forwardDiagonalConnections
                if not northEastCell.neighbours["eastCell"] == None:
                    northEastCell = northEastCell.neighbours["eastCell"]

            for _ in range(southWestCount):
                southWestCell.connections["forwardDiagonal"] = forwardDiagonalConnections
                if not southWestCell.neighbours["eastCell"] == None:
                    southWestCell = southWestCell.neighbours["eastCell"]



        def updateBackwardDiagonalConnections():
            northWestCell, southEastCell = self.neighbours["northWestCell"], self.neighbours["southEastCell"]

            northWestCount = northWestCell.connections["backwardDiagonal"] if northWestCell is not None and northWestCell.value == self.value else 0
            southEastCount = southEastCell.connections["backwardDiagonal"] if southEastCell is not None and southEastCell.value == self.value else 0
            
            backwardDiagonalConnections = southEastCount + 1 + northWestCount
            self.connections["backwardDiagonal"] = backwardDiagonalConnections

            for _ in range(northWestCount):
                northWestCell.connections["backwardDiagonal"] = backwardDiagonalConnections
                if not northWestCell.neighbours["eastCell"] == None:
                    northWestCell = northWestCell.neighbours["eastCell"]

            for _ in range(southEastCount):
                southEastCell.connections["backwardDiagonal"] = backwardDiagonalConnections
                if not southEastCell.neighbours["eastCell"] == None:
                    southEastCell = southEastCell.neighbours["eastCell"]
            


        # Update connections using above functions
                    
        if self.value == None:                                   
            raise ValueError("updateConnectionCounts is being called on a cell without a player token")

        updateVerticalConnections()
        updateHorizontalConnections()
        updateforwardDiagonalConnections()
        updateBackwardDiagonalConnections()

        for connectionCount in self.connections.values():
            if connectionCount >= 4:
                print(f"Won with connection count {connectionCount}")
                return "Win"