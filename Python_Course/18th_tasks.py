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

print(' - - - - -- - - Uzduotis 2 - - - - - - - - - ')


