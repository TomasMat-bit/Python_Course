import time
from keyword import kwlist

print('- - - - - - - - Pažangios Python Funkcijos - - - - - - - - - ')
print('- - - - - - - - Funkcijos kaip Pirmos Klasės Objektai - - - - - - - - - ')
print('- - - - - - - - Pavyzdys: Funkcijos perdavimas kaip argumentas - - - - - - - - - ')

def apversti_teksta(tekstas):
    return tekstas[::-1]

def apversti_sakini(tekstas):
    return " ".join(tekstas.split()[::-1])
print('-' * 30)
print(apversti_teksta("ABC")) # CBA
print('-' * 30)
print(apversti_sakini("Labas Pasauli Dabar!!!")) # Dabar!!! Pasauli Labas
print('-' * 30)
def i_didziasias(tekstas, funkcija=None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.upper()

print(i_didziasias("abc", funkcija=apversti_teksta)) # CBA
print('-' * 30)
print(i_didziasias("Labas Pasauli Dabar!!!", funkcija=apversti_sakini)) # DABAR!!! PASAULI LABAS
print('-' * 30)

def apversti_teksta(tekstas):
    return tekstas[::-1]

# print(apversti_teksta('labas'))

def apversti_sakini(tekstas):
    return " ".join(tekstas.split()[::-1])

# print(apversti_sakini('Hello World My Name Is Python'))

def sudetinga_funkcija(func):
    for i in range(1, 10):
        print(func('Super tekstas 123 312'))

def super_sudetinga_funkcija(func):
    for i in range(1, 20):
        print(func('Labas'))

# sudetinga_funkcija(apversti_sakini)
# super_sudetinga_funkcija(apversti_teksta)

def i_didziasias(tekstas, funkcija=None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.upper()

print(
    i_didziasias('labas', apversti_teksta)
)
print('-' * 30)

print('- - - - - - - - Pavyzdys: Paprastas Dekoratorius - - - - - - - - - ')

# # flasko ir jango naudoja labai daug savo dekoratoriu.
#
# def registratorius(funkcija):
#     print(f'funkcija: {funkcija}')
#     def apvalkalas(argumentas):
#         print(f'argumentas: {argumentas}')
#         rezultatas = funkcija(argumentas)
#         if rezultatas % 2 == 0:
#             print(f'{rezultatas} yra lyginis')
#         else:
#             print(f'{rezultatas} yra nelyginis')
#         return rezultatas
#     return apvalkalas
#
# @registratorius
# def kvadratu(skaicius):
#     return skaicius ** 2
#
# print(kvadratu(8))
#
# def top_level_delay(seconds):
#     def returner_of_delayed_func(func):
#         def wrapper(*args, **kwargs):
#             print(f'FUnkcijos darbas prasides po: {seconds}')
#             time.sleep(seconds)
#             res = func(*args, *kwargs)
#             return res
#         return wrapper
#     return returner_of_delayed_func
#
# @top_level_delay(9)
# def grazink500():
#     return 500
#
# @top_level_delay(15)
# def vydkyk_aritmetika(skaicius1, skaicius2, veiksmas=None):
#     if veiksmas == 'atimtis':
#         return skaicius1 - skaicius2
#
# res = grazink500()
# print(res)
#
# res = vydkyk_aritmetika(100, 1, 'atimtis')
# print(res)


print('- - - - - - - - Pavyzdys: Vartotojo Apibrėžtas Iteratorius  - - - - - - - - - ')

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    def __iter__(self):
        return iter([self.vardas, self.pavarde, self.pareigos, 'Labas' , 'Mano' , 'Vardas' , self.vardas])

darbuotojas = Darbuotojas("Jonas", "Jonaitis", "Programuotojas")
for savybe in darbuotojas:
    print(savybe)
print('-' * 30)

# listas = ['sausis' , 'vasaris' , 'kovas']
# listo_iteratorius = iter(listas)
# print(listas)
# print(listo_iteratorius)
#
# res = next(listo_iteratorius)
# print(res)
#
# res = next(listo_iteratorius)
# print(res)
#
# res = next(listo_iteratorius)
# print(res)
print('-' * 30)

listas = ['sausis' , 'vasaris' , 'kovas']
while True:
    try:
        element = listas.pop(0)
        print(element)
    except IndexError:
        print('nera elementu')
        break

print('- - - - - - - - Pavyzdys: Generatorinė Funkcija  - - - - - - - - - ')

def skaiciuok_iki(max_reiksme):
    skaicius = 0
    while skaicius < max_reiksme:
        yield skaicius
        skaicius += 1
        print('-' * 30)


for numeris in skaiciuok_iki(5):
    print(numeris)

employees = [x * x for x in range(6)]
for employee in employees:
    print(employee)

def squares(length):
    for i in range(length):
        yield i * i
for square in squares(6):
    print(square)







