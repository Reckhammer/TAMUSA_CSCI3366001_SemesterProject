
class TicTacToeGame:
    
    def __init__(self):
        # Initialize the board with empty spaces
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turnCount = 0

    def play_game(self):
        print("Starting Tic Tac Toe Game!")
        winner = None
        while self.turnCount < 9 and winner is None:
            self.display_board()
            row, col = self.get_player_move()
            if self.validate_move(row, col):
                self.board[row][col] = 'X' if self.turnCount % 2 == 0 else 'O'
                self.turnCount += 1
                winner = self.check_win()
            else:
                print("Invalid move, please try again.")
        
        self.display_board()
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a tie!")

    def validate_move(self, row, col):
        # Check if the move is within bounds and if the cell is empty
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def get_player_move(self):
        # Simple console input to get the player's move
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                return row, col
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def check_win(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def display_board(self):
        # Display the board in a user-friendly format
        print("Current board:")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)