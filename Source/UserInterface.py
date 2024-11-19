#abstract interface

from abc import ABC, abstractmethod # allows for abstract methods

class UserInterface(ABC):
    @abstractmethod
    def GetPlayerInput(self, row, col):
        pass

    @abstractmethod
    def ValidatePlayerInput(self, row, col):
        pass

    @abstractmethod
    def DisplayBoard(self, board):
        pass

    @abstractmethod
    def SendMessage(self, msg):
        pass