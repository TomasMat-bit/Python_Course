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
        self.amzius = amzius

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

print(' - -  -  -   - -  UZDUOTIS 3 - - - -    - -    - - -  ')

# 3. Komponavimas (Composition)
# Užduotis:
# Sukurkite klasę Variklis, kuri turi atributą galia ir metodą startuoti(), kuris+
# spausdina "Variklis veikia su galia: X arklio galių".+
# Tada sukurkite klasę Automobilis, kuri turi atributus marke ir modelis, bei naudoja+
# Variklis kaip savo atributą.+
# • Pridėkite metodą vaziuoti(), kuris iškviečia startuoti() metodą.
# Papildoma užduotis:
# Sukurkite kelis Automobilis objektus su skirtingais varikliais ir priverskite juos važiuoti.

class Variklis:
    def __init__(self, galia):
        self.galia = galia

    def startuoti(self):
        print(f'Variklis veikia su {self.galia} arklio galių!')

class Automobilis:
    def __init__(self, marke, modelis, variklis):
        self.marke = marke
        self.modelis = modelis
        self.variklis = variklis

    def vaziuoti(self):
        print(f'Super family car`as {self.marke} {self.modelis} važiuoja:')
        self.variklis.startuoti()

variklis1 = Variklis(500)
variklis2 = Variklis(306)

automobilis1 = Automobilis('BMW', 'M5', variklis1)
automobilis2 = Automobilis('MINI', 'JCW', variklis2)

automobilis1.vaziuoti()
automobilis2.vaziuoti()
