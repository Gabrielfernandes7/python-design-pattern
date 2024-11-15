from src import Guerreiro, LutaArco, LutaEspada, Curar

cavaleiro = Guerreiro(
    LutaEspada(6)
)

arqueiro = Guerreiro(
    LutaArco(9)
)

arqueiro.acao()
arqueiro.atributos()

cavaleiro.acao()