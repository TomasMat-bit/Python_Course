from xml.dom.minidom import Element

print(' --- -   -   -   -Gyvūnų klasės ir metodai- - - - - - - - ')

class Kate:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f"{self.vardas} bėgu!!!")

    def miaukseti(self):
        print(f"{self.vardas} sako MIAU!!!")

print(' --- -   -   -   - Paveldėjimas (Inheritance)- - - - - - - - ')

class Gyvunas:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f"{self.vardas} bėgu!!!")

class Zinduolis:
    def __init__(self, geras):
        self.geras = geras

class Kate(Gyvunas):
    def miaukseti(self):
        print(f"{self.vardas} sako MIAU!!!")

class Suo(Gyvunas):
    def lot(self):
        print(f'{self.vardas} loja!!!')

cat = Kate('Murkis', 'Geltinas')
cat.begti()

dog = Suo('Jimm', 'Margas')
dog.begti()

print(' --- -   -   -   - Komponavimas (Composition) - - - - - - - - ')

class Stack:
    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        return self.data.pop()

class Element:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2

    def __str__(self):
        return(f'{self.item1} {self.item2}')

elems = [
    Element(1, 2),
    Element(3, 4),
    Element(5, 6)
    ]

stck = Stack()

for  i in elems:
    stck.push(i)

a = stck.pop()

for i in stck.data:
    print(i)
print('-' * 11)
print(a)

print(' --- -   -   -   - Konstruktoriaus Perrašymas - - - - - - - - ')

class Asmuo:
    def __init__(self, vardas, pavarde, gim_metai):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gim_metai = gim_metai

class MokinioTevas(Asmuo):
    def __init__(self, vardas, pavarde, gim_metai, darboviete):
        super().__init__(vardas, pavarde, gim_metai)
        self.darboviete = darboviete

tevas = MokinioTevas(1,2,3,4)

print(tevas.vardas)
print(tevas.pavarde)
print(tevas.gim_metai)
print(tevas.darboviete)

print(' --- -   -   -   - Kitų Metodų Perrašymas (Overriding) - - - - - - - - ')

class Mygtukas:
    def deaktyvuoti(self):
        print("Mygtukas deaktyvuotas")

class RaudonasMygtukas(Mygtukas):
    def deaktyvuoti(self):
        super().deaktyvuoti()
        print("Spalva pasikeitė į rausvą")

class RaudonasMygtukas(Mygtukas):
    def deaktyvuoti(self):
        super().deaktyvuoti()
        print('Aciu, kad pirkote')
        print('Spalva pasikeite i rausva')

red_btn = RaudonasMygtukas()
red_btn.deaktyvuoti()

print(' --- -   -   -   - Objektų Išsaugojimas į Failą - - - - - - - - ')
print(' --- -   -   -   - Objektų Klasė - - - - - - - - ')

import datetime

class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year

    def __str__(self):
        return f"Namas {self.year} pastatymo, kaina - {self.price}, amžius - {self.get_age()}"

print(' --- -   -   -   - Objektų Įkėlimas iš Failo - - - - - - - - ')

# import pickle
#
# try:
#     with open('namai.pickle', mode='rb') as f:
#         houses_kaupiklis = pickle.load(f)
# except FileNotFoundError:
#     houses_kaupiklis = []
#
# # with open('info.txt', mode='r') as file:
# #     a = file.read()
# # print(a)

import pickle
import datetime

class House:
    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year

    def __str__(self):
        return f"Namas {self.year} pastatymo, kaina {self.price}, amžius - {self.get_age()}"

try:
    with open('namai.pickle', mode='rb') as f:
        houses_kaupiklis = pickle.load(f)
except:
    houses_kaupiklis = []

print('Welcome to ultimate real estate program!')

while True:
    print('1. Show all houses.')
    print('2. Add house.')
    print('3. Remove last house.')
    print('4. Exit.')
    print('\n')
    try:
        user_input = int(input('Please choose action: '))
        if user_input < 1 or user_input > 4:
            raise ValueError
    except ValueError:
        print('Please choose number from 1 to 4.')
        continue
    if user_input == 4:
        with open('namai.pickle', mode='wb') as f:
            pickle.dump(houses_kaupiklis, f)
        print('Bye!')
        break
    elif user_input == 1:
        print()
        for house in houses_kaupiklis:
            print(house)
        print()
    elif user_input == 2:
        try:
            price = int(input('Price: '))
            year = int(input('year: '))
            new_house = House(price, year)
            houses_kaupiklis.append(new_house)
            print()
        except ValueError:
            print('Values should be integers')
    elif user_input == 3:
        houses_kaupiklis.pop()




# print(' --- -   -   -   - Naujo Objekto Pridėjimas - - - - - - - - ')
#
# while True:
#     print("Namų sąrašas")
#     for house in houses_kaupiklis:
#         print(house)
#
#     quit_choice = input("įveskite bet kokį simbolį kad išeiti Enter, tęsti įvedimą")
#     if quit_choice:
#         break
#
#     year = int(input("Įveskite metus "))
#     price = int(input("Įveskite kainą "))
#
#     house_instance = House(price, year)
#     houses_kaupiklis.append(house_instance)




