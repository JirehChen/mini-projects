'''
A quick project: A rudimentary game of Connect 4, run in the terminal, for two players.
Jireh Chen, 6th Nov 2024
'''
from gameBoard import GameBoard
from gameController import GameController

class Connect4():
    _playerNames = {1:'Player 1', 2:'Player 2'}    
    _gameDimensions = {'rows': 6, 'cols': 7}
    _gameBoard = None                               # Risky? 
    _gameController = None

    def play(self):
        self._setUpGame()
        self._gameController.run()

    def _setUpGame(self):
        self._welcome()
        self._namePlayers()
        self._gameBoard = GameBoard(self._gameDimensions.get('rows'), self._gameDimensions.get('cols') )  
        self._gameController = GameController(self._gameBoard, self._playerNames)                      
    
    def _welcome(self):
        print("Welcome to a new game of Connect 4 for two players\n")
    
    def _namePlayers(self):
        self._playerNames[1] = str(input("Who is our first player? "))
        self._playerNames[2] = str(input("Who is the second player? "))


if __name__ == "__main__":
    Connect4().play()
