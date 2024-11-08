'''
Connect4 GameColumn Class representing a column on the game board
Jireh Chen, 8th Nov 2024
'''
from gameCell import GameCell

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

        # Update target cell
        cell = self.cells[self.nextCell]
        cell.value = marker
        moveResult = cell.updateConnectionCounts()

        self.nextCell += 1

        return moveResult


    def isFull(self):
        if self.nextCell == self._cellLimit:
            print(f"nextCell: {self.nextCell}, cellLimit: {self._cellLimit}") 
        return self.nextCell == self._cellLimit

