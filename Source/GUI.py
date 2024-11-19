import tkinter as tk
from UserInterface import UserInterface
from TicTacToeGame import TicTacToeGame


class TkinterInterface(UserInterface):
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.board_buttons = [[None for _ in range(3)] for _ in range(3)]
        self.message_label = tk.Label(root, text="Player X's turn", font=("Arial", 16))
        self.message_label.grid(row=3, column=0, columnspan=3, pady=10)
        self.restart_button = tk.Button(root, text="Restart", font=("Arial", 14), command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.GetPlayerInput(r, c)
                )
                button.grid(row=row, column=col)
                self.board_buttons[row][col] = button

    def restart_game(self):
        # Reset game logic
        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game.turnCount = 0
        self.message_label.config(text="Player X's turn")

        # Reset button states and text
        for row in self.board_buttons:
            for button in row:
                button.config(text="", state="normal")

    def GetPlayerInput(self, row, col):
        # Handle button clicks and process the player's move.
        if self.ValidatePlayerInput(row, col):
            player = self.game.GetCurrentPlayer()  # Determine the current player
            self.board_buttons[row][col].config(text=player, state="disabled")
            self.game.PlayTurn(row, col)
            self.SendMessage(self.game.GetGameStatus())
            if "wins" in self.game.GetGameStatus() or "tie" in self.game.GetGameStatus():
                self.disable_board()

    def ValidatePlayerInput(self, row, col):
        # Ensure the selected cell is valid (not already taken).
        return self.board_buttons[row][col]["state"] == "normal"

    def DisplayBoard(self, board):
        # Update the button texts to reflect the current game state.
        for row in range(3):
            for col in range(3):
                if board[row][col] != ' ':
                    self.board_buttons[row][col].config(text=board[row][col], state="disabled")

    def SendMessage(self, msg):
        # Update the label to display the current message.
        self.message_label.config(text=msg)

    def disable_board(self):
        # Disable all buttons to prevent further moves after the game ends.
        for row in self.board_buttons:
            for button in row:
                button.config(state="disabled")


# Main Application Demo
if __name__ == "__main__":
    # Create the Tkinter root window
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Instantiate the game and GUI interface
    ui_interface = TkinterInterface(root, None)  # Placeholder for game
    game = TicTacToeGame(ui_interface)
    ui_interface.game = game  # Inject the game instance into the UI

    # Start the Tkinter event loop
    root.mainloop()
