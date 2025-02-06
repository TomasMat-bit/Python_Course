print(' - - - - - -  UZDUOTIS 2 - - - - - - - - - ')

# 2. Paveldėjimas (Inheritance)
# Užduotis:
# Sukurkite bazinę klasę Gyvunas, kuri turi atributus vardas ir amzius.+
# Pridėkite metodą judeti(), kuris spausdina, kad gyvūnas juda.+
# Sukurkite dvi paveldinčias klases: Kate ir Suo.+
# Kate klasėje pridėkite metodą miaukseti(), kuris sako "Vardas sako MIAU!"+
# Suo klasėje pridėkite metodą lot(), kuris sako "Vardas sako AU AU!"+
# Papildoma užduotis:
# Sukurkite Kate ir Suo objektus, iškvieskite jų metodus ir patikrinkite, ar paveldėjimas
# veikia.

class Gyvunas:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.spalva = amzius

    def judeti(self):
        print(f' Gyvūnas {self.vardas} juda!!!')

class Suo(Gyvunas):
    def lot(self):
        print(f'{self.vardas} sako AU AU AU!!!')

class Kate(Gyvunas):
    def miaukseti(self):
        print(f'{self.vardas} sako MIAU!!!')

cat = Kate('Rainiukas', '3')
cat.miaukseti()

dog = Suo('Argas', '9')
dog.judeti()