from retangulo import Retangulo
from adapter import QuadradoAdapter

def client_code(retangulo):
    print(f"Área: {retangulo.calcular_area()}")

if __name__ == "__main__":
    retangulo = Retangulo(5, 10)
    print("Calculando a área do retângulo")
    client_code(retangulo)

    # utilizando o adaptador para o quadrado
    quadrado_adapter = QuadradoAdapter(5)
    print("Calculando a área do quadrado utilizando o adaptador")
    client_code(quadrado_adapter)