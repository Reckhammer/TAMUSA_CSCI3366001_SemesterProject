class TicTacToeGame:
    def __init__(self, uiInterface):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turnCount = 0
        self.uiInterface = uiInterface

    def PlayGame(self):
        self.uiInterface.SendMessage("Starting Tic Tac Toe Game!")
        winner = None
        while self.turnCount < 9 and winner is None:
            self.DisplayBoard()
            playerName = self.GetCurrentPlayer()
            row, col = self.GetPlayerMove(playerName)
            if self.MakeMove(row, col):
                winner = self.CheckWin()
        self.DisplayBoard()
        if winner:
            self.uiInterface.SendMessage(f"Player {winner} wins!")
        else:
            self.uiInterface.SendMessage("It's a tie!")

    def GetCurrentPlayer(self):
        # 'X' for even turns, 'O' for odd turns
        return 'X' if self.turnCount % 2 == 0 else 'O'

    def MakeMove(self, row, col):
        if self.ValidateMove(row, col):
            # Place current player's symbol on the board
            self.board[row][col] = self.GetCurrentPlayer()
            self.turnCount += 1
            return True
        else:
            self.uiInterface.SendMessage("Invalid move, please try again.")
            return False

    def ValidateMove(self, row, col):
        # Check if the move is within bounds and if the cell is empty
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def GetPlayerMove(self, playerName):
        # Use the interface to get player input
        return self.uiInterface.GetPlayerInput(playerName)

    def CheckWin(self):
        if self.turnCount < 5:  # Impossible to win before 5 moves
            return None
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

    def GetGameStatus(self):
        winner = self.CheckWin()
        if winner:
            return f"Player {winner} wins!"
        elif self.turnCount == 9:
            return "It's a tie!"
        return f"Player {self.GetCurrentPlayer()}'s turn"

    def PlayTurn(self, row, col):
        if self.MakeMove(row, col):
            self.uiInterface.DisplayBoard(self.board)
            self.uiInterface.SendMessage(self.GetGameStatus())

    def DisplayBoard(self):
        self.uiInterface.DisplayBoard(self.board)
