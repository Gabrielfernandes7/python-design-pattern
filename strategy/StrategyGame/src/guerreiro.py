class Guerreiro:
    def __init__(self, habilidade_arco, habilidade_cura, habilidade_luta) -> None:
        self.habilidade_arco = habilidade_arco
        self.habilidade_cura = habilidade_cura
        self.habilidade_luta = habilidade_luta

    def curar(self):
        print("Curar outro guerreiro")

    def luta(self):
        print("Ataca com espada")

    def flexa(self):
        print("Ataca com flechas")

    def atributos(self):
        print(
            '''
                Nível arco: {}
                Nível cura: {}
                Nível luta: {}
            '''.format(self.habilidade_arco, self.habilidade_luta, self.habilidade_cura)
        )
    
