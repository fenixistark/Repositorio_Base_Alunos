from classe_pai import Animal
class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} esta miando: Miau!")
    def comer(self):
        print(f"{self.nome} esta comendo!")
animal2 = Gato("garfield")
animal2.fazer_som()
animal2.comer()