from TestUI import TestUI
from TicTacToeGame import TicTacToeGame

def main():
    # Create an instance of user interface
    ui_instance = TestUI()
    
    # Create an instance of TicTacToeGame, passing the UI instance to it
    game_instance = TicTacToeGame(ui_instance)
    
    # Start the game
    game_instance.PlayGame()
    
if __name__ == "__main__":
    main()