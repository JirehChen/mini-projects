'''
Connect4 GameController class that is responsible for the game playing process
'''
from gameBoard import GameBoard

class GameController:
    _gameBoard = None
    _playerNames = None

    def __init__(self, gameBoard, playerNames):
        self._gameBoard = gameBoard    
        self._playerNames = playerNames

    def run(self):
        currentPlayer = 1                           # TODO: Can be upgraded... ENUM? or New class.. Overkill?
        currentPlayerMove = None
        print("Player 1 - {} - starts".format(self._playerNames[1]))

        gameInProgress = True
        while gameInProgress:
            
            (self._gameBoard).display()
            
            currentPlayerMove = self._promptForMove()
            
            moveResult = self._gameBoard.update(currentPlayerMove)

            if moveResult != None:
                self._endGame(moveResult, currentPlayer)
            else:
                currentPlayer = currentPlayer%2+1           # TODO: Not the most efficient? 

            gameInProgress = False                  #TODO: Temporary infinite loop prevention - to be removed once preceding functions are implemented

    ## Prompts the currentPlayer to select their move
    def _promptForMove(self):
        return

    ## Ends the game according the the current player and the result they achieved (Win/Draw/Terminated))
    def _endGame(self, result, player):
        pass        
        