'''
Connect4 Gameboard Class for generating, viewing, updating and analysing the game board
Jireh Chen, 7th Nov 2024
'''


class GameBoard():

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols

        # Gameboard grid, represented by a list of Connect4Columns
        self._grid = [GameColumn(self._rows) for _ in range(cols)]
        self.linkCells()


    ## Updates the game board with the player's move
    def update(self, move, marker):

        # Verify input
        if move not in self.validMoves():
            raise ValueError(f"Invalid move of [{move}] received")
        
        # Add move to gameBoard
        columnIndex = ord(move) - ord('A')
        self._grid[columnIndex].addMove(marker)
        
        # Check result


    # Links cells in the gameboard to their adjacent cells
    def linkCells(self):
        for colIndex in range(self._cols):
            for rowIndex in range(self._rows):
                cell = self._grid[colIndex].cells[rowIndex]

                if rowIndex+1 < self._rows:
                    cell.neighbouringCells.northCell = self._grid[colIndex].cells[rowIndex+1]
                    
                    if colIndex+1 < self._cols:
                        cell.neighbouringCells.northEastCell = self._grid[colIndex+1].cells[rowIndex+1]

                if colIndex+1 < self._cols:
                    cell.neighbouringCells.eastCell = self._grid[colIndex+1].cells[rowIndex]
                    
                    if rowIndex-1 >= 0:
                        cell.neighbouringCells.southEastCell = self._grid[colIndex+1].cells[rowIndex-1]
                
                if rowIndex-1 >= 0:
                    cell.neighbouringCells.southCell = self._grid[colIndex].cells[rowIndex-1]
                    
                    if colIndex-1 >= 0:
                        cell.neighbouringCells.southWestCell = self._grid[colIndex-1].cells[rowIndex-1]

                if colIndex-1 >= 0:
                    cell.neighbouringCells.westCell = self._grid[colIndex-1].cells[rowIndex]
                    
                    if rowIndex+1 < self._rows:
                        cell.neighbouringCells.northWestCell = self._grid[colIndex-1].cells[rowIndex+1]

    ## Returns all non-full columns as their letter representations.                TODO: Can be greatly improved
    def validMoves(self):
        return [chr(ord('A') + c) for c in range(self._cols) if not self._grid[c].isFull()]
    
    ## Prints out a visual displat of the current gameBoard state
    def display(self):

        ## e.g."   A     B     C     D     E     F     G   "
        def _columnLabels():
            columnLetters = [chr(ord('A') + c) for c in range(self._cols) ]
            return "   " + "     ".join(columnLetters) + "   "

        ## e.g."   ↓     ↓     ↓     x     ↓     ↓     ↓   "
        def _columnIndicators():
            columnIndicators = ['x' if col.isFull() else '↓' for col in self._grid]
            return "   " + "     ".join(columnIndicators) + "   "

        ## e.g."+ --- + --- + --- + --- + --- + --- + --- +"
        def _gridLine():
            return " --- ".join( ["+"] * (self._cols+1) )

        contentList = [_columnLabels()]

        contentList.append(_columnIndicators())

        contentList.append(_gridLine())
        
        for r in range(self._rows):

            # e.g. "|  1  |  2  |  1  |  1  |     |     |     |"
            rowContent = [self._grid[c].rep(r) for c in range(self._cols)]
            contentList.append("|  " + "  |  ".join(rowContent) + "  |")

            contentList.append(_gridLine())

        print("\n".join(contentList))

        


# A column in a Connect4 gameboard
class GameColumn():
    def __init__(self, height):
        self._cellLimit = height
        self.nextCell = 0
        self.cells = [GameCell() for _ in range(height)]

    def rep(self, cellNum):
        if not 0 <= cellNum < self._cellLimit:
            raise ValueError(f"Cell index {cellNum} out of range")
        else:
            match self.cells[cellNum].value:
                # Empty Cell
                case 0:                                         # Note: Needs to match initial value/empty representation of GameCell().value()
                    return " "
                # Player one's token
                case 1:
                    return 1
                # Player two's token
                case 2:
                    return 2
                case _: 
                    raise ValueError("Unexpected value in Connect4 Cell")
                

    def addMove(self, marker):

        if self.isFull():
            raise ValueError("No moves available in column")

        self.cells[self.nextCell].value = marker
        self.nextCell += 1

    def isFull(self):
        if self.nextCell == self._cellLimit:
            print(f"nextCell: {self.nextCell}, cellLimit: {self._cellLimit}") 
        return self.nextCell == self._cellLimit



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
