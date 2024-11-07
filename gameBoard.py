


class GameBoard():
    _rows = 6
    _cols = 7
    _grid = []               # Needs to be [] for correct bahaviour in __init__(self, rows, cols)

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        
        # Automatically generates in grid, an empty board with the specified dimensions (or 6x7 by default)
        for _ in cols:
            self._grid += [[0]*rows]
    
    ## Outputs a visual representation of the current gameBoard state
    def display():
        pass

    ## Processes the player's on the game board
    def update():
        pass