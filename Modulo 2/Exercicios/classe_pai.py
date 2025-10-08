class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comer(self):
        print (f"{self.nome} esta comendo.")
    def fazer_som(self):
        print(f"{self.nome} esta fazendo um som generico.")