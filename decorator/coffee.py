def cafe():
    return 5

def leite(func):
    def wrapper():
        return func() + 2
    return wrapper

def chantilly(func):
    def wrapper():
        return func() + 3
    return wrapper

def acucar(func):
    def wrapper():
        return func() + 1
    return wrapper

if __name__ == "__main__":
    print(f"Café simples: R$ {cafe()},00")

    @leite
    def cafe_com_leite():
        return cafe()
    print(f"Café com leite: R$ {cafe_com_leite()},00")

    @chantilly
    @leite
    def cafe_leite_chantilly():
        return cafe()
    print(f"Café com leite e chantilly: R${cafe_leite_chantilly()}")

    @acucar
    @chantilly
    @leite
    def cafe_completo():
        return cafe()
    print(f"Café completo: R${cafe_completo()}")