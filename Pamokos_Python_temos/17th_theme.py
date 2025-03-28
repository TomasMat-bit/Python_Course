#Apsaugoti ir Privatūs Atributai
#
print('- - - - -- - - -Apsaugoti Atributai (Protected Attributes) - - - - - - - - - - -')



class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self._atlyginimas = None
        self.__asmens_kodas = None

    def get_atlyginimas(self):
        if self._atlyginimas:
            return self._atlyginimas
        return 'Neaisku'

    def _set_atlyginimas(self, suma):
        if int(suma) > 0:
            self._atlyginimas = suma
        else:
            print('Atlyginimas negali būti <=0')

    def get_asmens_kodas(self):
        if self.__asmens_kodas:
            return self.__asmens_kodas
        return 'Neaisku'

    def _set_asmens_kodas(self, asmens_kodas):
        if int(asmens_kodas) > 0:
            self.__asmens_kodas = asmens_kodas
        else:
            print('Atlyginimas negali būti <=0')

    def __str__(self):
        return f'Vardas: {self.vardas} Pavarde: {self.pavarde} Pareigos: {self.pareigos} {self.get_atlyginimas()} {self.get_asmens_kodas()}'

    def __reset_asmens_kodas(self):
        self.__asmens_kodas = '123123123'

class Vadovas(Darbuotojas):
    def __init__(self, vardas, pavarde, pareigos, departamentas):
        super().__init__(vardas, pavarde, pareigos)
        self.departamentas = departamentas

    def super_change_of_atlyginmas(self):
        self._atlyginimas = '123412341234'

class Sarasas:
    def __init__(self):
        self.super_sarasas = []

    def change_elemntu_atlyginimas(self):
        for i in self.super_sarasas:
        #     i._atlyginimas
        #     i.__asmens_kodas
            print(i)

vadovas1 = Vadovas('Jonas',' Jonaitis', 'Programuotojas', 'IT')
vadovas1.super_change_of_atlyginmas()
# vadovas1.__reset_asmens_kodas()
print(vadovas1)

elem = Sarasas()
elem.super_sarasas.append(vadovas1)

print(elem.change_elemntu_atlyginimas())





print('- - - - -- - - - Privatūs Atributai (Private Attributes) - - - - - - - - - - -')

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.__atlyginimas = None  # Privatus atributas

    def get_atlyginimas(self):
        if self.__atlyginimas:
            print(self.__atlyginimas)
        else:
            print("Atlyginimas dar nepaskirtas!!!")

    def set_atlyginimas(self, suma):
        if suma > 0:
            self.__atlyginimas = suma
        else:
            print("Atlyginimas negali būti <= 0")


print('- - - - -- - - - @property Dekoratorius - - - - - - - - - - -')

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos, asmens_kodas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.asmens_kodas = asmens_kodas
        self.__atlyginimas = None

    @property
    def lytis(self):
        return 'Vyras' if self.asmens_kodas[0] == '3' else 'Moteris'

    @property
    def atlyginimas(self):
        return self.__atlyginimas if self.__atlyginimas else 0

    @atlyginimas.setter
    def atlyginimas(self, suma):
        self.__atlyginimas = suma if suma >= 0 else 1

darb1 = Darbuotojas('Jonas', 'Jonaitis', 'Direktorius', '47575483939')

print(
    darb1.lytis
)

atl = darb1.atlyginimas
print(atl)

darb1.atlyginimas = 5000
atl2 = darb1.atlyginimas
print(atl2)

print('- - - - -- - - - @staticmethod Dekoratorius - - - - - - - - - - -')

class Calculator:
    def __init__(self):
        self.a = 1

    def get_a(self):
        return

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2

a = Calculator.add(10, 5)
print(a)
print('-' * 30)

a = Calculator.sub(10, 5)
print(a)
print('-' * 30)


class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    @classmethod
    def sukur_is_vienos_eilutes(cls, eilute):
        vardas, pavarde, pareigos = eilute.split()
        return cls(vardas, pavarde, pareigos)

    def __str__(self):
        return f'{self.vardas} {self.pavarde}, pareigos {self.pareigos}'

    def pakeeisti_pareigas(self, naujos_pareigos):
        self.pareigos = naujos_pareigos

eilute = 'Tadas Tadauskas Inzinierius'
darbuotojas = Darbuotojas.sukur_is_vienos_eilutes(eilute)
print(darbuotojas)
print('-' * 30)

darbuotojas.pakeeisti_pareigas('IT specialistas')
print(darbuotojas)

print('-' * 30)

print('- - - - -- - - - @classmethod Dekoratorius - - - - - - - - - - -')

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    @classmethod
    def sukurk_is_vienos_eilutes(cls, eilute):
        vardas, pavarde, pareigos = eilute.split()
        return cls(vardas, pavarde, pareigos)