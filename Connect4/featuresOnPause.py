
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