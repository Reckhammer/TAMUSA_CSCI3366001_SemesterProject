
from UserInterface import UserInterface

class TicTacToeGame:
    
    def __init__(self, uiInterface):
        # Initialize the board with empty spaces
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turnCount = 0
        self.uiInterface = uiInterface

    def PlayGame(self):
        print("Starting Tic Tac Toe Game!")
        winner = None
        while self.turnCount < 9 and winner is None:
            self.DisplayBoard()
            
            playerName = 'X' if self.turnCount % 2 == 0 else 'O'

            # Prompt User
            while(True):
                row, col = self.GetPlayerMove(playerName)
                if self.ValidateMove(row, col):
                    self.board[row][col] = playerName
                    self.turnCount += 1
                    winner = self.CheckWin()
                    break
                else:
                    print("Invalid move, please try again.")
        
        self.DisplayBoard()
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a tie!")

    def ValidateMove(self, row, col):
        # Check if the move is within bounds and if the cell is empty
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def GetPlayerMove(self, playerName):
        return self.uiInterface.GetPlayerInput(playerName)

    def CheckWin(self):
        # Don't even check before turn 5 since it's impossible to win
        if (self.turnCount < 5):
            return None

        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        # Check Diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def DisplayBoard(self):
        self.uiInterface.DisplayBoard(self.board)