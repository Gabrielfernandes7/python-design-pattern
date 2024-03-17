from adaptee import Adaptee
from adapter import Adapter

def client_code(target):
    print(target.request())

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print("Cliente: A classe Adaptee tem uma interface estranha: ")
    print(f"Adaptee: {adaptee.specific_request()}")
    print("\nCliente: Mas posso utilizar o Adapter para chamar seu método")
    client_code(adapter)