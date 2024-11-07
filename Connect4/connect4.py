'''
A quick project: A rudimentary game of Connect 4, run in the terminal, for two players.
Jireh Chen, 6th Nov 2024
'''
from gameBoard import GameBoard

class Connect4():
    _nameOfPlayer = {1:'Player 1', 2:'Player 2'}    
    _gameDimensions = {'rows': 6, 'cols': 7}
    _gameBoard = None                               # Risky? 

    def play(self):
        self._setUpGame()
        self._runGame()
        return 

    def _setUpGame(self):
        self._welcome()
        self._namePlayers()
        self._gameBoard = GameBoard(self._gameDimensions.get('rows'), self._gameDimensions.get('cols') )                                
        return
    
    def _runGame(self):
        currentPlayer = 1                           # TODO: Can be upgraded... ENUM? or New class.. Overkill?
        currentPlayerMove = None
        print("Player 1 - {nameOfPlayer[1]} - starts")

        gameInProgress = True
        while gameInProgress:
            
            self._gameBoard.display()
            
            currentPlayerMove = promptForMove()
            
            moveResult = self._gameBoard.update(currentPlayerMove)

            if moveResult != None:
                endGame(moveResult, currentPlayer)
            else:
                currentPlayer = currentPlayer%2+1           # TODO: Not the most efficient? 

            gameInProgress = False                  #TODO: Temporary infinite loop prevention - to be removed once preceding functions are implemented
            

        ## Prompts the currentPlayer to select their move
        def promptForMove():
            pass

        ## Ends the game according the the current player and the result they achieved (Win/Draw/Terminated))
        def endGame(result, player):
            pass        


    def _welcome():
        print("Welcome to a new game of Connect 4 for two players/n/n")
    
    def _namePlayers(self):
        self._nameOfPlayer[1] = str(input("Who is our first player? "))
        self._nameOfPlayer[2] = str(input("Who is the second player? "))


if __name__ == "__main__":
    Connect4().play()
