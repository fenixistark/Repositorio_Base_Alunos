from herança_ex_01 import Personagem

class Sayajin(Personagem):
        def comer(self):
            print(f"{self.nome} esta comendo!")
        def dormir(self):
            print(f"{self.nome} esta dormindo!")
        def correr(self):
            print(f"{self.nome} esta correndo!")
        def pular(self):
            print(f"{self.nome} pulou!")
        def atacar(self):
            print(f"{self.nome} atacou!!!")
        def comer(self):
            print(f"{self.nome1} esta comendo.")
        def dormir(self):
            print(f"{self.nome1} está dormindo.")
        def correr(self):
            print(f"{self.nome1} esta correndo.")
        def pular(self):
            print(f"{self.nome1} pulou!!!")
        def atacar(self):
            print(f"{self.nome1} atacou!!!")

class Ninja(Personagem):
    pass

personagem = Sayajin("goku")
personagem2 = Ninja("naruto")
personagem.correr()
personagem2.comer()
personagem.pular()
personagem.atacar()
personagem.dormir()