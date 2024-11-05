from UserInterface import UserInterface

class TestUI(UserInterface):
    def GetPlayerInput(self, playerName):
        print(f"Player {playerName}'s Turn")
        # Simple console input to get the player's move
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))

                if (0 <= row <= 2) and (0 <= col <= 2):
                    return row, col
                    
                self.SendMessage("Input is out of range. Please enter values in range.")
            except ValueError:
                self.SendMessage("Invalid input. Please enter numbers only.")
    
    def ValidatePlayerInput(self, input):
        return True

    def DisplayBoard(self, board):
        for row in board:
            print(" | ".join(row))
            print("-" * 10)
    
    def SendMessage(self, msg):
        print(msg)
        