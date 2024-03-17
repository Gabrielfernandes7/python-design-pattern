from target import Target
from adaptee import Adaptee

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def request(self):
        return "Adapter: (Traduzido) {}".format(self.adaptee.specific_request()[::-1])