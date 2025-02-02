# Design Pattern Decorator

Decorator é um padrão de projeto estrutural que permite adicionar comportamentos ou responsabilidades adicionais a objetos de forma dinâmica, sem modificar sua estrutura original.

Esse padrão é útil quando você deseja estender as capacidades de um objeto de forma flexível e modular evitando a combinação de múltiplas subclasses para cada cominação possível de comportamentos.

Quando não utilzar o decorator:

* Simplicidade: se a hierarquia de classes é simples e as possíveis extensões de comportamento são limitadas, o uso de herança pode ser mais apropriado e direto.

```python
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()

async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

@app.get("/items/", dependencies=[Depends(verify_token)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
```