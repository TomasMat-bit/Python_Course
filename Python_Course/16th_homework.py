print(' - - - - - - - -  1. Sudėtinė užduotis - - - - - ')
# Užduotis:
# Sukurkite bazinę klasę Zmogus, su atributais vardas, pavarde ir metodu
# prisistatyti(), kuris spausdina žmogaus vardą ir pavardę.+
# Sukurkite paveldinčią klasę Studentas, kuri perrašo prisistatyti() metodą,
# pridėdama informaciją apie studijų programą.+
# Sukurkite klasę Universitetas, kuri naudoja kompoziciją, turėdama sąrašą
# Studentas objektų.+
# Pridėkite metodus prideti_studenta() ir rodyti_visus_studentus().+
# Papildoma užduotis:
# Sukurkite kelis Studentas objektus.+
# Pridėkite juos į Universitetas objektą.+
# Parodykite visų studentų informaciją, pasitelkiant paveldėjimą, metodų perrašymą
# ir kompoziciją+

class Zmogus:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def prisistatyti(self):
        print(f'Sveiki, as esu  {self.vardas} {self.pavarde}.')

zmogus = Zmogus('Tomas', 'Matukas')
zmogus.prisistatyti()
print('---' * 20)
# Sukurkite paveldinčią klasę Studentas, kuri perrašo prisistatyti() metodą,
# pridėdama informaciją apie studijų programą.+
class Studentas(Zmogus):
    def __init__(self, vardas, pavarde, studiju_programa):
        super().__init__(vardas, pavarde)
        self.studiju_programa = studiju_programa

    def prisistatyti(self):
        super().prisistatyti()
        print(f'As studijuoju {self.studiju_programa} programa.')
studentas = Studentas('Tomas', 'Matukas', 'Fast Track')
studentas.prisistatyti()

print('---' * 20)

# Sukurkite klasę Universitetas, kuri naudoja kompoziciją, turėdama sąrašą
# Studentas objektų.

class Universitetas:
    def __init__(self, pavadinimas):
        self.pavadinimas = pavadinimas
        self.studentai = []

# Pridėkite metodus prideti_studenta() ir rodyti_visus_studentus().+
    def prideti_studenta(self, studentas):
        if isinstance(studentas, Studentas):
            self.studentai.append(studentas)

    def parodyti_studentus(self):
        print(f'Universiteto {self.pavadinimas} studentai:')
        for studentas in students:
            studentas.prisistatyti()
            print()

#  studentai
students = [
    Studentas("Jonas", "Jonaitis", "Matematika"),
    Studentas("Petras", "Petrauskas", "Fizika"),
    Studentas("Ieva", "Žukauskaitė", "Inžinerija"),
    Studentas("Mantas", "Skaistys", "Ekonomika"),
    Studentas("Aistė", "Jankauskaitė", "Psichologija")
]
# Parodykite visų studentų informaciją, pasitelkiant paveldėjimą, metodų perrašymą
# ir kompoziciją+
universitetas = Universitetas('Klaipedos Universitetas')

universitetas.prideti_studenta(studentas)
universitetas.parodyti_studentus()

print('---' * 20)

print(' - - - - - - - -  2. Papildoma Užduotis - - - - - ')
# 2. Papildoma Užduotis
# Užduotis:
# Sukurkite klasę Biblioteka, kurioje saugomi Knyga objektai.+
# • Klasė Knyga turi atributus pavadinimas, autorius, metai.+
# • Pridėkite metodus prideti_knyga(), istrinti_knyga(), rodyti_knygas().+
# • Išsaugokite ir įkelkite duomenis naudojant pickle modulį.+
# Papildoma užduotis:
# Sukurkite paieškos funkcionalumą, leidžiantį ieškoti knygų pagal pavadinimą arba autorių.+

import pickle


class Knyga:
    def __init__(self, pavadinimas, autorius, metai):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai

    def __str__(self):
        return f'{self.pavadinimas} by {self.autorius} ({self.metai})'


class Biblioteka:
    def __init__(self):
        self.knygos = []

    def prideti_knyga(self, knyga):
        self.knygos.append(knyga)

    def istrinti_knyga(self, pavadinimas):
        for knyga in self.knygos:
            if knyga.pavadinimas == pavadinimas:
                self.knygos.remove(knyga)
                return f'Knyga "{pavadinimas}" pašalinta.'
        return f'Knyga "{pavadinimas}" nerasta.'

    def rodyti_knygas(self):
        if self.knygos:
            for knyga in self.knygos:
                print(knyga)
        else:
            print('Biblioteka tuščia.')

    def ieskoti_knygos(self, ieškoti_pagal, vertė):
        rezultatai = []
        for knyga in self.knygos:
            if getattr(knyga, ieškoti_pagal) == vertė:
                rezultatai.append(knyga)
        return rezultatai


try:
    with open('biblioteka.pickle', mode='rb') as f:
        biblioteka = pickle.load(f)
except:
    biblioteka = Biblioteka()

# Adding 5 Lithuanian books about programming
books = [
    Knyga("Python programavimas", "Vaidotas Tamulaitis", 2019),
    Knyga("Java programavimas", "Tomas Stankevičius", 2021),
    Knyga("C++ praktika", "Aidas Paliulis", 2018),
    Knyga("Kurkime svetaines su HTML ir CSS", "Andrius Kazlauskas", 2020),
    Knyga("Duomenų struktūros ir algoritmai", "Marius Žukauskas", 2022)
]

# Add these books to the library
for knyga in books:
    biblioteka.prideti_knyga(knyga)

print('Sveiki atvyke i biblioteka!')

while True:
    print('\n1. Rodyti visas knygas.')
    print('2. Pridėti knygą.')
    print('3. Pašalinti knygą.')
    print('4. Ieškoti knygų.')
    print('5. Išeiti.')

    try:
        user_input = int(input('Pasirinkite veiksmą: '))
        if user_input < 1 or user_input > 5:
            raise ValueError
    except ValueError:
        print('Pasirinkite numerį nuo 1 iki 5.')
        continue

    if user_input == 5:
        with open('biblioteka.pickle', mode='wb') as f:
            pickle.dump(biblioteka, f)
        print('Iki!')
        break

    elif user_input == 1:
        biblioteka.rodyti_knygas()

    elif user_input == 2:
        pavadinimas = input('Įveskite knygos pavadinimą: ')
        autorius = input('Įveskite knygos autorių: ')
        metai = input('Įveskite knygos metus: ')
        try:
            metai = int(metai)
            knyga = Knyga(pavadinimas, autorius, metai)
            biblioteka.prideti_knyga(knyga)
            print(f'Knyga "{pavadinimas}" pridėta.')
        except ValueError:
            print('Metai turi būti skaičius.')

    elif user_input == 3:
        pavadinimas = input('Įveskite knygos pavadinimą, kurią norite pašalinti: ')
        print(biblioteka.istrinti_knyga(pavadinimas))

    elif user_input == 4:
        ieškoti_pagal = input('Ieškoti pagal (pavadinimas/ autorius): ').strip().lower()
        vertė = input('Įveskite reikšmę: ').strip()
        if ieškoti_pagal == 'pavadinimas' or ieškoti_pagal == 'autorius':
            rezultatai = biblioteka.ieskoti_knygos(ieškoti_pagal, vertė)
            if rezultatai:
                for knyga in rezultatai:
                    print(knyga)
            else:
                print('Nerasta knygų pagal šiuos kriterijus.')
        else:
            print('Pasirinkite galiojančią paieškos kategoriją (pavadinimas/ autorius).')

