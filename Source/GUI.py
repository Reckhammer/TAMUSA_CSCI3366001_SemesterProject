import tkinter as tk
from UserInterface import UserInterface
from TicTacToeGame import TicTacToeGame

class TkinterInterface(UserInterface):
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.board_buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.message_label = tk.Label(root, text="Player X's turn", font=("Arial", 16))
        self.message_label.grid(row=3, column=0, columnspan=3, pady=10)

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.board_buttons[row][col] = button

    def handle_click(self, row, col):
        if self.game.ValidateMove(row, col):
            player = 'X' if self.game.turnCount % 2 == 0 else 'O'
            self.game.board[row][col] = player
            self.board_buttons[row][col].config(text=player, state="disabled")
            self.game.turnCount += 1
            winner = self.game.CheckWin()
            if winner:
                self.SendMessage(f"Player {winner} wins!")
                self.disable_board()
            elif self.game.turnCount == 9:
                self.SendMessage("It's a tie!")
            else:
                next_player = 'X' if self.game.turnCount % 2 == 0 else 'O'
                self.SendMessage(f"Player {next_player}'s turn")

    def disable_board(self):
        for row in self.board_buttons:
            for button in row:
                button.config(state="disabled")

    def GetPlayerInput(self, playerName):
        # Not needed for Tkinter as it's handled by button click
        pass

    def ValidatePlayerInput(self, input):
        # Not used as input validation is within the game logic
        return True

    def DisplayBoard(self, board):
        # Not directly used as board updates happen through button clicks
        pass

    def SendMessage(self, msg):
        self.message_label.config(text=msg)


# Main Application Setup
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Instantiate Game and GUI Interface
    ui_interface = TkinterInterface(root, None)  # Placeholder None; will update after game instantiation
    game = TicTacToeGame(ui_interface)
    ui_interface.game = game  # Inject the game instance

    root.mainloop()
