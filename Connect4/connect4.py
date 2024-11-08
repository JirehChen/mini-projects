'''
A quick project: A rudimentary game of Connect 4, run in the terminal, for two players.
Jireh Chen, 6th Nov 2024
'''
from gameController import GameController

class Connect4():
    
    def __init__(self):
        self._playerNames = {1:'Player 1', 2:'Player 2'}    
        self._gameController = None

    def play(self):
        self._setUpGame()
        self._gameController.run()

    def _setUpGame(self):
        self._welcome()
        self._namePlayers()
        self._gameController = GameController(self._playerNames)                      
    
    def _welcome(self):
        print("\nWelcome to a new game of Connect 4 for two players\n")
    
    def _namePlayers(self):
        self._playerNames[1] = str(input("Please name player 1: "))
        self._playerNames[2] = str(input("Please name player 2: "))


if __name__ == "__main__":
    Connect4().play()
