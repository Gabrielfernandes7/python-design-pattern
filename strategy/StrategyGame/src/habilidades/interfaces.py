# nossa forma
from abc import ABC, abstractmethod

class IHabilidade(ABC):

    @abstractmethod
    def comportamento(self):
        pass

    @abstractmethod
    def nivel_atributo(self):
        pass