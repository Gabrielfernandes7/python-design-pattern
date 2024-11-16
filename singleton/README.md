# Design pattern singleton

O padrão singleton tem como principal preocupação garantir que uma classe tenha apenas uma instância em todo o ciclo de vida da aplicação.

Isso é útil quando precisamos:

* Um único recurso: Quando existe um recurso global que deve ser compartilhado por todas as partes da aplicação. Um gerenciador de banco de dados, um objeto de configuração ou um logger.

* Estado global: Ao precisar manter um estado global que afeta todo o sistema, como um objeto que controla a sessão do usuário.

Desvantagens: 

Esse pattern pode ferir o SRP (Princípio da Responsabilidade única, do SOLID)

Dificuldade de testar: Pode dififultar os testes unitparios, pois a dependências entre as classes aumentam
