from abc import abstractmethod
from abc import ABCMeta

class Arma(metaclass=ABCMeta):
    @abstractmethod
    def enciende(self,screen):
        pass
    
    def grito(self):
        pass