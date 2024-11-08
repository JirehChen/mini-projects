'''
Connect4 Gamebaord Class for generating, viewing, updating and analysing the game board
Jireh CHen, 7th Nov 2024
'''


class GameBoard():

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols

        # Gameboard grid, represented by a list of Connect4Columns
        self._grid = [Connect4Column(self._rows) for _ in range(cols)]
    
    ## Processes the player's on the game board
    def update(self, move):
        pass

    ## Outputs a visual representation of the current gameBoard state
    ''' e.g. Sample Board Display:
           A     B     C     D     E     F     G
           ↓     ↓     x     x     ↓     ↓     ↓
        + --- + --- + --- + --- + --- + --- + --- +    
        |     |     |  2  |  1  |     |     |     |
        + --- + --- + --- + --- + --- + --- + --- +    
        |  1  |  2  |  1  |  1  |     |     |     |
        + --- + --- + --- + --- + --- + --- + --- +    '''
    def display(self):
        contentList = [self._columnLetters()]
        contentList.append(self._columnIndicators())

        contentList.append(self._gridLine())

        for r in range(1, self._rows+1):
            # Add cells from row r
            rowContent = [self._grid[c].rep(r) for c in range(self._cols)]
            contentList.append("|  " + "  |  ".join(rowContent) + "  |")

            contentList.append(self._gridLine())
        print("\n".join(contentList))

    ## Returns all non-full columns as their letter representations.                TODO: Can be improved
    def validMoves(self):
        return [chr(ord('A') + c) for c in range(self._cols) if not self._grid[c].isFull]

    ## Visual string representation of gameboard column (letter) labels         e.g."   A     B     C     D     E     F     G   "
    def _columnLetters(self):
        columnLetters = [chr(ord('A') + c) for c in range(self._cols)]
        return "   " + "     ".join(columnLetters) + "   "
    
    ## Visual string representation of which columns a move can be made in.     e.g."   ↓     ↓     ↓     x     ↓     ↓     ↓   "
    def _columnIndicators(self):
        columnIndicators = ['x' if col.isFull else '↓' for col in self._grid]
        return "   " + "     ".join(columnIndicators) + "   "

    ## Visual string representation of horizontal gridlines between cells       e.g."+ --- + --- + --- + --- + --- + --- + --- +"
    def _gridLine(self):
        return " --- ".join( ["+"] * (self._cols+1) )


## A column with 1 extra cell (@index 0) representing the next empty cell in the column
class Connect4Column():
    def __init__(self, height):
        self.isFull = False
        self._maxCells = height
        self._cells = [0]*(height+1)

    def rep(self, cellNum):
        if not 0 < cellNum <= self._maxCells:
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





