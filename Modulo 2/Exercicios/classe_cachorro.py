from classe_pai import animal
from classe_pessoa import Pessoa
class Cachorro(animal):
    def __init__(self, nome, raca):
        self.raca = raca
    def fazer_som(self):
        print(f"{self.nome} esta latindo: Au Au!")
    def abanar_rabo(self):
        print(f"{self.nome} esta abanando o rabo")
    def comendo(self):
        print(f"{self.nome} esta comendo")
animal1 = Cachorro('neguin', 'caramelo')
animal1.comendo()
animal1.abanar_rabo()
humano1 = Pessoa('jão', 15)
