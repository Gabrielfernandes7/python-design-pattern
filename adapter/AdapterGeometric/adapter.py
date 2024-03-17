from quadrado import Quadrado
from retangulo import Retangulo

# adapta o meu quadrado para se comportar como triângulo

class QuadradoAdapter(Retangulo):
    def __init__(self, lado):
        self.quadrado = Quadrado(lado)
    
    def calcular_area(self):
        return self.quadrado.calcular_area()
