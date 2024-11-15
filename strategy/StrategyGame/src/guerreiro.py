from .habilidades import IHabilidade
from typing import Type

class Guerreiro:
    def __init__(self, habilidade: Type[IHabilidade]):
        self.habilidade = habilidade

    def acao(self):
        self.habilidade.comportamento()

    def atributos(self):
        self.habilidade.nivel_atributo()
    
