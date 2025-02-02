# Classe base para o café
class Cafe:
    def custo(self):
        return 5  # Preço base do café simples

# Decorador base (classe abstrata para os decoradores)
class DecoradorCafe(Cafe):
    def __init__(self, cafe):
        self._cafe = cafe

    def custo(self):
        return self._cafe.custo()

# Decorador para adicionar leite
class Leite(DecoradorCafe):
    def custo(self):
        return self._cafe.custo() + 2  # Adiciona R$2 ao custo

# Decorador para adicionar chantilly
class Chantilly(DecoradorCafe):
    def custo(self):
        return self._cafe.custo() + 3  # Adiciona R$3 ao custo

# Decorador para adicionar açúcar
class Acucar(DecoradorCafe):
    def custo(self):
        return self._cafe.custo() + 1  # Adiciona R$1 ao custo

# Exemplo de uso
if __name__ == "__main__":
    # Café simples
    cafe_simples = Cafe()
    print(f"Café simples: R${cafe_simples.custo()}")

    # Café com leite
    cafe_com_leite = Leite(cafe_simples)
    print(f"Café com leite: R${cafe_com_leite.custo()}")

    # Café com leite e chantilly
    cafe_leite_chantilly = Chantilly(cafe_com_leite)
    print(f"Café com leite e chantilly: R${cafe_leite_chantilly.custo()}")

    # Café com leite, chantilly e açúcar
    cafe_completo = Acucar(cafe_leite_chantilly)
    print(f"Café completo: R${cafe_completo.custo()}")