#abstract interface

from abc import ABC, abstractmethod # allows for abstract methods

class UserInterface(ABC):
    @abstractmethod
    def GetPlayerInput(self, playerName):
        pass

    @abstractmethod
    def ValidatePlayerInput(self, input):
        pass

    @abstractmethod
    def DisplayBoard(self, board):
        pass