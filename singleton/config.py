class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class GerenciadorDeConfiguracoes(Singleton):
    def __init__(self):
        self.configuracoes = {}

    def adicionar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor

    def obter_configuracao(self, chave):
        return self.configuracoes.get(chave)

gerenciador1 = GerenciadorDeConfiguracoes()
gerenciador2 = GerenciadorDeConfiguracoes()

# Adição de configurações
gerenciador1.adicionar_configuracao('chave', 'valor')

# Obtenção de configurações
print(gerenciador2.obter_configuracao('chave'))  # 'valor'
