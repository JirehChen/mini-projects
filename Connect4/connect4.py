'''
A quick project: A rudimentary game of Connect 4, run in the terminal, for two players.
Jireh Chen, 6th Nov 2024
'''

class Connect4():
    nameOfPlayer = {1:'Player 1', 2:'Player 2'}    
    _gameDimensions = {'rows': 6, 'cols': 7}

    board = []

    def play(self):
        self._setUpGame()
        return 

    def _setUpGame(self):
        self._welcome()
        self._namePlayers()
        self._createEmptyBoard()
        return
    
    def _welcome():
        print("Welcome to Connect 4 for two players/n/n")
        return
    
    def _namePlayers(self):
        self.nameOfPlayer[1] = str(input("Who is our first player? "))
        self.nameOfPlayer[2] = str(input("Who is the second player? "))
        return
    

    ## Creates an empty board with 'gameDimensions' dimensions represented by an array of gameboard column arrays
    def _createEmptyBoard(self):
        for _ in self._gameDimensions['cols']:
            self.board += [[0]*self._gameDimensions['rows']]
        return

if __name__ == "__main__":
    Connect4().play()
