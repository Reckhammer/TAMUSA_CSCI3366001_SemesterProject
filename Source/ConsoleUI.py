from UserInterface import UserInterface
from TicTacToeGame import TicTacToeGame

class CommandLineInterface(UserInterface):
    def GetPlayerInput(self, playerName):
        while True:
            try:
                # Prompt user to enter row and column numbers
                user_input = input(f"Player {playerName}, enter your move as 'row col' (0, 1, or 2): ")
                row, col = map(int, user_input.split())
                if self.ValidatePlayerInput((row, col)):
                    return row, col
                else:
                    print("Invalid input. Please enter numbers 0, 1, or 2 for both row and column.")
            except ValueError:
                print("Invalid format. Please enter row and column as two numbers separated by a space.")

    def ValidatePlayerInput(self, input):
        row, col = input
        # Check if the input is within bounds (0-2 for row and column)
        return 0 <= row <= 2 and 0 <= col <= 2

    def DisplayBoard(self, board):
        # Display the current board state
        print("\nCurrent board:")
        for i, row in enumerate(board):
            print(" | ".join(row))
            if i < len(board) - 1:  # Only print dashes if it's not the last row
                print("-" * 9)


    def SendMessage(self, msg):
        # Print a message (for game status updates)
        print(msg)

# Main code to run the game in the command line
if __name__ == "__main__":
    # Instantiate Command Line Interface and Game
    ui_interface = CommandLineInterface()
    game = TicTacToeGame(ui_interface)
    
    # Start the game
    game.PlayGame()
