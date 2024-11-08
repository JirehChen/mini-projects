'''
Connect4 Gameboard Class for generating, viewing, updating and analysing the game board
Jireh Chen, 7th Nov 2024
'''
from gameColumn import GameColumn

class GameBoard():

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols

        # Gameboard grid, represented by a list of Connect4Columns
        self._grid = [GameColumn(self._rows) for _ in range(cols)]
        self.linkCells()


    ## Updates the game board with the player's move
    def update(self, move, marker):

        if move not in self.validMoves():
            raise ValueError(f"Invalid move of [{move}] received")
        
        # Add move to gameBoard
        columnIndex = ord(move) - ord('A')
        moveResult = self._grid[columnIndex].addMove(marker)

        if moveResult is None and self.validMoves == []:
            moveResult = "Draw"

        return moveResult
        

    ## Links cells in the gameboard to their adjacent cells
    def linkCells(self):
        for colIndex in range(self._cols):
            for rowIndex in range(self._rows):
                cell = self._grid[colIndex].cells[rowIndex]

                if rowIndex+1 < self._rows:
                    cell.neighbours["northCell"] = self._grid[colIndex].cells[rowIndex+1]
                    
                    if colIndex+1 < self._cols:
                        cell.neighbours["northEastCell"] = self._grid[colIndex+1].cells[rowIndex+1]

                if colIndex+1 < self._cols:
                    cell.neighbours["eastCell"] = self._grid[colIndex+1].cells[rowIndex]
                    
                    if rowIndex-1 >= 0:
                        cell.neighbours["southEastCell"] = self._grid[colIndex+1].cells[rowIndex-1]
                
                if rowIndex-1 >= 0:
                    cell.neighbours["southCell"] = self._grid[colIndex].cells[rowIndex-1]
                    
                    if colIndex-1 >= 0:
                        cell.neighbours["southWestCell"] = self._grid[colIndex-1].cells[rowIndex-1]

                if colIndex-1 >= 0:
                    cell.neighbours["westCell"] = self._grid[colIndex-1].cells[rowIndex]
                    
                    if rowIndex+1 < self._rows:
                        cell.neighbours["northWestCell"] = self._grid[colIndex-1].cells[rowIndex+1]


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
        
        # Ranged is reversed, as row 0 appears at the bottom of the game board
        for r in reversed(range(self._rows)):

            # e.g. "|  1  |  2  |  1  |  1  |     |     |     |"
            rowContent = [str(self._grid[c].rep(r)) for c in range(self._cols)]
            contentList.append("|  " + "  |  ".join(rowContent) + "  |")

            contentList.append(_gridLine())

        print("\n\n" + "\n".join(contentList))