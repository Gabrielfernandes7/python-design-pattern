from .interfaces import IHabilidade

class Curar(IHabilidade):
    def __init__(self, nivel) -> None:
        self.nivel = nivel

    def comportamento(self):
        print("Curar personagem")

    def nivel_atributo(self):
        print(f"Nível de cura: {self.nivel}")