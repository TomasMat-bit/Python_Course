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
    if b == 0:
        return 'klaida, is 0 negalima'
    return a / b

print(daugyba(4, 5))
print('-' * 30)
print(dalyba(10, 2))
print('-' * 30)
print(dalyba(10, 0))
print('-' * 30)

print(' - - - - -- - - Uzduotis 3 - - - - - - - - - ')




getattr(g
        getattr(getattr(
            float
        )))


