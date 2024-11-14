# Design pattern strategy

Uma aplicação direta do princípio da inversão da dependência


Conceito: padrão de projeto comportamental que permite que uma família de algoritmos, coloque-os em classes separadas, e faça os objetos deles intercambiáveis.

```python
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
    
```

Problemática levantada pelo código acima é que poderia prejudicar na definição de nossos personagens. Por exemplo: um curandeiro não iria lutar frontalmente e nem usar arco.

Exemplo:

```python
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

class Cavaleiro(Guerreiro):
    def __init__(self, habilidade_arco, habilidade_cura, habilidade_luta) -> None:
        self.habilidade_arco = habilidade_arco
        self.habilidade_cura = habilidade_cura
        self.habilidade_luta = habilidade_luta

    def curar(self):
        print("Não cura") # anti pattern

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
    
```