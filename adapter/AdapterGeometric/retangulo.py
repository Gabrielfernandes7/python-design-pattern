class Retangulo:
    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura
    
    def calcular_area(self):
        return (self.altura * self.comprimento)
