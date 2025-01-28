from mylib.aritmetikosmodulis import dalink, atimk

print(' - - - - - Uzduotis 2 - - - - - - - -')

# Paprastas importavimas
# Užduotis 2:
# Sukurkite Python programą, kuri importuoja random modulį ir:
# 1. Sugeneruoja atsitiktinį skaičių nuo 1 iki 100.
# 2. Sugeneruoja atsitiktinį skaičių su uniform(), kuris yra tarp 1 ir 50.
# 3. Išspausdina abu rezultatus.

import random

print(random.randint(1, 100))
print(round(random.uniform(1, 50), 2))

print(' - - - - - Uzduotis 3 - - - - - - - -')

# 3. Specifinių funkcijų importavimas
# Užduotis 3:
# Sukurkite Python programą, kuri naudoja:
# 1. from random import randint, choice
# 2. Sugeneruoja atsitiktinį skaičių nuo 1 iki 10 naudojant randint().
# 3. Pasirenka atsitiktinį elementą iš sąrašo ['obuolys', 'bananas', 'kriaušė',
# 'vyšnia'] naudodama choice().
# 4. Išspausdina abu rezultatus.

from random import randint, choice
generate_random_number = randint(1, 10)
print(generate_random_number)

select_random_fruit = choice(['obuolys', 'bananas', 'kriaušė', 'vyšnia'])
print(select_random_fruit)

print(' - - - - - Uzduotis 4 - - - - - - - -')

# 4. Modulio trumpinimas naudojant alias
# Užduotis 4:
# Sukurkite Python programą, kuri:
# 1. Importuoja datetime modulį su alias dt.
# 2. Naudoja dt.datetime.now() funkciją, kad gautų dabartinę datą ir laiką.
# 3. Išspausdina rezultatą su formatu: Dabartinė data ir laikas: YYYY-MM-DD
# HH:MM:SS

import datetime as dt
print(f'Dabartinė data ir laikas: {dt.datetime.now()}')
print(f"Dabartinė data ir laikas: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


print(' - - - - - Uzduotis 5 - - - - - - - -')

# 5. Specifinių funkcijų importavimas su alias
# Užduotis 5:
# Sukurkite Python programą, kuri:
# 1. Importuoja sqrt funkciją iš math modulio su alias sq.
# 2. Apskaičiuoja kvadratinę šaknį iš 625 naudojant sq().
# 3. Išspausdina rezultatą.

from math import sqrt as sq
print(sq(625)) #atsakymas - 25.0

print(' - - - - - Uzduotis 6 - - - - - - - -')

# 6. Visko importavimas iš modulio (nerekomenduojamas būdas)
# Užduotis 6:
# 1. Sukurkite Python programą, kuri naudoja from math import *.
# 2. Apskaičiuoja sinusą iš 90 laipsnių (naudojant sin()).
# 3. Išspausdina rezultatą.
# 4. Parašykite komentaruose, kodėl šis metodas gali būti pavojingas dideliuose
# projektuose.

from math import *
print(sin(90)) #atsakymas - 0.8939966636005579

print(' - - - - - Uzduotis 7 - - - - - - - -')

# 7. Importai iš mūsų sukurto modulio
# Užduotis 7:
# 1. Sukurkite naują Python failą matematika.py.
# 2. Šiame faile parašykite funkcijas:
# a. sudetis(a, b), kuri grąžina dviejų skaičių sumą.
# b. daugyba(a, b), kuri grąžina dviejų skaičių sandaugą.
# 3. Sukurkite kitą Python failą main.py, kuris importuoja šias funkcijas ir jas iškviečia.

from mylib import matematika as mtk, matematika, matematika as m

res = mtk.sumuok(2, 9)
print(res) #atsakymas - 11

res = mtk.daugink(11, 7)
print(res) #atsakymas - 77


print(' - - - - - Uzduotis 8 - - - - - - - -')

# 8. Visas modulio importavimas
# Užduotis 8:
# 1. Sukurkite Python programą, kuri importuoja matematika modulį (sukurtą
# ankstesnėje užduotyje).
# 2. Naudoja matematika.sudetis(10, 20) ir matematika.daugyba(5, 4).
# 3. Išspausdina rezultatus.

res = matematika.sumuok(13, 17)
print(res) #atsakymas - 30

res = matematika.daugink(5, 15)
print(res) #atsakymas - 75

print(' - - - - - Uzduotis 9 - - - - - - - -')

# 9. Specifinių funkcijų importavimas
# Užduotis 9:
# 1. Naudodami from matematika import sudetis, daugyba, importuokite tik tas
# funkcijas, kurios reikalingos.
# 2. Paskaičiuokite sumą ir sandaugą skaičių 8 ir 3.
# 3. Išspausdinkite rezultatus.

res = matematika.sumuok(8, 3), matematika.daugink(8, 3)
print(res) #atsakymas - 11, 24

print(' - - - - - Uzduotis 10 - - - - - - - -')

# 10. Modulio trumpinimas naudojant alias
# Užduotis 10:
# 1. Importuokite matematika modulį kaip m.
# 2. Naudokite m.sudetis(12, 18) ir m.daugyba(7, 6).
# 3. Išspausdinkite rezultatus.

res = m.sumuok(12, 18)
print(res) #atsakymas - 30
res = m.daugink(7, 6)
print(res)#atsakymas - 42
#kitas variantas
print(m.sumuok(12, 18))
print(m.daugink(8, 3))

print(' - - - - - Uzduotis 11 - - - - - - - -')

# 11. Importai iš folderio
# Užduotis 11:
# 1. Sukurkite folderį moduliai.
# 2. Sukurkite šiame folderyje failą aritmetika.py su funkcijomis atimtis(a, b) ir
# dalyba(a, b).
# 3. Sukurkite main.py, kuris importuoja aritmetika ir iškviečia šias funkcijas.

import mylib
res = mylib.matematika.sumuok(3, 9)
print(res) #atsakymas - 12
res = mylib.aritmetikosmodulis.atimk(4, 2)
print(res) #atsakymas - 2

print(' - - - - - Uzduotis 12 - - - - - - - -')

# 12. Visas modulio importavimas iš folderio
# Užduotis 12:
# 1. Sukurkite Python programą, kuri importuoja moduliai.aritmetika.
# 2. Naudokite moduliai.aritmetika.atimtis(20, 5) ir
# moduliai.aritmetika.dalyba(10, 2).
# 3. Išspausdinkite rezultatus.
import mylib.aritmetikosmodulis as art
res = art.atimk(20, 5)
print(res) #atsakymas - 15
res = art.dalink(10, 2)
print(res) #atsakymas - 5.0

print(' - - - - - Uzduotis 13 - - - - - - - -')
# 13. Specifinių funkcijų importavimas iš folderio
# Užduotis 13:
# 1. Importuokite iš moduliai.aritmetika tik atimtis ir dalyba.
# 2. Paskaičiuokite 50 - 25 ir 100 / 4.
# 3. Išspausdinkite rezultatus.

from mylib.aritmetikosmodulis import atimk, dalink

print(atimk(50, 25), dalink(100, 4)) #atsakymas - (25) (25.0)

print(' - - - - - Uzduotis 14 - - - - - - - -')

# 14. Modulio trumpinimas naudojant alias iš folderio
# Užduotis 14:
# 1. Importuokite moduliai.aritmetika kaip ar.
# 2. Naudokite ar.atimtis(30, 10) ir ar.dalyba(50, 5).
# 3. Išspausdinkite rezultatus.

import mylib.aritmetikosmodulis as ar
res = ar.atimk(30, 10)
print(res) #atsakymas - 20
res = ar.dalink(50, 5)
print(res) #atsakymas - 10.0

print(' - - - - - Uzduotis 15 - - - - - - - -')

# 15. Importavimas viso folderio
# Užduotis 15:
# 1. Sukurkite __init__.py failą folderyje moduliai, kad jis būtų laikomas Python
# paketu.
# 2. Importuokite visą folderį import moduliai ir naudokite
# moduliai.aritmetika.atimtis(15, 5).
# 3. Išspausdinkite rezultatą.

import mylib
res = mylib.aritmetikosmodulis.atimk(15, 5)
print(res) #atsakymas - 10




