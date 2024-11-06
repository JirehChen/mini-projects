'''
A quick project: A rudimentary game of Connect 4, run in the terminal, for two players.
Jireh Chen, 6th Nov 2024
'''

def runGame():
    players = ["",""]

    welcome(players)
    
    return 0

def welcome(players):
    print("Welcome to Connect 4 for two players/n ")
    players[0] = input("Who is our first player?/n")
    players[1] = input("Who is the second player?/n")
    return players


if __name__ == "__main__":
    runGame()
