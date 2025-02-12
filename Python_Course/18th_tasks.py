print(' - - - - -- - - Uzduotis 1 - - - - - - - - - ')

# 1. Funkcijos kaip Pirmos Klasės Objektai
# Užduotis:
# Sukurkite šias funkcijas:
# 1. prideti_zenkliuka(tekstas) – prideda žvaigždutę * prie teksto pabaigos.
# 2. apversti_teksta(tekstas) – apverčia pateiktą tekstą.
# 3. Sukurkite funkciją apdoroti_teksta(tekstas, funkcija=None), kuri:
# a. Jei nurodyta funkcija, pritaiko ją tekstui.
# b. Jei funkcija nenurodyta, tiesiog grąžina tekstą mažosiomis raidėmis.
# Papildoma užduotis:
# Sukurkite funkciją keli_apdorojimai(tekstas, *funkcijos), kuri pritaiko kelias
# funkcijas iš eilės tam pačiam tekstui.

def  prideti_zenkliuka(tekstas):
    return  tekstas + '*'

def  apversti_teksta(tekstas):
    return tekstas [::-1]

def  apdoroti_teksta(tekstas, funkcija=None):
    if funkcija:
        return funkcija(tekstas)
    else:
        return tekstas.lower()

def keli_apdorojimai(tekstas, *funkcijos):
    for funkcija in funkcijos:
        tekstas = funkcija(tekstas)
    return tekstas

tekstas = 'Hello, World'

print(prideti_zenkliuka(tekstas))
print(apversti_teksta(tekstas))
print(apdoroti_teksta(tekstas))
print(apdoroti_teksta(tekstas, apversti_teksta))
print(apdoroti_teksta(tekstas))
print('-' * 30)
# Papildoma užduotis:
# Sukurkite funkciją keli_apdorojimai(tekstas, *funkcijos), kuri pritaiko kelias
# funkcijas iš eilės tam pačiam tekstui.
print(keli_apdorojimai(tekstas, apversti_teksta, prideti_zenkliuka))
print('-' * 30)

# #destytojo kodas:
#
# def prideti_zenkliuka(tekstas):
#     return tekstas + "*"
#
# def apversti_teksta(tekstas):
#     return tekstas[::-1]
#
# def apdoroti_teksta(tekstas, funkcija=None):
#     if funkcija:
#         return funkcija(tekstas)
#     return tekstas.lower()
#
# def keli_apdorojimai(tekstas, *args):
#     for funkcija in args:
#         tekstas = funkcija(tekstas)
#     return tekstas
#
# # Testavimas
# tekstas = "Sveiki Atvykę"
#
# print(apdoroti_teksta(tekstas, prideti_zenkliuka))
# print(apdoroti_teksta(tekstas, apversti_teksta))
# print(apdoroti_teksta(tekstas))
#
# print(keli_apdorojimai(tekstas, prideti_zenkliuka, apversti_teksta))

print(' - - - - -- - - Uzduotis 2 - - - - - - - - - ')

# 2. Dekoratoriai
# Užduotis:
# Sukurkite dekoratorių sekimo_dekoratorius, kuris:
# 1. Išveda žinutę prieš ir po funkcijos vykdymo:
# a. Prieš: „Vykdoma funkcija: <funkcijos_pavadinimas>“
# b. Po: „Funkcija baigta!“
# 2. Pridėkite dekoratorių prie funkcijos dauginti(a, b), kuri grąžina dviejų skaičių
# sandaugą.
# Papildoma užduotis:
# Pridėkite funkciją dalinti(a, b) su tuo pačiu dekoratoriumi. Jei b == 0, grąžinkite
# klaidos pranešimą.

def sekimo_dekoratorius(funkcija):
    def apvalkalas(a, b):
        print(f'Vykdoma funkcija: {funkcija.__name__}')

        rezultatas = funkcija(a, b)

        print('Funkcija baigta!')
        return rezultatas
    return apvalkalas

@sekimo_dekoratorius
def daugyba(a, b):
    return a * b

@sekimo_dekoratorius
def dalyba(a, b):
    if b == 0 or b < 0 :
        return 'klaida, is 0 ir <0 negalima'
    return a / b

print(daugyba(4, 5))
print('-' * 30)
print(dalyba(10, 2))
print('-' * 30)
print(dalyba(10, -90))
print('-' * 30)

print(' - - - - -- - - Uzduotis 3 - - - - - - - - - ')

# 3. Iteratoriai
# Užduotis:
# Sukurkite klasę SkaiciuSekosIteratorius, kuri:
# 1. Inicializuojama su pradiniu ir galiniu skaičiumi.
# 2. Leidžia iteruoti nuo pradinio iki galinio skaičiaus imtinai.
# 3. Grąžina skaičius kas antrą žingsnį.
# Papildoma užduotis:
# Pridėkite metodą atgaline_seka(), kuris grąžina skaičius atvirkštine tvarka.

class SkaiciuSekosIteratorius:
    def __init__(self, pradzia, pabaiga):
        self.pradzia = pradzia
        self.pabaiga = pabaiga

    def __iter__(self):
        current = self.pradzia
        while current <= self.pabaiga:
            yield current
            current += 2

    def atgaline_seka(self):
        current = self.pabaiga
        while current >= self.pradzia:
            yield current
            current -= 2

sekos_iteratorius = SkaiciuSekosIteratorius(1, 10)

print("Sekos iteratorius:")
for skaicius in sekos_iteratorius:
    print(skaicius)

print("\nAtgalinė seka:")
for skaicius in sekos_iteratorius.atgaline_seka():
    print(skaicius)

# # destytojo kodas
# class SkaiciuSekosIteratorius:
#     def __init__(self, pradinis, galinis):
#         self.pradinis = pradinis
#         self.galinis = galinis
#
#     def __iter__(self):
#         return iter(range(self.pradinis, self.galinis + 1, 2))
#
#     def atgaline_seka(self):
#         return [i for i in range(self.galinis, self.pradinis - 1, -2)]
#
# # Pavyzdys naudojimui
# skaiciai = SkaiciuSekosIteratorius(1, 10)
#
# print("Sekos iteravimas:")
# for skaicius in skaiciai:
#     print(skaicius)
#
# print("Atgalinė seka:")
# print(skaiciai.atgaline_seka())

print(' - - - - -- - - Uzduotis 4 - - - - - - - - - ')

# 4. Generatoriai
# Užduotis:
# Sukurkite generatorių fib_generator(n), kuris grąžina pirmus n Fibonacci skaičius.
# • Fibonacci seka: 0, 1, 1, 2, 3, 5, 8, 13, …
# Papildoma užduotis:
# Sukurkite generatorių filtruoti_lyginius(seka), kuris iš pateiktos skaičių sekos
# grąžina tik lyginius skaičius.

def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def filtruoti_lyginius(seka):
    for sk in seka:
        if sk % 2 == 0:
            yield sk

n = 10
fibonacci_seka = fib_generator(n)
print('Pirmi 10 Fibonacci skaičiai:', list(fibonacci_seka))

print('-' * 30)

fibonacci_seka = fib_generator(n)
lyginiu_fib = filtruoti_lyginius(fibonacci_seka)
print('Lyginiai Fibonacci skaičiai: ', list(lyginiu_fib))