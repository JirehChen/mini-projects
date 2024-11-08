'''
Connect4 Gamebaord Class for generating, viewing, updating and analysing the game board
Jireh Chen, 7th Nov 2024
'''


class GameBoard():

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols

        # Gameboard grid, represented by a list of Connect4Columns
        self._grid = [Connect4Column(self._rows) for _ in range(cols)]

    ## Updates the game board with the player's move
    def update(self, move, marker):

        # Verify input
        if move not in self.validMoves:
            raise ValueError(f"Invalid move of [{move}] received")
        
        # Add move to gameBoard
        columnIndex = ord(move) - ord('A')
        self._grid[columnIndex].addMove(marker)
        
        # Check result



    ## Returns all non-full columns as their letter representations.                TODO: Can be greatly improved
    def validMoves(self):
        return [chr(ord('A') + c) for c in range(self._cols) if not self._grid[c].isFull]
    
    ## Prints out a visual displat of the current gameBoard state
    def display(self):

        contentList = [_columnLabels()]

        contentList.append(_columnIndicators())

        contentList.append(_gridLine())
        
        for r in range(self._rows):

            # e.g. "|  1  |  2  |  1  |  1  |     |     |     |"
            rowContent = [self._grid[c].rep(r) for c in range(self._cols)]
            contentList.append("|  " + "  |  ".join(rowContent) + "  |")

            contentList.append(_gridLine())

        print("\n".join(contentList))

        ## e.g."   A     B     C     D     E     F     G   "
        def _columnLabels():
            columnLetters = [chr(ord('A') + c) for c in range(self._cols) ]
            return "   " + "     ".join(columnLetters) + "   "

        ## e.g."   ↓     ↓     ↓     x     ↓     ↓     ↓   "
        def _columnIndicators():
            columnIndicators = ['x' if col.isFull else '↓' for col in self._grid]
            return "   " + "     ".join(columnIndicators) + "   "

        ## e.g."+ --- + --- + --- + --- + --- + --- + --- +"
        def _gridLine():
            return " --- ".join( ["+"] * (self._cols+1) )


## A column with 1 extra cell (@index 0) representing the next empty cell in the column
class Connect4Column():
    def __init__(self, height):
        self._cellLimit = height
        self.nextCell = 0
        self._cells = [0]*height

    def rep(self, cellNum):
        if not 0 <= cellNum < self._cellLimit:
            raise ValueError(f"Cell index {cellNum} out of range")
        else:
            match self._cells[cellNum]:
                # Empty Cell
                case 0: 
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

        self._cells[self.nextCell] = marker
        self.nextCell += 1

    def isFull(self):
        return self.nextCell == self._cellLimit
