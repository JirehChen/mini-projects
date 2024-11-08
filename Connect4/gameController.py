'''
Connect4 GameController class that is responsible for the game playing process
Jireh Chen, 8th Nov 2024
'''
from gameBoard import GameBoard

class GameController:
     
    def __init__(self, playerNames, gameRows=6, gameCols=7, startingPlayer=1):
        self._gameRows = gameRows
        self._gameCols = gameCols
        self._gameBoard = GameBoard(self._gameRows, self._gameCols)
        self._playerNames = playerNames
        self._currentPlayer = startingPlayer      # TODO: Can be upgraded... ENUM? or New class..Overkill?
        self._gameInProgress = True

    def run(self):
        print(f"\nPlayer 1 [{self._playerNames[1]}] starts")

        while self._gameInProgress:
            
            self._gameBoard.display()
            
            currentPlayerMove = self._promptForMove()
            
            moveResult = self._gameBoard.update(currentPlayerMove, self._currentPlayer)

            if moveResult is not None:
                self._endGame(moveResult)
            else:
                self._currentPlayer = self._currentPlayer%2+1           # TODO: Not the most efficient? 


    ## Prompts the currentPlayer to select their move, until a vaild move is made
    def _promptForMove(self):
        print(f"Current player: [{self._currentPlayer}] {self._playerNames[self._currentPlayer]}")

        if self._gameBoard.validMoves() == []:
            raise ValueError("Incorrect game state, no moves possible.")
        
        move = str(input("\nPlease select a column to drop your token: "))
        while True:
            if move in self._gameBoard.validMoves():
                return move 
            else:
                print(f"Invalid selection, please choose one of {self._gameBoard.validMoves()}\n")
                move = str(input("In which column would you like to drop your token? "))


    ## Ends the game according the the current player and the result they achieved (Win/Draw/Terminated))
    def _endGame(self, result):

        self._gameBoard.display()

        match result:
            case "Win":
                print(f"Congratulations, {self._playerNames[self._currentPlayer]} has won the game")                
                self._gameInProgress = False 

            case "Draw":
                print(f"The game has ended in a draw. Good Game!")                
                self._gameInProgress = False 

            case _:
                raise ValueError("Attempting to end game qith unrecognised result.")
        