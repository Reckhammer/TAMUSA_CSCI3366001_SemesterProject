from Source.TicTacToeGame import TicTacToeGame
from Source.UserInterface import UserInterface


class CommandLineInterface(UserInterface):
    def GetPlayerInput(self, playerName):
        while True:
            try:
                user_input = input(f"Player {playerName}, enter your move as 'row col' (0, 1, or 2): ")
                row, col = map(int, user_input.split())
                if self.ValidatePlayerInput(row, col):
                    return row, col
                else:
                    print("Invalid input. Enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid format. Enter row and column as two numbers separated by a space.")

    def ValidatePlayerInput(self, row, col):
        return 0 <= row <= 2 and 0 <= col <= 2

    def DisplayBoard(self, board):
        print("\nCurrent board:")
        for i, row in enumerate(board):
            print(" | ".join(row))
            if i < len(board) - 1:
                print("-" * 9)

    def SendMessage(self, msg):
        print(msg)


# Main console Demo
if __name__ == "__main__":
    # Instantiate Command Line Interface and Game
    ui_interface = CommandLineInterface()
    game = TicTacToeGame(ui_interface)

    # Start the game
    game.PlayGame()