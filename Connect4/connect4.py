'''
A quick project: A rudimentary game of Connect 4, run in the terminal, for two players.
Jireh Chen, 6th Nov 2024
'''

class Connect4():
    nameOfPlayer = {1:'Player 1', 2:'Player 2'}    
    gameDimensions = [7,6]
    board = [[]]

    def play(self):
        self._welcome()
        self._setUpGame()

        return 0
    
    def _welcome():
        print("Welcome to Connect 4 for two players/n/n")
        return

    def _setUpGame(self):
        self._namePlayers
        self._selectGameDimensions()

        return 0
    
    def _namePlayers(self):
        self.nameOfPlayer[1] = str(input("Who is our first player? "))
        self.nameOfPlayer[2] = str(input("Who is the second player? "))
        return
    
    def _selectGameDimensions(self):
        choice = input('''Select your game size: (Or press Enter for the default setting)/n
              A) 6x5/n
              B) 7×6 - Default/n
              C) 8×7/n
              D) 9×7/n
              E) 10×7/n
              F) 8×8/n
              G) Custom/n
              ''')
        
        match choice:
            case '/n':
                return
            case [aA]:
                self.gameDimensions = [6,5]
            case [bB]:
                return
            case [cC]:
                self.gameDimensions = [8,7]
            case [dD]:
                self.gameDimensions = [9,7]
            case [eE]:
                self.gameDimensions = [10,7]
            case [fF]:
                self.gameDimensions = [8,8]
            case [gG]:
                print("Function under construction")            #TODO: Check w. user n. either exit game or continue with default game size. Implement once exitGame() is made.
            case _:
                raise ValueError("Invalid selection made. Requires a value between A and G inclusive.")


if __name__ == "__main__":
    Connect4().play()
