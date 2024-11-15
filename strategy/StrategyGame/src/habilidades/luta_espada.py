from .interfaces import IHabilidade

class LutaEspada(IHabilidade):
    def __init__(self, nivel) -> None:
        self.nivel = nivel

    def comportamento(self):
        print("Lutar com espada")

    def nivel_atributo(self):
        print(f"Nível de uso Espada: {self.nivel}")