from classe_pai import Animal
animal1 = Criatura(8, "leão", 10.00, "rei da selva")
animal2 = AnimalMarinho(138, "Tartaruga", 10.00, "idoso")
animal3 = Criatura(8, "leão", 10.00, "rei da selva")
def comunicar(qualquer_animal):
    print(f"Tentando comunicação com {qualquer_animal.especie}")
    qualquer_animal.fazer_som()
print("-"*50)
comunicar()animal1
print("-"*50)
comunicar()animal2
print("-"*50)
comunicar()animal3