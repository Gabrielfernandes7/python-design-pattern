from .interfaces import IHabilidade

class LutaArco(IHabilidade):
    def __init__(self, nivel) -> None:
        self.nivel = nivel

    def comportamento(self):
        print("Atirar flechas")

    def nivel_atributo(self):
        print(f"Nível de uso Arco: {self.nivel}")